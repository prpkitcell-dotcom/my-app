import streamlit as st

# 1. 页面设置
st.set_page_config(page_title="外贸成交助手", page_icon="💰")
st.balloons()

# 2. 标题
st.title("⚖️ 外贸报价与汇率换算器")
st.write("---")

# 3. 汇率换算模块
st.header("💵 实时汇率换算")
# 假设当前汇率是 7.2，你可以手动改这个数字
exchange_rate = st.number_input("当前美金对人民币汇率：", value=7.20, step=0.01)

usd_amount = st.number_input("请输入美金金额 ($)：", min_value=0.0, value=1000.0)
cny_result = usd_amount * exchange_rate

# 用醒目的方式显示结果
st.metric(label="换算成人民币 (¥)", value=f"¥{cny_result:,.2f}")

st.write("---")

# 4. 产品报价小工具
st.header("📦 产品报价记录")
product_name = st.text_input("产品名称（如：医疗美容仪）：", "医用激光设备")
cost = st.number_input("成本价 (¥)：", value=5000.0)

if st.button("计算利润率"):
    profit = cny_result - cost
    profit_margin = (profit / cny_result) * 100 if cny_result > 0 else 0
    
    if profit > 0:
        st.success(f"🎉 预估利润：¥{profit:,.2f} | 利润率：{profit_margin:.2f}%")
        st.snow()
    else:
        st.error(f"⚠️ 预估亏损：¥{profit:,.2f}，请重新核算报价！")

# 5. 底部正反馈
st.info("💡 提示：你可以把这个网页收藏到手机浏览器，出差谈客户时随时计算。")
