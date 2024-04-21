import wfdb
import matplotlib.pyplot as plt
import plotly.graph_objects as go

plt.ioff()

def generate_plot_and_comments(record_path: str) -> tuple[go.Figure, str]:
    record = wfdb.rdrecord(record_path)
    figure = wfdb.plot_wfdb(record=record, return_fig=True)
    plotly_fig = go.Figure()

    for ax in figure.get_axes():
        for line in ax.get_lines():
            x, y = line.get_data()
            plotly_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=ax.get_ylabel(), visible="legendonly"))

        xlabel = ax.get_xlabel()
        plotly_fig.update_layout(xaxis_title=xlabel)

    plotly_fig.update_layout(template="plotly_white", dragmode='pan', title=figure.axes[0].get_title(), height=700, width=1520)

    return plotly_fig, record.comments[0]
    