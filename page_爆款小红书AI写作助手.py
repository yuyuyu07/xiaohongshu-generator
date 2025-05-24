from langchain_组件 import xiaohongshu_generator
import streamlit as st

# +------------------------------------------------------------------+
# |                            创建 网页组件                            |
# +------------------------------------------------------------------+
# 侧边栏 布局
with st.sidebar:  # 侧边栏 布局
    st_api_key = st.text_input("请输入API密钥:", type="password")  # 密码 输入框 # 返回 文字
    st.markdown("[API获取地址](https://ai.google.dev/gemini-api/docs?hl=zh-cn)")
    st.markdown("---")
    st.markdown("""
    ### 当前模型: 
    **gemini-2.0-flash**
    """)

# 显示 大标题
st.title("爆款小红书写作助手📝")     # 显示 大标题
st_输入 = st.text_input("写入主题")  # 行文字 输入框  # 返回 文字
st_按钮 = st.button("开始写作")      # 按钮 交互 # 返回 布尔值（点击True，不按False)

# +------------------------------------------------------------------+
# |                             提交前 检查                            |
# +------------------------------------------------------------------+
# 检测api_key是否输入:
if st_按钮 and not st_api_key:  # 如果 点击按钮 并没有 输入 AIP密钥
    st.info("请输入API密钥")  # 提醒 提示
    st.stop()               # 终止 # 类似break

# 检测视频主题是否输入:
if st_按钮 and not st_输入:   # 如果 点击按钮 并没有 输入 主题
    st.info("请输入文案主题")  # 提醒 提示
    st.stop()               # 终止 # 类似break

# +------------------------------------------------------------------+
# |                              提交                                 |
# +------------------------------------------------------------------+
# 提交 调用自定义函数
if st_按钮:
    # 加载等待提示
    with st.spinner("AI正在思考中，请等待..."):  # 使用 st.spinner 创建一个加载动画，提示用户 AI 正在思考 # 只要以下代码没有运行完，就会一直提示正在加载
        结果 = xiaohongshu_generator(st_api_key,st_输入) # 调用函数 返回 结果

    # 成功 提示
    st.success("小红书文案生成成功")   # 成功 提示
    st.divider()  # 显示 分割线

    # +---------------------------------------------------+
    # |                    显示生成内容                      |
    # +---------------------------------------------------+
    # 2列布局
    columns1, columns2 = st.columns(2)  # 3列 布局  # 返回 列表
    with columns1:  # 第一列
        # 显示 主题
        st.subheader("🖍小红书主题")  # 显示 副标题
        st.markdown("##### 标题1")
        st.write(结果.主_题[0])
        st.markdown("##### 标题2")
        st.write(结果.主_题[1])
        st.markdown("##### 标题3")
        st.write(结果.主_题[2])
        st.markdown("##### 标题4")
        st.write(结果.主_题[3])
        st.markdown("##### 标题5")
        st.write(结果.主_题[4])

    with columns2:  # 第二列
        # 显示 脚本
        st.subheader("📄小红书文案")  # 显示 副标题
        st.write(结果.内_容)

# streamlit run page_爆款小红书AI写作助手.py