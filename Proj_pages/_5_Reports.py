import io

import pandas as pd
import streamlit as st

from utils.helper import page_heading


TAB_NAMES = [
    "📋 Dataset Summary",
    "📥 Download Dataset",
    "📑 Generate Report",
    "ℹ️ Project Information",
]


def _show_page_title():
    st.markdown(
        """
        <h1 style='text-align:center;'>
            📄 Reports
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.divider()


def _dataset_summary(df):
    page_heading("📋 Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📑 Total Rows", df.shape[0])
        st.metric("❌ Missing Values", df.isnull().sum().sum())

    with col2:
        st.metric("📊 Total Columns", df.shape[1])
        st.metric("🗂️ Duplicate Rows", df.duplicated().sum())

    st.divider()

    st.subheader("📌 Column Information")

    info_df = pd.DataFrame(
        {
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values,
        }
    )

    st.dataframe(
        info_df,
        hide_index=True,
        use_container_width=True,
    )


def _download_csv(df):
    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name="Cleaned_Dataset.csv",
        mime="text/csv",
        use_container_width=True,
    )


def _download_excel(df):
    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl",
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Dataset",
        )

    st.download_button(
        label="⬇️ Download Excel",
        data=excel_buffer.getvalue(),
        file_name="Cleaned_Dataset.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True,
    )


def _download_json(df):
    json_data = df.to_json(
        orient="records",
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download JSON",
        data=json_data,
        file_name="Cleaned_Dataset.json",
        mime="application/json",
        use_container_width=True,
    )


def _download_dataset(df):
    page_heading("📥 Download Dataset")

    download_tabs = st.tabs(
        [
            "📄 CSV",
            "📗 Excel",
            "📜 JSON",
        ]
    )

    with download_tabs[0]:
        _download_csv(df)

    with download_tabs[1]:
        _download_excel(df)

    with download_tabs[2]:
        _download_json(df)


def _generate_report(df):
    page_heading("📑 Dataset Report")

    report = f"""
==============================
      DATASET REPORT
==============================

Total Rows              : {df.shape[0]}
Total Columns           : {df.shape[1]}

Missing Values          : {df.isnull().sum().sum()}
Duplicate Rows          : {df.duplicated().sum()}

Numeric Columns         : {len(df.select_dtypes(include='number').columns)}
Categorical Columns     : {len(df.select_dtypes(include=['object', 'category']).columns)}

Dataset Memory Usage    : {round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2)} MB
"""

    st.text(report)

    st.download_button(
        label="⬇️ Download Report",
        data=report,
        file_name="Dataset_Report.txt",
        mime="text/plain",
        use_container_width=True,
    )


def _project_information():
    page_heading("ℹ️ Project Information")

    st.markdown(
        """
<div style="
    background: linear-gradient(180deg, #ffffff, #fafbff);
    border: 1px solid #E7EAF3;
    border-top: 4px solid #5B5CEB;
    border-bottom: 2px solid #5B5CEB;
    border-radius: 18px;
    padding: 24px 28px;
    box-shadow: 0 8px 22px rgba(0,0,0,.08);
    font-size: 15px;
">

### 📊 **Generic Automated Data Analytics Dashboard**

#### 🚀 Features
- 📂 Upload CSV / Excel Dataset
- 🧹 Data Cleaning
- 🔍 Data Filtering
- 📈 Interactive Charts
- 🧠 Analytics
- 📄 Report Generation
- 📥 Export Dataset

---

#### 🛠️ Technologies Used
- Python
- Pandas
- Plotly
- Streamlit

---

#### 🎯 Objective
- Automate the complete data analysis workflow
- Enable users to upload any dataset
- Clean and explore data with ease
- Visualize insights through interactive charts
- Analyze patterns for deeper understanding
- Download processed data and reports for ML / Business Analytics

---

#### 👤 Developer
**Rishabh Gaur**

🔗 GitHub: https://github.com/rishabh163

---

#### 📌 Version
v1.0.0

</div>
""",
        unsafe_allow_html=True
    )


def reports(df):
    _show_page_title()

    tabs = st.tabs(TAB_NAMES)

    with tabs[0]:
        _dataset_summary(df)

    with tabs[1]:
        _download_dataset(df)

    with tabs[2]:
        _generate_report(df)

    with tabs[3]:
        _project_information()