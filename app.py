
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Title of the app
st.title("Market Analysis: Supply and Demand")

# Add motivational message
st.sidebar.info("Hello, I will help you with your homework!")

# Input fields for the first market equations
st.subheader("Market 1: Customize Supply and Demand Equations")
slope_supply_1 = st.number_input("Slope of Supply Curve (Market 1)", value=0.35)
intercept_supply_1 = st.number_input("Intercept of Supply Curve (Market 1)", value=15.0)
slope_demand_1 = st.number_input("Slope of Demand Curve (Market 1)", value=-0.5)
intercept_demand_1 = st.number_input("Intercept of Demand Curve (Market 1)", value=100.0)

# Define supply and demand functions for Market 1
supply_1 = lambda Q: intercept_supply_1 + slope_supply_1 * Q
demand_1 = lambda Q: intercept_demand_1 + slope_demand_1 * Q

# Calculate equilibrium for Market 1
Q_eq_1 = (intercept_demand_1 - intercept_supply_1) / (slope_supply_1 - slope_demand_1)
P_eq_1 = supply_1(Q_eq_1)

# Create Q values for plotting Market 1
Q_values_1 = np.linspace(0, max(Q_eq_1 * 1.5, 300), 1000)

# Plot for Market 1
st.subheader("Market 1: Supply and Demand")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=Q_values_1, y=supply_1(Q_values_1), mode='lines', name='Supply', line=dict(color='blue')))
fig1.add_trace(go.Scatter(x=Q_values_1, y=demand_1(Q_values_1), mode='lines', name='Demand', line=dict(color='red')))
fig1.add_trace(go.Scatter(x=[Q_eq_1], y=[P_eq_1], mode='markers', name='Equilibrium', marker=dict(color='green', size=10)))
fig1.update_layout(title="Market 1: Supply and Demand", xaxis_title="Quantity (Q)", yaxis_title="Price (P)")
st.plotly_chart(fig1)

# Input fields for the second market equations
st.subheader("Market 2: Customize Supply and Demand Equations")
slope_supply_2 = st.number_input("Slope of Supply Curve (Market 2)", value=0.1)
intercept_supply_2 = st.number_input("Intercept of Supply Curve (Market 2)", value=10.0)
slope_demand_2 = st.number_input("Slope of Demand Curve (Market 2)", value=-0.08)
intercept_demand_2 = st.number_input("Intercept of Demand Curve (Market 2)", value=100.0)

# Define supply and demand functions for Market 2
supply_2 = lambda Q: intercept_supply_2 + slope_supply_2 * Q
demand_2 = lambda Q: intercept_demand_2 + slope_demand_2 * Q

# Calculate equilibrium for Market 2
Q_eq_2 = (intercept_demand_2 - intercept_supply_2) / (slope_supply_2 - slope_demand_2)
P_eq_2 = supply_2(Q_eq_2)

# Create Q values for plotting Market 2
Q_values_2 = np.linspace(0, max(Q_eq_2 * 1.5, 1200), 1000)

# Plot for Market 2
st.subheader("Market 2: Supply and Demand")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=Q_values_2, y=supply_2(Q_values_2), mode='lines', name='Supply', line=dict(color='blue')))
fig2.add_trace(go.Scatter(x=Q_values_2, y=demand_2(Q_values_2), mode='lines', name='Demand', line=dict(color='red')))
fig2.add_trace(go.Scatter(x=[Q_eq_2], y=[P_eq_2], mode='markers', name='Equilibrium', marker=dict(color='green', size=10)))
fig2.update_layout(title="Market 2: Supply and Demand", xaxis_title="Quantity (Q)", yaxis_title="Price (P)")
st.plotly_chart(fig2)

# Display equilibrium points
st.subheader("Equilibrium Points")
st.write(f"**Market 1:**\n- Equilibrium Quantity: {Q_eq_1:.2f}\n- Equilibrium Price: {P_eq_1:.2f}")
st.write(f"**Market 2:**\n- Equilibrium Quantity: {Q_eq_2:.2f}\n- Equilibrium Price: {P_eq_2:.2f}")

