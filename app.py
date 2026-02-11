import streamlit as st

# 1. 页面配置
st.set_page_config(page_title="医美器械报价系统", page_icon="🩺")

# 2. 标题和气球正反馈
st.balloons()
st.title("💎 医美产品展示与报价")

# 3. 展示产品图片
# 这里的 "product.jpg" 必须和你刚才上传的文件名一模一样
try:
    st.image("product.jpg", caption="当前主推：专业级医美设备", use_container_width=True)
except:
    st.warning("提示：请在 GitHub 仓库上传一张名为 product.jpg 的图片，图片就会显示在这里。")

# 4. 报价计算逻辑
st.write("---")
col1, col2 = st.columns(2) # 把页面分成两列，左边选配置，右边出结果

with col1:
    st.subheader("配置选择")
    model = st.selectbox("选择型号：", ["标准款", "旗舰款", "定制款"])
    base_price = 15000 if model == "标准款" else 25000
    quantity = st.number_input("订购数量：", min_value=1, value=1)

with col2:
    st.subheader("实时报价")
    total_usd = base_price * quantity
    st.metric(label="总计金额 (USD)", value=f"${total_usd:,}")
    
    # 汇率换算逻辑
    rate = 7.2
    total_cny = total_usd * rate
    st.write(f"折合人民币：¥{total_cny:,.2f}")

# 5. 生成合同预览
if st.button("生成电子报价单预览"):
    st.snow()
    st.write(f"### 报价单预览")
    st.info(f"项目：{model} 医美设备\n\n数量：{quantity}\n\n状态：库存充足")
