import numpy as np
import plotly.graph_objects as go
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider, Button

def Energy(t1, t2, k):
    return np.sqrt(t1**2 + t2**2 + 2*t1*t2*np.cos(k))

k = np.linspace(-np.pi, np.pi, 100)


# Slider values
t_values = np.linspace(0, 1, 10)

# Create initial figure
fig = go.Figure()

# Add the first frame (initial t1, t2)
initial_t1 = 0.5
initial_t2 = 0.5

# Create figure
fig = go.Figure()

# Upper and lower bands
fig.add_trace(go.Scatter(x=k, y=Energy(initial_t1, initial_t2, k), name="+E(k)", line=dict(color="blue")))
fig.add_trace(go.Scatter(x=k, y=-Energy(initial_t1, initial_t2, k), name="-E(k)", line=dict(color="red")))

# Slider values
t1_values = np.linspace(0, 1, 21)
t2_values = np.linspace(0, 1, 21)

# Slider for t1
t1_steps = []
for t1 in t1_values:
    step = dict(
        method="update",
        args=[{"y": [Energy(t1, initial_t2, k), -Energy(t1, initial_t2, k)]}],
        label=f"{t1:.2f}"
    )
    t1_steps.append(step)

# Slider for t2
t2_steps = []
for t2 in t2_values:
    step = dict(
        method="update",
        args=[{"y": [Energy(initial_t1, t2, k), -Energy(initial_t1, t2, k)]}],
        label=f"{t2:.2f}"
    )
    t2_steps.append(step)

# Combine sliders
sliders = [
    dict(active=int(initial_t1*20), currentvalue={"prefix": "t1="}, pad={"t": 50}, steps=t1_steps),
    dict(active=int(initial_t2*20), currentvalue={"prefix": "t2="}, pad={"t": 150}, steps=t2_steps)
]

fig.update_layout(
    sliders=sliders,
    xaxis_title="k",
    yaxis_title="E(k)",
    yaxis=dict(range=[-2, 2]),
    width=500,
    height=500
)

# # Show figure interactively
# fig.show(renderer="browser")

# Export as standalone HTML (for embedding)
fig.write_html("mpags-topological/_static/plots/ssh_dispersion.html", include_plotlyjs='cdn')

print("Successfully Saved")