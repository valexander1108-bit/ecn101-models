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
        # --- Module 2 ---
        "Demand (schedule → line)",
        "Supply (schedule → line)",
        "Static Equilibrium",
        "Shifts (single)",
        "Shifts (double)",
    ],
    index=0,
    key="nav",
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
elif page == "Demand (schedule → line)":
    from apps.demand_schedule import app as dem_app
    dem_app()
elif page == "Supply (schedule → line)":
    from apps.supply_schedule import app as sup_app
    sup_app()
elif page == "Static Equilibrium":
    from apps.static_equilibrium import app as se_app
    se_app()
elif page == "Shifts (single)":
    from apps.shifts_single import app as ss_app
    ss_app()
elif page == "Shifts (double)":
    from apps.shifts_double import app as sd_app
    sd_app()