import streamlit as st

# 1. 自动撒花庆祝成功
st.balloons()

# 2. 这里的括号和引号全是英文格式，千万不要手动改
st.title("我的第一个 AI 智能 App")

# 3. 互动模块
name = st.text_input("请输入你的名字：", "天才开发者")

if st.button("启动惊喜"):
    st.snow()
    st.success(f"太棒了 {name}！你已经成功修复了所有报错！")
    st.write("现在的你已经是一名初级开发者了。")

# 4. 进度条正反馈
st.progress(100)
st.info("项目状态：部署成功 🚀")
