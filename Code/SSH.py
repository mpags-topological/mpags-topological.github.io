import numpy as np
import plotly.graph_objects as go
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider, Button

def Energy(ratio, k):
    return np.sqrt(ratio**2 + 1 + 2*ratio*np.cos(k))

k = np.linspace(-np.pi, np.pi, 101)


# Slider values
ratio_values = np.linspace(-2, 2, 41, endpoint=True)


# Create initial figure
fig = go.Figure()

# Add the first frame (initial t1, t2)
initial_ratio = 0
active_index = np.where(ratio_values == initial_ratio)[0][0]

# Create figure
fig = go.Figure()

# Upper and lower bands
fig.add_trace(go.Scatter(x=k, y=Energy(initial_ratio, k), name="+E(k)", line=dict(color="blue")))
fig.add_trace(go.Scatter(x=k, y=-Energy(initial_ratio, k), name="-E(k)", line=dict(color="red")))



# Slider for t1
ratio_steps = []
for ratio in ratio_values:
    step = dict(
        method="update",
        args=[{"y": [Energy(ratio, k), -Energy(ratio, k)]}],
        label=f"{ratio:.2f}"
    )
    ratio_steps.append(step)

# Combine sliders
sliders = [
    dict(active=active_index, currentvalue={"prefix": "t1/t2="}, pad={"t": 50}, steps=ratio_steps),
]

fig.update_layout(
    sliders=sliders,
    xaxis_title="k",
    yaxis_title="E(k)/t2",
    yaxis=dict(range=[-4, 4]),
    width=500,
    height=500
)

# # Show figure interactively
# fig.show(renderer="browser")

# Export as standalone HTML (for embedding)
fig.write_html("mpags-topological/_static/plots/ssh_dispersion.html", include_plotlyjs='cdn')

print("Successfully Saved")