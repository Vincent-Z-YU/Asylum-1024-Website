import streamlit as st
import pandas as pd

# --------------------------
# 页面设置（必须放最前面）
# --------------------------
st.set_page_config(
    page_title="疯人院官网演示",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 侧边栏
with st.sidebar:
    st.title("👉 导航")
    choice = st.radio(
        "menu",
        ["首页","结构","我们","医疗＆接待","更多","streamlit可用功能展示"],
        label_visibility="collapsed"
    )
    st.divider()
    st.error("0022：这里的演示我就暂时先保留了，还有院长你最爱的抽象套娃")
    st.subheader("选择")
    theme = st.selectbox("演示", ["a", "b"])
    joke = st.checkbox("不知道干啥的选项", value=False)
    if joke:
        o = st.checkbox("继续吗？", value=False)
        if o:
            t = st.checkbox("真的要继续吗？", value=False)
            if t:
                _ = st.checkbox("停下！", value=False)
                if _:
                    st.error("0022：你真够闲的")
                    st.link_button("别点","https://vd3.bdstatic.com/mda-qjcrrsjkbtmeycuv/360p/h264/1728843064552037960/mda-qjcrrsjkbtmeycuv.mp4")

    # 不知道写这玩意干啥，又蠢又好玩，0038最爱的大粪
    st.caption("© 2026 疯人院1024项目组")

# ↓一坨屎，AI和0022的粪便混合物
def show():
    # ==========================
    # 单页展示所有功能（合并版）
    # ==========================
    st.title("👻 疯人院官方网站演示（单页版）")
    st.subheader("Streamlit 全功能演示 · 所有元素一页看完")
    st.markdown("---")

    # --------------------------
    # 1. 首页展示部分
    # --------------------------
    st.error('0022：这是那个瞎写的演示，让AI整成一页保留了，方便给你们看可用功能和效果')
    st.markdown("---")

    st.markdown("""
    ### 功能概览
    - 侧边栏导航
    - 多页面切换
    - 响应式排版
    - 图片、视频、文件上传
    - 表格、图表、表单
    - 多列并排布局
    """)
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("演示")
        st.write("文字")
    with col2:
        st.info("演示")
        st.write("")
    with col3:
        st.warning("演示")
        st.write("")

    st.divider()

    # --------------------------
    # 2. 排版布局
    # --------------------------
    st.title("排版与布局演示")
    st.subheader("标题层级")
    st.title("一级标题")
    st.header("二级标题")
    st.subheader("三级标题")
    st.caption("小字说明文本")

    st.subheader("多列布局（并排）")
    col_left, col_right = st.columns(2)
    with col_left:
        st.info("左侧栏目")
        st.write("巴拉巴拉")
    with col_right:
        st.success("右侧栏目")
        st.write("balabala")

    st.subheader("折叠面板")
    with st.expander("点击展开详情"):
        st.write("这里可以放一些可爱的东西")
        st.image("https://p4.itc.cn/q_70/images03/20220914/2cb80041290d446c8e1e9b33f6dfefa3.jpeg", caption="示例图")

    st.subheader("表单演示")
    with st.form("报名表单"):
        name = st.text_input("姓名")
        grade = st.selectbox("年级", ["初一", "初二", "初三"])
        submit = st.form_submit_button("提交报名")
        if submit:
            st.success("提交成功！（实则不然，只是个动画而已）")

    st.divider()

    # --------------------------
    # 3. 交互组件
    # --------------------------
    st.title("交互组件演示")

    st.subheader("输入类控件")
    st.text_input("单行输入")
    st.number_input("数字输入", 0, 100, 50)
    st.date_input("日期选择")
    st.time_input("时间选择")
    st.text_area("多行文本")

    st.subheader("选择类控件")
    st.checkbox("勾选框", value=True)
    st.radio("单选", ["选项A", "选项B", "选项C"])
    st.selectbox("下拉选择", ["选项1", "选项2", "选项3"])
    st.multiselect("多选标签", ["编程", "设计", "摄影", "写作"])

    st.subheader("按钮与链接")
    if st.button("主要按钮"):
        st.toast("操作成功！")

    st.link_button("打开视频",
                   "https://vd3.bdstatic.com/mda-qjcrrsjkbtmeycuv/360p/h264/1728843064552037960/mda-qjcrrsjkbtmeycuv.mp4")
    st.markdown(
        "超链接：[演示](https://vd3.bdstatic.com/mda-qjcrrsjkbtmeycuv/360p/h264/1728843064552037960/mda-qjcrrsjkbtmeycuv.mp4)")

    st.subheader("文件上传")
    uploaded = st.file_uploader("上传图片/文档", type=["jpg", "png", "pdf"])
    if uploaded:
        st.success("已上传：" + uploaded.name)

    st.divider()

    # --------------------------
    # 4. 数据表格
    # --------------------------
    st.title("📊 数据与表格演示")
    st.error("0022：这里用到了pandas，我不会用，拿AI写的。其他地方功能没问题")
    st.divider()

    df = pd.DataFrame({
        "姓名": ["张三", "李四", "王五", "赵六"],
        "部门": ["设计组", "技术组", "宣传组", "活动组"],
        "出勤": [95, 88, 92, 90],
        "评分": [4.5, 4.2, 4.7, 4.3]
    })

    st.subheader("基础表格")
    st.dataframe(df, use_container_width=True)

    st.subheader("可编辑表格")
    edited = st.data_editor(df, num_rows="dynamic")

    st.subheader("统计图表")
    st.bar_chart(df.set_index("姓名")["出勤"])

    st.divider()

    # --------------------------
    # 5. 图片 & 媒体
    # --------------------------
    st.title("🖼️ 图片与媒体展示")

    st.subheader("单张图片")
    st.image("https://picsum.photos/800/300", caption="示例图片")

    st.subheader("并排图片")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.image("https://picsum.photos/300/200?1")
    with col_b:
        st.image("https://picsum.photos/300/200?2")
    with col_c:
        st.image("https://picsum.photos/300/200?3")

    st.subheader("音频/视频演示")
    st.video("https://www.w3school.com.cn/i/movie.mp4")
    st.error('0022：不是只能播这么糊，是只找到这个能播。自己视频会清晰很多')

    st.subheader("成员卡片排版")
    for i in range(3):
        with st.container():
            cc1, cc2 = st.columns([1, 3])
            with cc1:
                st.image(f"https://picsum.photos/100/100?{i}")
            with cc2:
                st.markdown(f"**成员{i + 1}**")
                st.caption("职位 | 部门 | 简介")
            st.divider()
def main_page():
    st.title("院长你要的大标题")
    st.divider()
    st.image("https://p4.itc.cn/q_70/images03/20220914/2cb80041290d446c8e1e9b33f6dfefa3.jpeg", caption="还有院长你要的大照片")
    st.divider()
    st.header("还有院长你要的激情宣言")
    # st.header("二级标题")
    st.write("一块面包要五十万马克！！！$%^&*(@*&")
# 拼音命名的来了🤣
def jie_gou():
    st.header("医院（结构布局）")
    st.divider()
    st.header("世界观")
def wo_men():
    st.header("18层")
    st.divider()
    st.header("0000/0049")
    st.divider()
    st.header("17层及以下")
    st.divider()
    st.header("植物")
def yi_liao_jie_dai():
    st.write("由于0038其特殊书写带有一定模因污染，导致0022间歇性文盲。█████博士称此模因污染会使人抱怨“这字太tm草了”")
    st.divider()
    st.header("一些猎奇设施")
    st.divider()
    st.header("食堂")
def geng_duo():
    st.write("不知道放哪的文档先塞这")

if __name__ == '__main__':
    # 侧栏选择
    if choice == "streamlit可用功能展示":
        show()
    elif choice == "首页":
        print("首页")
        main_page()
    elif choice == "结构":
        print("结构")
        jie_gou()
    elif choice == "我们":
        print("我们")
        wo_men()
    elif choice == "医疗＆接待":
        print("医疗＆接待")
        yi_liao_jie_dai()
    elif choice == "更多":
        print("更多")
        geng_duo()
