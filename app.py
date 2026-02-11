import streamlit as st
import pandas as pd
from datetime import datetime

# 页面配置：设置成宽屏模式
st.set_page_config(page_title="医美器械专业报价系统", layout="wide", page_icon="📝")

# 氛围感：雪花特效（象征高端医美冰爽感）
st.snow()

# --- 侧边栏：全局设置 ---
with st.sidebar:
    st.header("⚙️ 核心参数设置")
    # 汇率可以手动调节，确保报价实时性
    rate = st.number_input("今日美金汇率 (USD/CNY)", value=7.22, step=0.01)
    tax_rate = st.slider("预估出口退税率 (%)", 0, 13, 13)
    st.divider()
    st.info("💡 提示：修改汇率后，所有报价将自动重新计算。")

# --- 主界面：报价器 ---
st.title("🏥 医美器械海外报价工作台")
st.write(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}")

# 第一部分：产品选择与基础报价
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("1. 选择产品与配置")
    # 模拟医美产品数据
    product_data = {
        "热玛吉代工设备 (旗舰版)": 12000,
        "光子嫩肤仪 (诊所专用)": 8500,
        "PRP 高速离心机": 1200,
        "医用水氧动力仪": 3500
    }
    
    selected_product = st.selectbox("产品名称", list(product_data.keys()))
    base_price_usd = product_data[selected_product]
    
    qty = st.number_input("订购数量 (Sets)", min_value=1, value=1)
    discount = st.slider("客户折扣 (%)", 0, 30, 0)

with col2:
    st.subheader("2. 物流与杂费")
    shipping_method = st.radio("运输方式", ["空运 (Air)", "海运 (Sea)", "快递 (Express)"])
    shipping_fee = st.number_input("单台预估运费 (USD)", value=150 if shipping_method == "空运 (Air)" else 50)

# --- 第二部分：自动计算核心数据 ---
st.divider()
st.subheader("💰 报价明细汇总")

# 计算逻辑
unit_price_after_discount = base_price_usd * (1 - discount/100)
total_product_usd = unit_price_after_discount * qty
total_shipping_usd = shipping_fee * qty
final_total_usd = total_product_usd + total_shipping_usd
final_total_cny = final_total_usd * rate

# 视觉反馈卡片
res1, res2, res3 = st.columns(3)
res1.metric("单台成交价 (USD)", f"${unit_price_after_discount:,.2f}")
res2.metric("总金额 (USD)", f"${final_total_usd:,.2f}", delta=f"含运费 ${total_shipping_usd}")
res3.metric("折合人民币 (CNY)", f"¥{final_total_cny:,.2f}", help="按侧边栏汇率计算")

# --- 第三部分：专业建议与导出 ---
st.divider()
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("📈 利润分析")
    # 假设一个简单的成本线
    estimated_cost_cny = (base_price_usd * 0.5) * rate 
    profit_cny = final_total_cny - (estimated_cost_cny * qty)
    
    if profit_cny > 0:
        st.success(f"预计毛利：¥{profit_cny:,.2f} (含退税)")
    else:
        st.error("警告：当前报价可能低于成本线，请核算！")

with col_b:
    st.subheader("📄 快捷操作")
    if st.button("🚀 生成正式报价单草案"):
        st.balloons()
        st.toast("报价单已准备好，可截图发给客户！")
        st.code(f"""
        QUOTATION PREVIEW
        -----------------
        Product: {selected_product}
        Quantity: {qty}
        Unit Price: ${unit_price_after_discount:,.2f}
        Shipping: ${total_shipping_usd} ({shipping_method})
        -----------------
        Total Amount: ${final_total_usd:,.2f}
        Validity: 7 Days
        """)
