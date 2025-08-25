import streamlit as st
import pandas as pd
from apps.common import Line, base_fig, add_line

def app():
    st.subheader("Supply — Build from Schedule (P = α + βQ, β > 0)")
    colA, colB = st.columns([1,2])

    with colA:
        st.caption("Enter a few (Q,P) points (at least two).")
        df = st.data_editor(
            pd.DataFrame({"Q":[10,30,50], "P":[8,15,24]}),
            num_rows="dynamic",
            use_container_width=True,
            key="sup_sched",
        )
        xmax = st.number_input("Max Q", 10, 1000, 100, 10)
        ymax = st.number_input("Max P", 10, 1000, 50, 5)

    if len(df) >= 2:
        Q = df["Q"].astype(float).values
        P = df["P"].astype(float).values
        b = ((Q - Q.mean())*(P - P.mean())).sum() / max(((Q - Q.mean())**2).sum(), 1e-9)
        a = P.mean() - b*Q.mean()
        S = Line(a=float(a), b=float(b))
    else:
        S = Line(a=5.0, b=0.1)

    with colB:
        fig = base_fig(xmax=xmax, ymax=ymax)
        add_line(fig, S, "Supply (fit)")
        st.plotly_chart(fig, use_container_width=True)
        st.caption(f"Estimated: **P = {S.a:.2f} + ({S.b:.3f})Q**  (β should be positive)")
        show_adv = st.toggle("Advanced (show equations)", value=False)
if show_adv:
    st.latex(r"P = \alpha + \beta Q")   # or st.markdown(...) for text