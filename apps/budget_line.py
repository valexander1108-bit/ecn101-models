import numpy as np
import streamlit as st
import plotly.graph_objects as go

def app():
    st.subheader("Budget Constraint")
    with st.sidebar.expander("Budget Inputs", expanded=True):
        M  = st.number_input("Income (M)", min_value=1.0, value=30.0, step=1.0)
        px = st.number_input("Price of good X (pₓ)", min_value=0.01, value=1.0, step=0.1, format="%.2f")
        py = st.number_input("Price of good Y (pᵧ)", min_value=0.01, value=1.0, step=0.1, format="%.2f")
        xmax = st.number_input("Max X", min_value=10, value=40, step=5)
        ymax = st.number_input("Max Y", min_value=10, value=40, step=5)

    # Intercepts
    x_int = M / px
    y_int = M / py

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, x_int], y=[y_int, 0], mode="lines", name="Budget Line"))
    fig.update_xaxes(range=[0, xmax], title="Good X")
    fig.update_yaxes(range=[0, ymax], title="Good Y")
    fig.update_layout(height=500, margin=dict(l=10, r=10, t=10, b=10))

    st.plotly_chart(fig, use_container_width=True)

    st.caption(f"Intercepts: X = {x_int:.2f}, Y = {y_int:.2f}  •  Slope = -pₓ/pᵧ = {-px/py:.3f}")
