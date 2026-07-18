import os
import streamlit as st

# --------------------------
# 页面设置
# --------------------------
st.set_page_config(
    page_title="Asylum12 Website",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 读取网址参数
page = st.query_params.get("page", "vincent_file")

# 侧边栏
with st.sidebar:
    st.title("Navigation")

    menu_dict = {
        "首页": "home",
        "结构": "structure",
        "我们": "us",
        "医疗＆接待": "medical",
        "更多": "more",
        "streamlit可用功能展示": "demo",
        "0022杂物柜": "vincent_file"
    }

    try:
        idx = list(menu_dict.values()).index(page)
    except ValueError:
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
    st.selectbox("演示", ["a", "b"])
    joke = st.checkbox("不知道干啥的选项", value=False)
    if joke:
        go_on = st.checkbox("继续吗？", value=False)
        if go_on:
            insist = st.checkbox("真的要继续吗？", value=False)
            if insist:
                stop = st.checkbox("停下！", value=False)
                if stop:
                    st.error("0022：你真够闲的")
                    video_link = "https://vd3.bdstatic.com/mda-qjcrrsjkbtmeycuv/360p/h264/1728843064552037960/mda-qjcrrsjkbtmeycuv.mp4"
                    st.link_button("别点", video_link)

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
    st.markdown("## Welcome to the 12th Asylum!")
    st.markdown(
        "We are delighted to see you here,dear patient,as we have been waiting for you "
        "for a long time.You may relax,for this is a safe haven for our kind.There is no "
        "need to worry about your little ‘condition’ anymore.Our medical team has specially "
        "tailored an exclusive rehabilitation program just for you. Please be assured that "
        "we will put our best efforts into improving your physical and mental health."
        "No forms or payment is required beforehand —we have taken care of those "
        "unimportant issues."
    )
    st.text("")
    st.markdown(
        "The only thing asked of you,my dear,is to follow a few simple rules.Please "
        "remember that this is a private institution,using the most cutting edge treatments."
        "Some of these methods are special to this place, so kindly do not mention them to "
        "anyone outside the 12th asylum.Don’t be afraid.None of the said treatments are "
        "dangerous,as long as you take them without struggle.We have some of the best "
        "therapists and psychologists working on cases such as yourself.Do not disobey us,"
        "or we will be forced to readjust your scheduled treatments.Most importantly,the "
        "main building has and only has 17 floors.If you see any patients from the 18th "
        "floor,report to a doctor immediately.All of them wear badges inscribed with serial "
        "numbers starting with 00.Never go to any floors above your assigned level.The "
        "patients living above you are rather more unstable.Socializing with them may "
        "worsen your own condition."
    )
    st.text("")
    st.markdown(
        "Dear patient,one final notice.Do not attempt to leave the 12th asylum.You are "
        "much safer with us than outside with those who do not see,who cannot dream to be "
        "who you are—who we are.Of course you won’t mind staying with us forever,right? "
        "We are the only ones who will accept you as you are. We strive to help you recover "
        "what you have lost,and find who you were always meant to be.Enjoy your permanent "
        "stay at the 12th asylum,my dear.We wish you a safe and pleasant recovery."
    )

    st.divider()
    st.title("院长你要的大标题")
    st.divider()
    st.image("https://p4.itc.cn/q_70/images03/20220914/2cb80041290d446c8e1e9b33f6dfefa3.jpeg", caption="还有院长你要的大照片")
    st.divider()
    st.header("还有院长你要的激情宣言")
    st.write("一块面包要五十万马克！！！$%^&*(@*&")


def structure():
    st.header("医院（结构布局）")
    st.divider()
    st.header("世界观")


def us():
    st.header("18层")
    st.divider()
    st.header("0000/0049")
    st.divider()
    st.header("17层及以下")
    st.divider()
    st.header("植物")

# todo The routing call does not pass parameters to this function, so the "pdf_name" parameter is removed to be improved.
# def medical_reception(pdf_name):

def medical_reception():
    st.write("由于0038其特殊书写带有一定模因污染，导致0022间歇性文盲。█████博士称此模因污染会使人抱怨“这字太tm草了”")
    st.divider()
    st.header("一些猎奇设施")
    st.divider()
    st.header("食堂")


def more():
    st.write("不知道放哪的文档先塞这")


def download_pdf(pdf_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, pdf_name)

    if os.path.exists(file_path):
        pdf_bytes = load_pdf_bytes(file_path)
        # 给用户一个下载按钮，点击就会下载PDF，本地直接打开
        st.download_button(
            label="下载PDF查看",
            data=pdf_bytes,
            file_name=pdf_name,
            mime="application/pdf"
        )
    else:
        st.error("❌ 文件不存在，请检查路径")


@st.cache_data
def load_pdf_bytes(file_path):
    with open(file_path, "rb") as f:
        return f.read()


def vincent_file():
    st.info("语文：鼓浪屿旅行手账")
    download_pdf("鼓浪屿旅行手账.pdf")
    st.divider()
    st.info("历史：历史博物馆——经典文物介绍：跪射俑")
    download_pdf("历史博物馆——经典文物介绍：跪射俑.pdf")
    st.divider()
    st.info("地理：台湾是我国领土不可分割的一部分")
    download_pdf("台湾是我国领土不可分割的一部分.pdf")
    st.info("道法：社区环保行动探究")
    download_pdf("社区环保行动探究.pdf")


# --------------------------
# 页面路由
# --------------------------
if __name__ == '__main__':
    if page == "demo":
        show()
    elif page == "home":
        main_page()
    elif page == "structure":
        structure()
    elif page == "us":
        us()
    elif page == "medical":
        medical_reception()
    elif page == "more":
        more()
    elif page == "vincent_file":
        vincent_file()
