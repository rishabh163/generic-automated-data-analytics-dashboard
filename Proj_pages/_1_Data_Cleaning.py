import pandas as pd
import streamlit as st
from io import BytesIO

from utils.helper import page_heading
from utils.session_manager import save_dataset


TAB_NAMES = [
    "🗂️ Dataset Overview",
    "❓ Missing Values",
    "📑 Duplicate Rows",
    "🔢 Numeric Columns",
    "⬇️ Download Cleaned Dataset",
]


def _show_page_title():
    st.markdown(
        """
        <h1 style='text-align:center;
        font-family:"Times New Roman", Times, serif;
        color:#1a1a2e;'>
            ✨ Data Cleaning
        </h1>
        """,
        unsafe_allow_html=True
    )


def _show_dataset_overview(df):
    page_heading("🗂️ Dataset Overview")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📑 Total Rows", df.shape[0])

    with col2:
        st.metric("📊 Total Columns", df.shape[1])

    col3, col4 = st.columns(2)

    with col3:
        st.metric("❌ Missing Values", df.isnull().sum().sum())

    with col4:
        st.metric("🗂️ Duplicate Rows", df.duplicated().sum())

    st.divider()

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe(include="all").T.round(2),
        use_container_width=True,
    )


def _handle_missing_values(df):
    page_heading("❓ Missing Values")
    st.divider()

    total_missing = df.isnull().sum().sum()

    st.metric("Total Missing Values", total_missing)

    missing_columns = [
        column
        for column in df.columns
        if df[column].isnull().sum() > 0
    ]

    if not missing_columns:
        st.success("🎉 No missing values found in the dataset!")
        return

    selected_column = st.selectbox(
        "Select Column with Missing Values",
        missing_columns,
    )

    before = df[selected_column].isnull().sum()

    st.metric(
        f"Missing Values in '{selected_column}'",
        before,
    )

    if df[selected_column].isnull().all():
        st.info(
            "⚠️ This column contains only missing values. "
            "Forward Fill and Backward Fill may not work."
        )

    st.subheader("Select Cleaning Method")

    cleaning_method = st.radio(
        "Choose Method",
        [
            "Remove Column",
            "Forward Fill",
            "Backward Fill",
        ],
        horizontal=True,
    )

    if st.button(
        "Apply Cleaning",
        use_container_width=True,
    ):

        if cleaning_method == "Remove Column":

            df.drop(columns=[selected_column], inplace=True)

            save_dataset(df, st.session_state.get("file_name"))

            st.success(
                f"✅ Column '{selected_column}' removed successfully."
            )

            return

        if cleaning_method == "Forward Fill":
            df[selected_column] = df[selected_column].ffill()

        if cleaning_method == "Backward Fill":
            df[selected_column] = df[selected_column].bfill()

        after = df[selected_column].isnull().sum()

        save_dataset(df, st.session_state.get("file_name"))

        if before == after:
            st.warning("⚠️ No missing values could be filled.")
        else:
            st.success(
                f"✅ {before-after} missing value(s) filled successfully."
            )


def _handle_duplicate_rows(df):
    page_heading("📑 Duplicate Rows")
    st.divider()

    duplicate_count = df.duplicated().sum()

    st.metric(
        "Total Duplicate Rows",
        duplicate_count,
    )

    if duplicate_count == 0:
        st.success("🎉 No duplicate rows found in the dataset!")
        return

    st.subheader("Duplicate Rows Preview")

    st.dataframe(
        df[df.duplicated()],
        use_container_width=True,
    )

    if st.button(
        "Remove Duplicate Rows",
        use_container_width=True,
    ):

        rows_before = df.shape[0]

        df.drop_duplicates(inplace=True)

        rows_after = df.shape[0]

        save_dataset(df, st.session_state.get("file_name"))

        st.success(
            f"✅ {rows_before-rows_after} duplicate row(s) removed successfully."
        )


def _show_numeric_columns(df):
    page_heading("🔢 Numeric Columns")
    st.divider()

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) == 0:
        st.warning("⚠️ No numeric columns found in the dataset.")
        return

    selected_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Minimum",
            df[selected_column].min(),
        )

    with col2:
        st.metric(
            "Maximum",
            df[selected_column].max(),
        )

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "Mean",
            round(df[selected_column].mean(), 2),
        )

    with col4:
        st.metric(
            "Std Dev",
            round(df[selected_column].std(), 2),
        )

    st.divider()

    st.subheader("Column Preview")

    st.dataframe(
        df[[selected_column]],
        use_container_width=True,
    )


def _download_section(df):
    page_heading("⬇️ Download Cleaned Dataset")
    st.divider()

    st.metric(
        "Ready to Download",
        f"{df.shape[0]} rows × {df.shape[1]} columns",
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        csv_data = df.to_csv(
            index=False,
        ).encode("utf-8")

        st.download_button(
            label="📄 Download CSV",
            data=csv_data,
            file_name="cleaned_dataset.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with col2:

        excel_buffer = BytesIO()

        with pd.ExcelWriter(
            excel_buffer,
            engine="openpyxl",
        ) as writer:

            df.to_excel(
                writer,
                index=False,
                sheet_name="Cleaned Data",
            )

        st.download_button(
            label="📗 Download Excel",
            data=excel_buffer.getvalue(),
            file_name="cleaned_dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

    with col3:

        json_data = df.to_json(
            orient="records",
            indent=4,
        )

        st.download_button(
            label="📑 Download JSON",
            data=json_data,
            file_name="cleaned_dataset.json",
            mime="application/json",
            use_container_width=True,
        )


def data_clean(df):
    _show_page_title()

    tabs = st.tabs(TAB_NAMES)

    with tabs[0]:
        _show_dataset_overview(df)

    with tabs[1]:
        _handle_missing_values(df)

    with tabs[2]:
        _handle_duplicate_rows(df)

    with tabs[3]:
        _show_numeric_columns(df)

    with tabs[4]:
        _download_section(df)