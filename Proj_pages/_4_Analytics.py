import pandas as pd
import plotly.express as px
import streamlit as st

from utils.helper import page_heading, style_head


TAB_NAMES = [
    "📊 GroupBy Analysis",
    "📋 Pivot Table",
    "📈 Distribution Analysis",
]


def _show_page_title():
    st.markdown(
        """
        <h1>
            🧠 Analytics
        </h1>
        """,
        unsafe_allow_html=True
    )


def _get_column_types(df):
    categorical_columns = (
        df.select_dtypes(include=["object", "category"])
        .columns
        .tolist()
    )

    numeric_columns = (
        df.select_dtypes(include="number")
        .columns
        .tolist()
    )

    return categorical_columns, numeric_columns


def _groupby_analysis(df):
    page_heading("📊 GroupBy Analysis")

    categorical_columns, numeric_columns = _get_column_types(df)

    if not categorical_columns or not numeric_columns:
        st.warning("Required columns not found.")
        return

    category_column = st.selectbox(
        "Select Category Column",
        categorical_columns,
    )

    numeric_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns,
    )

    operation = st.selectbox(
        "Select Operation",
        [
            "Sum",
            "Mean",
            "Max",
            "Min",
            "Count",
        ],
    )

    grouped_data = df.groupby(category_column)[numeric_column]

    operation_map = {
        "Sum": grouped_data.sum,
        "Mean": grouped_data.mean,
        "Max": grouped_data.max,
        "Min": grouped_data.min,
        "Count": grouped_data.count,
    }

    result = operation_map[operation]()

    st.dataframe(result, use_container_width=True)

def _pivot_table(df):
    page_heading("📋 Pivot Table")

    categorical_columns, numeric_columns = _get_column_types(df)

    if not categorical_columns or not numeric_columns:
        st.warning("Required columns not found.")
        return

    category_column = st.selectbox(
        "Select Category",
        categorical_columns,
        key="pivot_cat",
    )

    numeric_column = st.selectbox(
        "Select Numeric",
        numeric_columns,
        key="pivot_num",
    )

    pivot_table = pd.pivot_table(
        df,
        values=numeric_column,
        index=category_column,
        aggfunc="sum",
    )

    st.dataframe(
        pivot_table,
        use_container_width=True,
    )


def _box_plot(df, numeric_columns):
    style_head("📊 Box Chart")

    selected_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns,
        key="box",
    )

    figure = px.box(
        df,
        y=selected_column,
        points="outliers",
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
    )


def _violin_plot(df, categorical_columns, numeric_columns):
    style_head("🧮 Violin Chart")

    if not categorical_columns:
        st.warning("No categorical columns found.")
        return

    selected_column = st.selectbox(
        "Numeric",
        numeric_columns,
        key="vio_num",
    )

    figure = px.violin(
        df,
        y=selected_column,
    )

    figure.update_traces(
        meanline_visible=True,
    )

    st.plotly_chart(
        figure,
        use_container_width=True,
    )


def _distribution_analysis(df):
    page_heading("📈 Distribution Analysis")

    _, numeric_columns = _get_column_types(df)
    categorical_columns, _ = _get_column_types(df)

    distribution_tabs = st.tabs(
        [
            "Box Plot",
            "Violin Plot",
        ]
    )

    with distribution_tabs[0]:
        _box_plot(
            df,
            numeric_columns,
        )

    with distribution_tabs[1]:
        _violin_plot(
            df,
            categorical_columns,
            numeric_columns,
        )


def analytics(df):
    _show_page_title()

    tabs = st.tabs(TAB_NAMES)

    with tabs[0]:
        _groupby_analysis(df)

    with tabs[1]:
        _pivot_table(df)

    with tabs[2]:
        _distribution_analysis(df)