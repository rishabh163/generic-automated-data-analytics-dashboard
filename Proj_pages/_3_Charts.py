import plotly.express as px
import streamlit as st

from utils.helper import page_heading


TAB_NAMES = [
    "📊 Bar",
    "〰️ Line",
    "🔵 Scatter",
    "📊 Histogram",
    "🥧 Pie",
    "📉 Area",
    "🔥 Heatmap",
    "🌐 3D Scatter",
]


def _show_page_title():
    st.markdown(
        """
        <h1 style='text-align:center;'>
            📈 Charts
        </h1>
        """,
        unsafe_allow_html=True
    )


def _common_settings(df):
    columns = df.columns.tolist()

    numeric_columns = (
        df.select_dtypes(include="number")
        .columns
        .tolist()
    )

    category_columns = (
        df.select_dtypes(include=["object", "category"])
        .columns
        .tolist()
    )

    col1, col2 = st.columns(2)

    with col1:
        selected_color = st.selectbox(
            "🎨 Color (Optional)",
            ["None"] + columns,
        )

    with col2:
        chart_height = st.slider(
            "📏 Chart Height",
            min_value=400,
            max_value=900,
            value=500,
        )

    if selected_color == "None":
        selected_color = None

    return (
        columns,
        numeric_columns,
        category_columns,
        selected_color,
        chart_height,
    )


def _display_chart(fig, height):
    fig.update_layout(height=height)

    with st.container(border=True):
        st.plotly_chart(
            fig,
            use_container_width=True,
        )


def _bar_chart(df, columns, numeric_columns, color, height):
    page_heading("📊 Bar Chart")

    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox(
            "X-axis",
            columns,
            key="bar_x",
        )

    with col2:
        y_axis = st.selectbox(
            "Y-axis",
            numeric_columns,
            key="bar_y",
        )

    fig = px.bar(
        df,
        x=x_axis,
        y=y_axis,
        color=color,
    )

    _display_chart(fig, height)

    return fig


def _line_chart(df, columns, numeric_columns, color, height):
    page_heading("〰️ Line Chart")

    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox(
            "X-axis",
            columns,
            key="line_x",
        )

    with col2:
        y_axis = st.selectbox(
            "Y-axis",
            numeric_columns,
            key="line_y",
        )

    fig = px.line(
        df,
        x=x_axis,
        y=y_axis,
        color=color,
    )

    _display_chart(fig, height)

    return fig


def _scatter_chart(df, columns, numeric_columns, color, height):
    page_heading("🔵 Scatter Chart")

    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox(
            "X-axis",
            columns,
            key="scatter_x",
        )

    with col2:
        y_axis = st.selectbox(
            "Y-axis",
            numeric_columns,
            key="scatter_y",
        )

    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color=color,
    )

    _display_chart(fig, height)

    return fig


def _histogram(df, numeric_columns, color, height):
    page_heading("📊 Histogram Chart")

    histogram_column = st.selectbox(
        "Numeric Column",
        numeric_columns,
        key="hist",
    )

    fig = px.histogram(
        df,
        x=histogram_column,
        color=color,
    )

    _display_chart(fig, height)

    return fig


def _pie_chart(df, category_columns, numeric_columns, height):
    page_heading("🥧 Pie Chart")

    if not category_columns:
        st.warning("No categorical columns found.")
        return None

    col1, col2 = st.columns(2)

    with col1:
        names = st.selectbox(
            "Category",
            category_columns,
            key="pie_name",
        )

    with col2:
        values = st.selectbox(
            "Values",
            numeric_columns,
            key="pie_value",
        )

    fig = px.pie(
        df,
        names=names,
        values=values,
    )

    _display_chart(fig, height)

    return fig


def _area_chart(df, columns, numeric_columns, color, height):
    page_heading("📉 Area Chart")

    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox(
            "X-axis",
            columns,
            key="area_x",
        )

    with col2:
        y_axis = st.selectbox(
            "Y-axis",
            numeric_columns,
            key="area_y",
        )

    fig = px.area(
        df,
        x=x_axis,
        y=y_axis,
        color=color,
    )

    _display_chart(fig, height)

    return fig


def _heatmap(df, numeric_columns, height):
    page_heading("🔥 Heatmap Chart")

    if len(numeric_columns) < 2:
        st.warning("At least 2 numeric columns are required.")
        return None

    correlation = df[numeric_columns].corr()

    fig = px.imshow(
        correlation,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
    )

    _display_chart(fig, height)

    return fig


def _scatter_3d(df, numeric_columns, color, height):
    page_heading("🌐 3D Scatter Chart")

    if len(numeric_columns) < 3:
        st.warning("At least 3 numeric columns are required.")
        return None

    col1, col2, col3 = st.columns(3)

    with col1:
        x_axis = st.selectbox(
            "X-axis",
            numeric_columns,
            key="x3",
        )

    with col2:
        y_axis = st.selectbox(
            "Y-axis",
            numeric_columns,
            index=1,
            key="y3",
        )

    with col3:
        z_axis = st.selectbox(
            "Z-axis",
            numeric_columns,
            index=2,
            key="z3",
        )

    fig = px.scatter_3d(
        df,
        x=x_axis,
        y=y_axis,
        z=z_axis,
        color=color,
    )

    _display_chart(fig, height)

    return fig


def charts(df):
    _show_page_title()

    st.divider()

    (
        columns,
        numeric_columns,
        category_columns,
        color,
        height,
    ) = _common_settings(df)

    tabs = st.tabs(TAB_NAMES)

    current_chart = None

    with tabs[0]:
        current_chart = _bar_chart(
            df,
            columns,
            numeric_columns,
            color,
            height,
        )

    with tabs[1]:
        current_chart = _line_chart(
            df,
            columns,
            numeric_columns,
            color,
            height,
        )

    with tabs[2]:
        current_chart = _scatter_chart(
            df,
            columns,
            numeric_columns,
            color,
            height,
        )

    with tabs[3]:
        current_chart = _histogram(
            df,
            numeric_columns,
            color,
            height,
        )

    with tabs[4]:
        current_chart = _pie_chart(
            df,
            category_columns,
            numeric_columns,
            height,
        )

    with tabs[5]:
        current_chart = _area_chart(
            df,
            columns,
            numeric_columns,
            color,
            height,
        )

    with tabs[6]:
        current_chart = _heatmap(
            df,
            numeric_columns,
            height,
        )

    with tabs[7]:
        current_chart = _scatter_3d(
            df,
            numeric_columns,
            color,
            height,
        )

    st.divider()

    if current_chart is not None:
        st.download_button(
            label="📥 Download Current Chart (HTML)",
            data=current_chart.to_html(),
            file_name="chart.html",
            mime="text/html",
            use_container_width=True,
        )