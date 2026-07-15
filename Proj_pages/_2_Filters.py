import io

import pandas as pd
import streamlit as st

from utils.helper import page_heading


TAB_NAMES = [
    "📄 Data Selection",
    "📋 Data Types",
    "📥 Data Export",
]


def _show_page_title():
    st.markdown(
        """
        <h1 style='text-align:center;'>
            🔍 Filters
        </h1>
        """,
        unsafe_allow_html=True
    )


def _data_selection_tab(df):
    page_heading("📄 Data Selection")

    row_count = st.slider(
        "Select Number of Rows",
        min_value=1,
        max_value=df.shape[0],
        value=min(10, df.shape[0]),
    )

    selection_type = st.radio(
        "Select Data",
        ["Top", "Bottom", "Random"],
        horizontal=True,
    )

    if selection_type == "Top":
        preview_data = df.head(row_count)

    elif selection_type == "Bottom":
        preview_data = df.tail(row_count)

    else:
        preview_data = df.sample(n=row_count)

    st.dataframe(
        preview_data,
        use_container_width=True,
    )


def _data_types_tab(df):
    page_heading("📋 Data Types")

    info_df = pd.DataFrame(
        {
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Non-Null": df.count().values,
            "Null Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values,
        }
    )

    selected_column = st.selectbox(
        "🔎 Search Column",
        df.columns,
    )

    filtered_info = info_df[
        info_df["Column Name"].str.contains(
            selected_column,
            case=False,
        )
    ]

    st.dataframe(
        filtered_info,
        hide_index=True,
        use_container_width=True,
    )


def _download_csv(data):
    csv_data = data.to_csv(
        index=False,
    ).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv_data,
        file_name="filtered_data.csv",
        mime="text/csv",
        use_container_width=True,
    )


def _download_json(data):
    json_data = data.to_json(
        orient="records",
        indent=4,
    )

    st.download_button(
        label="📥 Download JSON",
        data=json_data,
        file_name="filtered_data.json",
        mime="application/json",
        use_container_width=True,
    )


def _download_excel(data):
    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl",
    ) as writer:

        data.to_excel(
            writer,
            index=False,
            sheet_name="Sheet1",
        )

    st.download_button(
        label="📥 Download Excel",
        data=excel_buffer.getvalue(),
        file_name="filtered_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True,
    )


def _data_export_tab(df):
    page_heading("📥 Export Selected Columns")

    selected_columns = st.multiselect(
        "Select Columns",
        df.columns,
    )

    if not selected_columns:
        st.info("Select one or more columns.")
        return

    filtered_data = df[selected_columns]

    st.dataframe(
        filtered_data,
        use_container_width=True,
    )

    download_tabs = st.tabs(
        [
            "📄 CSV",
            "📑 JSON",
            "📗 Excel",
        ]
    )

    with download_tabs[0]:
        _download_csv(filtered_data)

    with download_tabs[1]:
        _download_json(filtered_data)

    with download_tabs[2]:
        _download_excel(filtered_data)


def filters(df):
    _show_page_title()

    tabs = st.tabs(TAB_NAMES)

    with tabs[0]:
        _data_selection_tab(df)

    with tabs[1]:
        _data_types_tab(df)

    with tabs[2]:
        _data_export_tab(df)