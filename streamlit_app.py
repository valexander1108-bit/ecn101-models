# --- NAV & ROUTER (replace your current block with this) ---
import streamlit as st

options = [
    "Budget Constraint","PPC","Comparative Advantage",
    "Demand (schedule → line)","Supply (schedule → line)",
    "Static Equilibrium","Shifts (single)","Shifts (double)",
]

# read “default target” set by subpages (if any)
default = st.session_state.get("nav_default", options[0])

# single radio, unique key
page = st.sidebar.radio(
    "Go to:",
    options,
    index=options.index(default),
    key="main_nav"
)

# consume the default so it doesn't stick
st.session_state.pop("nav_default", None)

# --- routes ---
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