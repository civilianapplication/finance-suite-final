import streamlit as st

def card(title, value, help_text=None):
    st.markdown(
        f"""
        <div style="
            background-color: #0E1117;
            padding: 16px;
            border-radius: 12px;
            border: 1px solid #262730;
            margin-bottom: 10px;
        ">
            <div style="font-size:14px; opacity:0.7;">{title}</div>
            <div style="font-size:26px; font-weight:600; margin-top:4px;">
                {value}
            </div>
            <div style="font-size:12px; opacity:0.5;">
                {help_text or ""}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def status_box(message, level="good"):
    colors = {
        "good": "#1f8f5f",
        "warn": "#b38b00",
        "bad": "#b3002d"
    }

    st.markdown(
        f"""
        <div style="
            background-color:{colors[level]};
            padding:12px;
            border-radius:10px;
            color:white;
            margin-top:10px;
        ">
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )
