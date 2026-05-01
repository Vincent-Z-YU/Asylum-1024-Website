import streamlit as st
import base64

# --------------------------
# 页面设置
# --------------------------
st.set_page_config(
    page_title="Asylum12 Website",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 读取网址参数
query = st.query_params
page = query.get("page", "home")

# 侧边栏
with st.sidebar:
    st.title("Navigation")

    menu_dict = {
        "首页": "home",
        "结构": "structure",
        "我们": "us",
        "医疗＆接待": "medical",
        "更多": "more",
        "streamlit可用功能展示": "demo"
    }

    try:
        idx = list(menu_dict.values()).index(page)
    except:
        idx = 0

    choice = st.radio(
        "menu",
        list(menu_dict.keys()),
        index=idx,
        label_visibility="collapsed"
    )

    current_page = menu_dict[choice]
    if current_page != page:
        st.query_params["page"] = current_page
        st.rerun()

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

    st.caption("© 2026 疯人院1024项目组")

# --------------------------
# 页面函数
# --------------------------
def show():
    st.title("👻 疯人院官方网站演示（单页版）")
    st.subheader("Streamlit 全功能演示 · 所有元素一页看完")
    st.markdown("---")
    st.error('0022：这是那个瞎写的演示，让AI整成一页保留了，方便给你们看可用功能和效果')
    st.markdown("""
    ### 功能概览
    - 侧边栏导航
    - 多页面切换
    - 响应式排版
    - 图片、视频、文件上传
    - 表格、图表、表单
    - 多列并排布局
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("演示")
        st.write("文字")

def main_page():
    st.title("Asylum12 Website(Under construction)")
    st.text("这是 Asylum12 的官方网页，但是还在建设")
    st.text("这里的内容目前不属于 Asylum12 的官方内容")
    st.text("这个网站被0022塞了很多奇怪的东西，忽视即可")
    st.text("注：这个网站在建设期间常被0022用作一些个人文件的临时存放处:P")
    st.divider()
    st.title("院长你要的大标题")
    st.divider()
    st.image("https://p4.itc.cn/q_70/images03/20220914/2cb80041290d446c8e1e9b33f6dfefa3.jpeg", caption="还有院长你要的大照片")
    st.divider()
    st.header("还有院长你要的激情宣言")
    st.write("一块面包要五十万马克！！！$%^&*(@*&")

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

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'''
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" 
        height="900px" 
        type="application/pdf">
    </iframe>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)

def V():
    st.info("鼓浪屿旅行手账")
    show_pdf("鼓浪屿旅行手账.pdf")
    st.divider()
    st.info("历史博物馆——经典文物介绍：跪射俑")
    show_pdf("历史博物馆——经典文物介绍：跪射俑")



# --------------------------
# 页面路由
# --------------------------
if __name__ == '__main__':
    if page == "demo":
        show()
    elif page == "home":
        main_page()
    elif page == "structure":
        jie_gou()
    elif page == "us":
        wo_men()
    elif page == "medical":
        yi_liao_jie_dai()
    elif page == "more":
        geng_duo()
