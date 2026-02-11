import streamlit as st

st.balloons() # 一进来就喷气球庆功！
st.title"("这是我的第一个神器！")
name = st.text_input("请输入你的名字：")
if name:
    st.write(f"你好 {name}，你已经正式跨入了开发者的大门！")
    
if st.button("点我试试"):
    st.snow() # 点一下按钮会下雪
    st.success("代码运行成功！正反馈拉满！")
