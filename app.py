import streamlit as st

# 1. 设定“氛围”：页面图标和标题
st.set_page_config(page_title="Vibe Dashboard", page_icon="🌈")

# 2. 注入正反馈：五彩纸屑
st.balloons()

# 3. 极简页眉
st.title("✨ 我的 Vibe Coding 空间")
st.markdown("> *“代码不重要，感觉才重要。”*")

# 4. 做三个漂亮的“数据卡片” (Metrics)
# 这就是 Vibe Coding 的精髓：用最简单的指令做出最专业的 UI
col1, col2, col3 = st.columns(3)
col1.metric("今日心情", "100%", "↑ 10%")
col2.metric("编程技能", "LV.1", "Ready")
col3.metric("外贸订单", "12 个", "Hot")

# 5. 加入一个“魔法按钮”
st.divider() # 画一条优雅的分隔线
if st.button("释放压力，触发极光"):
    st.snow()
    st.toast("极光已送达！今日好运+1", icon='✨')

# 6. 加入一个带“氛围感”的互动
mood_color = st.select_slider(
    '滑动调节今天的氛围颜色',
    options=['灰暗', '平淡', '温暖', '火热', '炸裂']
)

if mood_color == '炸裂':
    st.error("BOOM! 你的能量已经溢出屏幕了！")
    st.balloons()
