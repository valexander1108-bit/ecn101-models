import streamlit as st
from apps.common import Line, base_fig, add_line, add_point, intersect

def make_pane(title, D0, S0, xmax, ymax, which):
    st.markdown(f"### {title}")
    d_alpha = st.slider(f"{which} Δα", -20.0, 20.0, 0.0, 0.5, key=f"{title}_a")
    d_beta  = st.slider(f"{which} Δβ", -0.5, 0.5, 0.0, 0.05, key=f"{title}_b")
    if which=="Demand":
        D1, S1 = Line(D0.a+d_alpha, D0.b+d_beta), S0
    else:
        D1, S1 = D0, Line(S0.a+d_alpha, S0.b+d_beta)

    q0,p0 = intersect(D0,S0)
    q1,p1 = intersect(D1,S1)

    fig = base_fig(xmax=xmax, ymax=ymax)
    add_line(fig, D0, "Demand (baseline)", dash="dash")
    add_line(fig, S0, "Supply (baseline)", dash="dash")
    add_line(fig, D1, "Demand")
    add_line(fig, S1, "Supply")
    add_point(fig, q0, p0, "(Q0*,P0*)")
    add_point(fig, q1, p1, "(Q1*,P1*)")
    fig.update_layout(
    showlegend=False,            # hide legend ("keys")
    height=560,                  # a bit taller
    margin=dict(l=40, r=20, t=20, b=40)
    )
    st.plotly_chart(fig, use_container_width=True,key=f"{title}_chart")

    price_dir = "↑" if p1>p0 else ("↓" if p1<p0 else "ambiguous/no change")
    qty_dir   = "↑" if q1>q0 else ("↓" if q1<q0 else "ambiguous/no change")
    st.markdown(f"**Price:** {price_dir} &nbsp; | &nbsp; **Quantity:** {qty_dir}")

def app():
    st.subheader("Double Shifts — Demand vs Supply (side‑by‑side)")
    xmax = st.sidebar.number_input("Max Q", 10, 1000, 200, 10)
    ymax = st.sidebar.number_input("Max P", 10, 1000, 50, 5)
    st.sidebar.markdown("**Baseline curves**")
    ad = st.sidebar.number_input("α_d", value=30.0, step=1.0)
    bd = st.sidebar.number_input("β_d", value=-0.2, step=0.05)
    as_ = st.sidebar.number_input("α_s", value=5.0, step=1.0)
    bs = st.sidebar.number_input("β_s", value=0.1, step=0.05)
    D0, S0 = Line(ad, bd), Line(as_, bs)

    c1, c2 = st.columns(2)
    with c1: make_pane("Demand shift", D0, S0, xmax, ymax, "Demand")
    with c2: make_pane("Supply shift", D0, S0, xmax, ymax, "Supply")

show_adv = st.toggle("Advanced (show equations)", value=False, key="shifts_double_adv")
if show_adv:
    st.latex(r"P = \alpha + \beta Q")   # or st.markdown(...) for text