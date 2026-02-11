import streamlit as st
import datetime

# --- 1. 页面整体设置 ---
st.set_page_config(page_title="医美器械海外报价系统", page_icon="🏥", layout="wide")

# --- 2. 这里的正反馈：进场特效 ---
st.balloons()
st.title("🌍 医美器械：全球询盘报价工作台")
st.markdown("---")

# --- 3. 核心功能区：采用左右分栏布局 ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🖼️ 产品视觉展示")
    # 使用一张高质量的医疗设备网图，确保小白不需要手动上传也能看到图片
    st.image("https://images.unsplash.com/photo-1579152276502-545a248a9931?q=80&w=800", 
             caption="主推型号：高能激光美容仪", use_container_width=True)
    
    st.info("💡 建议：在外贸谈单时，清晰的实拍图能提高 30% 的成交率。")

with col2:
    st.header("💰 实时报价计算器")
    
    # 获取用户输入
    product_model = st.selectbox("选择仪器型号：", ["基础修复款", "旗舰全能款", "诊所定制版"])
    quantity = st.number_input("订购数量 (台)：", min_value=1, value=1, step=1)
    
    # 模拟报价逻辑（外贸人可以根据需求自己改数字）
    price_map = {"基础修复款": 8500, "旗舰全能款": 15000, "诊所定制版": 22000}
    unit_price = price_map[product_model]
    
    total_usd = unit_price * quantity
    
    # 汇率设置（常州外贸人最关心的数字）
    exchange_rate = st.number_input("今日美金汇率 (USD/CNY)：", value=7.21, step=0.01)
    total_cny = total_usd * exchange_rate

    # 结果展示
    st.metric(label="总报价 (USD)", value=f"${total_usd:,}")
    st.metric(label="折合人民币 (CNY)", value=f"¥{total_cny:,.2f}", delta="实时换算")

st.markdown("---")

# --- 4. 客户询盘记录（留言板功能） ---
st.header("📝 海外客户询盘登记")
with st.form("inquiry_form"):
    c_name = st.text_input("客户名称/诊所名称：")
    c_email = st.text_input("联系邮箱 (Email)：")
    c_message = st.text_area("需求备注：")
    
    submit_button = st.form_submit_button("提交询盘并锁定报价")
    
    if submit_button:
        if c_name and c_email:
            st.snow() # 提交成功，下场雪庆祝
            st.success(f"✅ 成功！{c_name} 的询盘已记录。")
            # 在这里我们模拟保存了数据
            st.write(f"**记录时间：** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
            st.write(f"**报价单摘要：** {quantity}台 {product_model}，总计 ${total_usd:,}")
        else:
            st.error("❌ 请务必填写客户名称和邮箱，方便后续跟进。")

# --- 5. 底部版权 ---
st.caption("© 2026 常州外贸精英助手 | 由 Streamlit 强力驱动")
