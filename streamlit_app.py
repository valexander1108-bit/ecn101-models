import streamlit as st

st.set_page_config(page_title="ECN101 Models", layout="wide")

st.title("ECN101 — Interactive Models")
st.caption("Budget Constraint • PPC • Comparative Advantage • (more coming)")

# --- Sidebar navigation ---
page = st.sidebar.radio(
    "Go to:",
    [
        "Budget Constraint",
        "PPC",
        "Comparative Advantage",
    ],
    index=0
)

# --- Route to sub-apps ---
if page == "Budget Constraint":
    from apps.budget_line import app as budget_app
    budget_app()
elif page == "PPC":
    from apps.ppc import app as ppc_app
    ppc_app()
elif page == "Comparative Advantage":
    from apps.comparative_advantage import app as ca_app
    ca_app()