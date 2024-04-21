import wfdb
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
from paths import get_bases_and_path_dict
plt.ioff()

WFDB_BASES_NAMES, WFDB_TO_RECORD = get_bases_and_path_dict()
#record = wfdb.rdrecord(WFDB_TO_RECORD[WFDB_BASES_NAMES[0]][0])

def generate_plot(record_path: str) -> go.Figure:
    record = wfdb.rdrecord(record_path)
    figure = wfdb.plot_wfdb(record=record, return_fig=True)
    plotly_fig = go.Figure()

    for ax in figure.get_axes():
        for line in ax.get_lines():
            x, y = line.get_data()
            plotly_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=ax.get_ylabel(), visible="legendonly"))

        xlabel = ax.get_xlabel()
        plotly_fig.update_layout(xaxis_title=xlabel)

    plotly_fig.update_layout(template="plotly_white", dragmode='pan', title=figure.axes[0].get_title())
    return plotly_fig
    
def save_plot(fig: go.Figure, save_path: str = "templates/plot.html", config: dict = {'scrollZoom': True, 'displaylogo': False}) -> None:
    html_plot = pio.to_html(fig, full_html=False, config=config)

    with open(save_path, "w") as f:
        f.write(html_plot)

def generate_and_save_plot(record_path: str) -> None:
    save_plot(generate_plot(record_path))

generate_and_save_plot(WFDB_TO_RECORD[WFDB_BASES_NAMES[0]][0])