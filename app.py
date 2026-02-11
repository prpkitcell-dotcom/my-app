import streamlit as st

st.set_page_config(page_title="常州外贸助手", layout="centered")

# 双重惊喜！
st.balloons()
st.snow()

st.title("🌟 我的专业外贸 App")

# 替代图片方案
st.success("✅ 设备模型已加载")
st.write("### [ 🏥 专业医疗美容设备 ]")
st.write("---")

# 报价逻辑
price = st.slider("设定美金单价：", 1000, 50000, 15000)
num = st.number_input("订购数量：", value=1)
st.metric("总金额 (USD)", f"${price * num:,}")

st.info("快看！即便没有外部图片，你的软件逻辑依然是完美的。")
