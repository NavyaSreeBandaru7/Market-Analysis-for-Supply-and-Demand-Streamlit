import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Title of the app
st.title("Market Analysis: Supply and Demand")

# Define the equations for the first market
supply_1 = lambda Q: 15 + 0.35 * Q
demand_1 = lambda Q: 100 - 0.5 * Q

# Define the equations for the second market
supply_2 = lambda Q: 10 + 0.1 * Q
demand_2 = lambda Q: 100 - 0.08 * Q

# Create a range of Q values for plotting
Q_values_1 = np.linspace(0, 300, 1000)
Q_values_2 = np.linspace(0, 1200, 1000)  # Adjusted range for the second market

# Calculate equilibrium for the first market
Q_eq_1 = (100 - 15) / (0.35 + 0.5)
P_eq_1 = supply_1(Q_eq_1)

# Calculate equilibrium for the second market
Q_eq_2 = (100 - 10) / (0.1 + 0.08)
P_eq_2 = supply_2(Q_eq_2)

# Plot for the first market
st.subheader("Market 1: Supply and Demand")
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=Q_values_1, y=supply_1(Q_values_1), mode='lines', name='Supply', line=dict(color='blue')))
fig1.add_trace(go.Scatter(x=Q_values_1, y=demand_1(Q_values_1), mode='lines', name='Demand', line=dict(color='red')))
fig1.add_trace(go.Scatter(x=[Q_eq_1], y=[P_eq_1], mode='markers', name='Equilibrium', marker=dict(color='green', size=10)))
fig1.update_layout(title="Market 1: Supply and Demand", xaxis_title="Quantity (Q)", yaxis_title="Price (P)")

st.plotly_chart(fig1)

# Plot for the second market
st.subheader("Market 2: Fresh Oranges")
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=Q_values_2, y=supply_2(Q_values_2), mode='lines', name='Supply', line=dict(color='blue')))
fig2.add_trace(go.Scatter(x=Q_values_2, y=demand_2(Q_values_2), mode='lines', name='Demand', line=dict(color='red')))
fig2.add_trace(go.Scatter(x=[Q_eq_2], y=[P_eq_2], mode='markers', name='Equilibrium', marker=dict(color='green', size=10)))
fig2.update_layout(title="Market 2: Fresh Oranges", xaxis_title="Quantity (Q)", yaxis_title="Price (P)")

st.plotly_chart(fig2)

# Display equilibrium values
st.subheader("Equilibrium Points")
st.write("**Market 1:**")
st.write(f"Equilibrium Quantity: {Q_eq_1:.2f}")
st.write(f"Equilibrium Price: {P_eq_1:.2f}")

st.write("**Market 2:**")
st.write(f"Equilibrium Quantity: {Q_eq_2:.2f} (in 1,000 crates)")
st.write(f"Equilibrium Price: {P_eq_2:.2f}")
