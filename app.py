import streamlit as st
from streamlit_option_menu import option_menu

from Proj_pages._1_Data_Cleaning import data_clean
from Proj_pages._2_Filters import filters
from Proj_pages._3_Charts import charts
from Proj_pages._4_Analytics import analytics
from Proj_pages._5_Reports import reports

from utils.css import load_css
from utils.file_handler import load_uploaded_file
from utils.html_templates import get_banner
from utils.image_loader import load_project_images
from utils.session_manager import (
    dataset_exists,
    get_dataset,
    get_file_name,
    save_dataset,
)

# ===========================
# Page Configuration
# ===========================

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

# ===========================
# Load Project Resources
# ===========================

logo_base64, hero_base64 = load_project_images()

load_css()

banner = get_banner(hero_base64)

# ===========================
# Sidebar
# ===========================

with st.sidebar:
    st.markdown(
        f"""
        <div class='sidebar-logo'>
            <img src='data:image/png;base64,{logo_base64}'>
            <div>
                <h3>Analytics</h3>
                <p>Dashboard</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='sidebar-label'>PAGES</p>",
        unsafe_allow_html=True
    )

    menu = option_menu(
        menu_title=None,
        options=[
            "Home",
            "Data Cleaning",
            "Filters",
            "Charts",
            "Analytics",
            "Report",
        ],
        icons=[
            "house-fill",
            "brush-fill",
            "funnel-fill",
            "bar-chart-fill",
            "graph-up-arrow",
            "file-earmark-text-fill",
        ],
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "transparent",
            },
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "4px 0",
                "border-radius": "10px",
                "padding": "10px 14px",
                "color": "#333",
            },
            "nav-link-selected": {
                "background": (
                    "linear-gradient("
                    "90deg,"
                    "#182a96 0%,"
                    "#3729b6 40%,"
                    "#6c31d7 75%,"
                    "#a33cff 100%)"
                ),
                "color": "white",
                "font-weight": "600",
            },
        },
    )

    st.markdown(
        """
        <div class='about-box'>
            <b>ℹ️ About</b>
            <p>
                Upload your dataset and generate automated
                insights with visual analytics.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
# ===========================
# Home Page
# ===========================

if menu == "Home":
    # Banner
    st.markdown(banner, unsafe_allow_html=True)
    
    # ===========================
    # File Upload Section
    # ===========================

    with st.container(border=True):
        st.markdown(
            "<div class='section-header'>"
            "<div class='icon-circle'><img src='https://cdn-icons-png.flaticon.com/512/126/126477.png'></div>"
            "<div>"
            "<p class='section-title'>Choose the file</p>"
            "<p class='section-sub'>Upload your CSV or Excel file to get started</p>"
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )

        uploaded_file = st.file_uploader(
            "Choose the file",
            type=["csv", "xlsx", "json"],
            label_visibility="collapsed",
        )

        if uploaded_file is not None:

            dataframe, file_name = load_uploaded_file(uploaded_file)

            if dataframe is not None:
                save_dataset(dataframe, file_name)

        if dataset_exists():

            st.success("✅ File uploaded successfully!")

            st.markdown(
                f"""
                <div class='file-name-line'>
                    📄 <b>Uploaded File Name :</b>
                    <a href='#'>{get_file_name()}</a>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ===========================
    # Dataset Information
    # ===========================

    with st.container(border=True):
        st.markdown(
            "<div class='section-header'>"
            "<div class='icon-circle'><img src='https://cdn-icons-png.flaticon.com/512/2906/2906274.png'></div>"
            "<div>"
            "<p class='section-title'>Dataset Information</p>"
            "<p class='section-sub'>Preview of your uploaded dataset</p>"
            "</div>"
            "</div>",
            unsafe_allow_html=True
        )

        if dataset_exists():
            dataframe = get_dataset()
            st.dataframe(
                dataframe,
                use_container_width=True,
            )
            column1, column2, column3 = st.columns(3)
            with column1:
                st.metric(
                    "📄 Total Rows",
                    dataframe.shape[0],
                )

            with column2:
                st.metric(
                    "📊 Total Columns",
                    dataframe.shape[1],
                )

            with column3:
                dataset_size = (
                    dataframe.memory_usage(deep=True).sum()
                    / (1024 * 1024)
                )

                st.metric(
                    "💾 Total Size (MB)",
                    f"{dataset_size:.2f} MB",
                )

        else:

            st.info(
                "📂 No dataset uploaded yet. Please upload a file above."
            )

            column1, column2, column3 = st.columns(3)

            with column1:
                st.metric("📄 Total Rows", "—")

            with column2:
                st.metric("📊 Total Columns", "—")

            with column3:
                st.metric("💾 Total Size (MB)", "—")
# ===========================
# Page Navigation
# ===========================

elif menu == "Data Cleaning":

    if not dataset_exists():
        st.warning("⚠️ Please upload a file first.")
        st.stop()

    data_clean(get_dataset())


elif menu == "Filters":

    if not dataset_exists():
        st.warning("⚠️ Please upload a file first.")
        st.stop()

    filters(get_dataset())


elif menu == "Charts":

    if not dataset_exists():
        st.warning("⚠️ Please upload a file first.")
        st.stop()

    charts(get_dataset())


elif menu == "Analytics":

    if not dataset_exists():
        st.warning("⚠️ Please upload a file first.")
        st.stop()

    analytics(get_dataset())


elif menu == "Report":

    if not dataset_exists():
        st.warning("⚠️ Please upload a file first.")
        st.stop()

    reports(get_dataset())

