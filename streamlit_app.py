import streamlit as st

options = [
    "Budget Constraint","PPC","Comparative Advantage",
    "Demand (schedule → line)","Supply (schedule → line)",
    "Static Equilibrium","Shifts (single)","Shifts (double)",
]

default = st.session_state.get("nav_default", options[0])

# Use a UNIQUE key that nothing else uses
page = st.sidebar.radio(
    "Go to:",
    options,
    index=options.index(default),
    key="main_nav"   # <-- renamed from 'nav'
)

# optional: once consumed, clear the default
st.session_state.pop("nav_default", None)