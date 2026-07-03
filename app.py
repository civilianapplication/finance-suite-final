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
    import streamlit as st
from datetime import date

from db import init, add, get_all
from finance import *

init()

st.set_page_config(page_title="Finance Suite", layout="wide")

data = get_all()

income, expenses, dividends = breakdown(data)

salary = st.sidebar.number_input("Salary", value=1047.5)
pension = st.sidebar.number_input("Pension", value=500.0)

p = profit(income, expenses, salary, pension)
tax = corp_tax_amount(p)
ret = retained(p, tax, dividends)

page = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Add Transaction", "History", "Decision Engine", "Scenario"]
)

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.title("📊 Finance Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Income", f"£{income:.2f}")
    c2.metric("Profit", f"£{p:.2f}")
    c3.metric("Tax Reserve", f"£{tax:.2f}")
    c4.metric("Retained", f"£{ret:.2f}")

    st.divider()
    st.success(f"Safe Withdrawal: £{safe_withdrawal(ret):.2f}")

# ---------------- ADD ----------------
elif page == "Add Transaction":
    st.title("➕ Add Transaction")

    ttype = st.selectbox("Type", ["income", "expense", "dividend"])
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Save"):
        add(ttype, category, amount, str(date.today()))
        st.success("Saved")

# ---------------- HISTORY ----------------
elif page == "History":
    st.title("📜 History")
    st.dataframe(data)

# ---------------- DECISION ENGINE ----------------
elif page == "Decision Engine":
    st.title("🧠 Decision Engine")

    st.subheader("Can I take money out?")

    if ret < 0:
        st.error("❌ Overdrawn — stop dividends")
    else:
        st.success("✔ Safe to extract funds")

    st.write("Recommended withdrawal:")
    st.info(f"£{safe_withdrawal(ret):.2f}")

# ---------------- SCENARIO ----------------
elif page == "Scenario":
    st.title("📈 Scenario Simulator")

    adj_income = st.slider("Income multiplier", 0.5, 2.0, 1.0)
    adj_expenses = st.slider("Expense multiplier", 0.5, 2.0, 1.0)

    sim_income = income * adj_income
    sim_expenses = expenses * adj_expenses

    sim_p = profit(sim_income, sim_expenses, salary, pension)
    sim_tax = corp_tax_amount(sim_p)
    sim_ret = retained(sim_p, sim_tax, dividends)

    st.metric("Sim Profit", f"£{sim_p:.2f}")
    st.metric("Sim Tax", f"£{sim_tax:.2f}")
    st.metric("Sim Retained", f"£{sim_ret:.2f}")
