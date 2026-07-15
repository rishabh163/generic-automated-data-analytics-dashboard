import streamlit as st


def page_heading(title: str) -> None:
    """
    Display the main page heading with a gradient background.
    """

    st.markdown(
        f"""
        <div style="
            color: white;
            font-family: 'Times New Roman', Times, serif;
            font-size: 34px;
            font-weight: bold;
            text-align: center;
            border: 2px solid #333;
            border-radius: 20px;
            box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
            background: linear-gradient(
                90deg,
                #182a96 0%,
                #4130da 40%,
                #6c31d7 75%,
                #a33cff 100%
            );
            padding: 12px;
            margin-bottom: 20px;
        ">
            {title}
        </div>
        """,
        unsafe_allow_html=True
    )


def style_head(title: str) -> None:
    """
    Display a styled section heading.
    """

    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: flex-start;
            margin: 10px;
        ">
            <div style="
                border: 2px solid #000000;
                border-radius: 12px;
                box-shadow: 0px 0px 6px black;
                padding: 6px 10px;
                background-color: #ffffff;
                width: fit-content;
            ">
                <h4 style="
                    text-align: center;
                    margin: 0;
                    font-family: 'Times New Roman', Times, serif;
                ">
                    {title}
                </h4>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )