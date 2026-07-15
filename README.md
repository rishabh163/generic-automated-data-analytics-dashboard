# Generic Automated Data Analytics Dashboard

A Streamlit-based data analytics dashboard that allows users to upload a dataset, clean data, apply filters, generate interactive charts, perform analytics, and create reports.

---

## Project Overview

This project is designed to simplify data analysis by providing an easy-to-use dashboard where users can upload CSV, Excel, or JSON files and perform multiple analytics operations without writing code.

---

## Features

- Upload CSV, Excel, and JSON files
- Data Cleaning
- Data Filtering
- Interactive Charts
- Automated Analytics
- Report Generation

---

## Project Structure

```
PY INTERNSHIP PROJECT/
│
├── assets/
│   ├── logo.png
│   └── home_logo.png
│
├── Proj_pages/
│   ├── _1_Data_Cleaning.py
│   ├── _2_Filters.py
│   ├── _3_Chart.py
│   ├── _4_Analytics.py
│   └── _5_Report.py
│
├── utils/
│   ├── helper.py
│   ├── image_loader.py
│   ├── css.py
│   ├── html_templates.py
│   ├── file_handler.py
│   └── session_manager.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Move into the project directory

```bash
cd "PY INTERNSHIP PROJECT"
```

### Create a virtual environment

```bash
python -m venv proj
```

### Activate the virtual environment

**Windows**

```bash
proj\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL
- Streamlit Option Menu

---

## Author

Rishabh Gaur