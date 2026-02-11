import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. 页面配置与美化 ---
st.set_page_config(page_title="外贸全能管家", layout="wide", page_icon="💼")

# 注入一点正反馈：今日份的好运
st.balloons()

# --- 2. 标题与核心指标 ---
st.title("🛡️ 医疗美容外贸客户管理系统 (CRM)")
st.markdown(f"**今天是：{datetime.now().strftime('%Y-%m-%d')}** | 助你签下大单！")

# 模拟三个关键指标
col1, col2, col3, col4 = st.columns(4)
col1.metric("本月询盘", "42", "↑ 5")
col2.metric("在谈订单", "$128,500", "↑ 12%")
col3.metric("本月成交", "8 个", "Target: 10")
col4.metric("客户活跃度", "92%", "Excellent")

st.divider()

# --- 3. 客户数据录入区（模拟数据库） ---
st.header("📋 客户动态管理")

# 我们创建一个初始表格数据
if 'customer_data' not in st.session_state:
    st.session_state.customer_data = pd.DataFrame([
        {"客户名称": "Dubai Aesthetic Clinic", "国家": "阿联酋", "产品意向": "激光脱毛仪", "状态": "报价中", "预计金额": 15000},
        {"客户名称": "Paris Medical Group", "国家": "法国", "产品意向": "皮秒激光", "状态": "待付款", "预计金额": 32000},
        {"客户名称": "Seoul Skin Center", "国家": "韩国", "产品意向": "热玛吉代工", "状态": "已成交", "预计金额": 28000},
    ])

# 核心功能：数据编辑器（你可以直接像 Excel 这样改）
edited_df = st.data_editor(
    st.session_state.customer_data,
    num_rows="dynamic", # 允许你动态增加行
    use_container_width=True,
    column_config={
        "状态": st.column_config.SelectboxColumn(
            options=["初次联系", "报价中", "样机测试", "待付款", "已成交", "售后中"]
        ),
        "预计金额": st.column_config.NumberColumn(format="$ %d")
    }
)

# 保存修改
if st.button("💾 保存所有修改"):
    st.session_state.customer_data = edited_df
    st.toast("客户数据已实时保存！", icon="✅")

st.divider()

# --- 4. 业务深度互动 ---
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("💡 智能报价建议")
    client_name = st.selectbox("选择目标客户进行分析：", edited_df["客户名称"])
    discount = st.slider("给予折扣范围 (%)", 0, 20, 5)
    
    # 查找选定客户的价格
    base_price = edited_df[edited_df["客户名称"] == client_name]["预计金额"].values[0]
    final_price = base_price * (1 - discount/100)
    
    st.warning(f"对 {client_name} 的最终建议报价为：**${final_price:,.2f}**")
    if st.button("生成报价草案"):
        st.snow()
        st.info("报价草案已生成，已准备好发送至您的邮箱。")

with right_col:
    st.subheader("📊 业务分布概览")
    # 简单统计图表
    status_counts = edited_df["状态"].value_counts()
    st.bar_chart(status_counts)

# --- 5. 底部贴心小工具 ---
with st.expander("🛠️ 外贸常用小工具"):
    st.write("1. **时差对照**：迪拜时间 = 北京时间 - 4小时")
    st.write("2. **单位转换**：1 英寸 = 2.54 厘米 (常用于仪器屏幕规格说明)")
