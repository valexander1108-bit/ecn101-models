import streamlit as st
from apps.common import Line, base_fig, add_line, add_point, intersect

def app():
    st.subheader("Shifts — Demand or Supply (one at a time)")
    xmax = st.sidebar.number_input("Max Q", 10, 1000, 200, 10)
    ymax = st.sidebar.number_input("Max P", 10, 1000, 50, 5)

    st.sidebar.markdown("**Baseline curves** (P = α + βQ)")
    ad = st.sidebar.number_input("α_d (baseline)", value=30.0, step=1.0)
    bd = st.sidebar.number_input("β_d (baseline; <0)", value=-0.2, step=0.05)
    as_ = st.sidebar.number_input("α_s (baseline)", value=5.0, step=1.0)
    bs = st.sidebar.number_input("β_s (baseline; >0)", value=0.1, step=0.05)
    D0, S0 = Line(ad, bd), Line(as_, bs)

    which = st.radio("Shift which curve?", ["Demand", "Supply"], horizontal=True)
    d_alpha = st.slider("Vertical shift Δα", -20.0, 20.0, 0.0, 0.5)
    d_beta  = st.slider("Pivot Δβ", -0.5, 0.5, 0.0, 0.05)

    D1, S1 = D0, S0
    tag = ""
    if which == "Demand":
        D1 = Line(D0.a + d_alpha, D0.b + d_beta)
        tag = "Demand shifted ↑" if d_alpha>0 else ("Demand shifted ↓" if d_alpha<0 else "Demand pivoted")
    else:
        S1 = Line(S0.a + d_alpha, S0.b + d_beta)
        tag = "Supply shifted ↑" if d_alpha>0 else ("Supply shifted ↓" if d_alpha<0 else "Supply pivoted")

    q0,p0 = intersect(D0,S0)
    q1,p1 = intersect(D1,S1)

    fig = base_fig(xmax=xmax, ymax=ymax)
    add_line(fig, D0, "Demand (baseline)", dash="dash")
    add_line(fig, S0, "Supply (baseline)",  dash="dash")
    add_line(fig, D1, "Demand", ) 
    add_line(fig, S1, "Supply", )
    add_point(fig, q0, p0, "(Q0*,P0*)")
    add_point(fig, q1, p1, "(Q1*,P1*)")
    fig.add_annotation(x=0.75*xmax, y=0.9*ymax, text=tag, showarrow=False)

    st.plotly_chart(fig, use_container_width=True, key="shift_single_chart")

    # Direction summary
    price_dir = "↑" if p1>p0 else ("↓" if p1<p0 else "no change")
    qty_dir   = "↑" if q1>q0 else ("↓" if q1<q0 else "no change")
    st.markdown(f"**Price:** {price_dir} &nbsp; | &nbsp; **Quantity:** {qty_dir}")
show_adv = st.toggle("Advanced (show equations)", value=False, key="single_shift_adv")
if show_adv:
    st.latex(r"P = \alpha + \beta Q")   # or st.markdown(...) for text
