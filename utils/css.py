import streamlit as st


SIDEBAR_CSS = """
<style>
section[data-testid="stSidebar"] {
    background-color: #f4f2fc;
    border-right: 1px solid #e8e4f5;
}
.sidebar-logo {
    border-radius: 35px;
    border: 1px solid black;
    display: flex;
    gap: 2px;
    font-size: 40px;
    box-shadow: 0px 0px 4px black;
    margin-bottom: 6px;
}
.sidebar-logo img {
    width: 106px;
    height: auto;
}
.sidebar-logo h3 {
    line-height: 0.9;
    font-size: 35px;
    margin: 0;
    font-weight: 700;
    color: #1a1a2e;
}
.sidebar-logo p {
    line-height: 0.9;
    margin: 0;
    font-size: 25px;
    color: #888;
}
.sidebar-label {
    font-size: 18px;
    color: #999;
    font-weight: bold;
}
.about-box {
    border: 1px solid #d1c3c3;
    background: #f6f7fb;
    border-radius: 12px;
    padding: 14px;
    margin-top: 30px;
    font-size: 13px;
    color: #555;
}
.about-box b { color: #1a1a2e; }
</style>
"""


HOME_CSS = """
<style>
.st-emotion-cache-10p9htt { height: 1.75rem;
}

.section-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 4px;
}
.icon-circle {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: #4b3ff5;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.icon-circle img { width: 20px; filter: brightness(0) invert(1); }
.section-title {
    font-size: 17px;
    font-weight: 700;
    color: #1a1a2e;
    margin: 0;
}
.section-sub {
    font-size: 13px;
    color: #888;
    margin: 0;
}
.file-name-line {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    color: #333;
    margin: 6px 0 18px 0;
}
.file-name-line b { color: #1a1a2e; }
.file-name-line a { color: #4b3ff5; text-decoration: none; }

div[data-testid="stFileUploaderDropzone"] {
    border-radius: 16px;
    border: 2px dashed #d5d5e0;
    background-color: #fafafd;
}
/* ===========================
        Metric Cards - IMPROVED
=========================== */

div[data-testid="stMetric"]{
    background: linear-gradient(180deg, #ffffff, #fafbff);
    border: 1px solid #E7EAF3;
    border-top: 3px solid #5B5CEB;
    border-bottom: 1px solid #5B5CEB;
    border-radius: 18px;
    padding: 24px 18px 20px 18px;
    box-shadow: 0 8px 22px rgba(0,0,0,.08);
    transition: all .25s ease;
    min-height: 120px;
}

div[data-testid="stMetric"]:hover{
    transform: translateY(-4px);
    box-shadow: 0 14px 32px rgba(0,0,0,.14);
    border-top-color: #4338ca;
}

/* Metric Label - BIGGER */
div[data-testid="stMetricLabel"]{
    font-size: 18px ;
    font-weight: 600 ;
    color: #4B5563 ;
    
    margin-bottom: 8px ;
}

/* Metric Value - BIGGER & BOLDER */
div[data-testid="stMetricValue"]{
    font-size: 48px ;
    font-weight: 800 ;
    color: #182A96 ;
    line-height: 1.2 ;
}

div[data-testid="stMetricDelta"]{
    font-size: 14px ;
}
div[data-testid="stAlert"] {
    border-radius: 12px;
}
div[data-testid="stDataFrame"] {
    border: 1px solid #E7EAF3;
    border-radius: 14px;
    overflow: hidden;
}

div[data-testid="stVerticalBlockBorderWrapper"],
div[data-testid="stContainer"]{
    border-radius: 18px ;
    box-shadow: 0 2px 8px rgba(0,0,0,.06) ;
}
/* ===========================
        Tabs - Hover Effect      
=========================== */
button[data-baseweb="tab"]{
    transition: all .2s ease;
    border-radius: 8px 8px 0 0;
    padding: 8px 16px;
}

button[data-baseweb="tab"]:hover{
    background-color: #EEF0FF;
    color: #4338ca ;
    transform: translateY(-2px);
}

button[data-baseweb="tab"][aria-selected="true"]{
    color: #5B5CEB ;
    font-weight: 700 ;
}

button[data-baseweb="tab"][aria-selected="true"]:hover{
    background-color: transparent;
    transform: none;
}

div[data-baseweb="tab-highlight"]{
    background-color: #5B5CEB ;
}

/* ===========================
        All Tables - Border + Shadow
=========================== */

div[data-testid="stDataFrame"],
div[data-testid="stTable"] {
    border: 1px solid #000000;
    border-radius: 14px;
    box-shadow: 0 6px 16px rgba(0,0,0,.25);
    overflow: hidden;
    padding: 2px;
}

/* Covers native HTML tables too, e.g. st.table() or markdown tables */
table {
    border: 1px solid #000000 ;
    border-radius: 14px ;
    box-shadow: 0 0 5px rgba(0,0,0,.25) ;
    overflow: hidden ;
}
/* ===========================
        Buttons
=========================== */

div.stButton > button{
    width:100%;
    height:50px;
    border:none;
    border-radius:12px;
    background:linear-gradient(
        90deg,
        #ba4a00 0%,
        #d35400 50%,
        #e67e22 100%
    );
    color:white;
    font-size:16px;
    font-weight:700;
    transition:all .25s ease;
    box-shadow:0 6px 16px rgba(211,84,0,.30);
}

div.stButton > button:hover{
    
    background:linear-gradient(
        90deg,
       #C2410C 0%,
       #EA580C 50%,
       #FB923C 100%
    );
    transform:translateY(-2px);
    box-shadow:0 10px 22px rgba(211,84,0,.40);
}

div.stButton > button:focus{
    outline:none;
    box-shadow:0 0 0 3px rgba(243,156,18,.25);
}
/* ===========================
        Download Buttons
=========================== */

div[data-testid="stDownloadButton"] > button{
    width:100%;
    height:48px;
    border:none;
    border-radius:12px;

    background:linear-gradient(
        90deg,
        #15803d 0%,
        #16a34a 50%,
        #22c55e 100%
    );

    color:white ;
    font-size:15px;
    font-weight:700;
    box-shadow:0 8px 18px rgba(22,163,74,.30);
    transition:all .25s ease;
}

div[data-testid="stDownloadButton"] > button:hover{
    background:linear-gradient(
        90deg,
        #166534 0%,
        #15803d 50%,
        #16a34a 100%
    );

    transform:translateY(-3px);
    box-shadow:0 12px 24px rgba(22,163,74,.40);
}

div[data-testid="stDownloadButton"] > button:active{
    transform:scale(.98);
}
</style>
"""


def load_css() -> None:
    """
    Apply all custom CSS styles to the Streamlit application.
    """

    st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)
    st.markdown(HOME_CSS, unsafe_allow_html=True)