import streamlit as st
from apps.common import Line, base_fig, add_line, add_point, intersect

def app():
    st.subheader("Static Equilibrium")
    xmax = st.sidebar.number_input("Max Q", 10, 1000, 200, 10)
    ymax = st.sidebar.number_input("Max P", 10, 1000, 50, 5)

    st.sidebar.markdown("**Demand (β < 0)** — P = α + βQ")
    ad = st.sidebar.number_input("α_d", value=30.0, step=1.0)
    bd = st.sidebar.number_input("β_d", value=-0.2, step=0.05)

    st.sidebar.markdown("**Supply (β > 0)** — P = α + βQ")
    as_ = st.sidebar.number_input("α_s", value=5.0, step=1.0)
    bs = st.sidebar.number_input("β_s", value=0.1, step=0.05)

    D, S = Line(ad, bd), Line(as_, bs)
    q_star, p_star = intersect(D, S)

    if "prev_eq" not in st.session_state:
        st.session_state.prev_eq = None

    c1, c2 = st.columns(2)
    with c1:
        hide_d = st.toggle("Hide Demand", value=False)
    with c2:
        hide_s = st.toggle("Hide Supply", value=False)

    fig = base_fig(xmax=xmax, ymax=ymax)
    if not hide_d: add_line(fig, D, "Demand")
    if not hide_s: add_line(fig, S, "Supply")
    if not hide_d and not hide_s:
        add_point(fig, q_star, p_star, "(Q*, P*)")
        st.session_state.prev_eq = (q_star, p_star)
    elif st.session_state.prev_eq:
        q0, p0 = st.session_state.prev_eq
        add_point(fig, q0, p0, "previous equilibrium")

    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**Equilibrium:** Q* = {q_star:.2f}, P* = {p_star:.2f}")
    
    show_adv = st.toggle("Advanced (show equations)", value=False)
if show_adv:
    st.latex(r"P = \alpha + \beta Q")   # or st.markdown(...) for text
