import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Asylum12 Website",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 页面函数不动
def show():
    st.title("👻 疯人院官方网站演示")
def main_page():
    st.title("Asylum12 Website(Under construction)")
def jie_gou():
    st.header("医院（结构布局）")
def wo_men():
    st.header("18层")
def yi_liao_jie_dai():
    st.write("医疗接待内容")
def geng_duo():
    st.write("更多内容")

# 关键：全部塞进 main_ui，和你TAG完全一致
def main_ui():
    query = st.query_params
    page = query.get("page", "home")

    with st.sidebar:
        st.header("Navigation")
        menu = {
            "首页":"home",
            "结构":"structure",
            "我们":"us",
            "医疗＆接待":"medical",
            "更多":"more",
            "streamlit可用功能展示":"demo"
        }

        select_label = st.radio(
            "",
            list(menu.keys()),
            index=list(menu.values()).index(page),
            label_visibility="collapsed"
        )

        select_page = menu[select_label]
        if select_page != page:
            st.query_params["page"] = select_page
            st.rerun()

        # 你侧边栏其他杂物保留
        st.divider()
        st.error("0022：这里的演示我就暂时先保留了")
        st.caption("© 2026 疯人院1024项目组")

    # 页面分发
    if select_page == "home":
        main_page()
    elif select_page == "structure":
        jie_gou()
    elif select_page == "us":
        wo_men()
    elif select_page == "medical":
        yi_liao_jie_dai()
    elif select_page == "more":
        geng_duo()
    elif select_page == "demo":
        show()

if __name__ == "__main__":
    main_ui()
