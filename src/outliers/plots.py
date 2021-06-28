import matplotlib.pyplot as plt
import plotly.graph_objects as go


def show_outliers(original, outliers):
    fig, ax = plt.subplots(figsize=(15,3), sharex=True)
    ax.plot(original, linewidth=1)
    ax.scatter(x=outliers.index, y=outliers, color='r', marker='+', s=30)

def show_outliers_w_zoom(original, outliers):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=original.index, y=original,
                    mode='lines',
                    name='Original'))
    fig.add_trace(go.Scatter(x=outliers.index, y=outliers,
                    mode='markers',
                    name='Outliers'))  
    fig.show()