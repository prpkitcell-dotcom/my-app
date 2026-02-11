import streamlit as st

# 1. 自动触发正反馈效果
st.balloons() 

# 2. 设置一个大标题（注意括号和引号都是英文）
st.title("我的第一个 AI 智能 App")

# 3. 添加一个简单的互动
name = st.text_input("请输入你的大名：", "未来开发者")

# 4. 逻辑判断
if st.button("点我启动惊喜"):
    st.write(f"你好，{name}！恭喜你成功修复了代码报错。")
    st.snow() # 屏幕会下雪
   st.error("这证明你已经具备了解决问题的开发者潜质！")
st.progress(80)
# 5. 展示一张图片或状态
st.info("项目进度：已完成 100% 部署测试")
