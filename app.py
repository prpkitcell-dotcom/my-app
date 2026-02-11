import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="外贸精英助手", page_icon="🌍")

# 2. 炫酷开场
st.balloons()
st.title("🚀 外贸业务增长工作台")

# 3. 侧边栏：模拟客户信息管理
with st.sidebar:
    st.header("客户档案管理")
    client_name = st.text_input("海外客户名称：", "Dubai Clinic")
    product_type = st.selectbox("意向产品线：", ["医疗美容仪器", "诊所耗材", "实验室设备"])
    st.write("---")
    st.info("💡 提示：填写后主界面将同步更新")

# 4. 主界面互动
st.subheader(f"📅 正在为 {client_name} 生成报价方案")

# 模拟一个进度条，模拟AI正在计算
progress_text = "方案优化中，请稍候..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

# 5. 核心正反馈按钮
if st.button("生成今日业务报告"):
    st.snow()
    st.success(f"✅ 已成功录入：{client_name} 的 {product_type} 询盘")
    st.metric(label="预计成交金额", value="$12,500", delta="+15%")
    st.info("加油！距离本月外贸业绩目标还差 20%。")

# 6. 小彩蛋：心情打卡
mood = st.feedback("stars")
if mood is not None:
    st.write("感谢打分！保持好心情是谈成大单的关键。")
