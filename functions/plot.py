import plotly.express as px
from plotly.graph_objects import Figure
from functions.data import download_history

def plot_history(ticker:str) -> Figure:
    """
    Plot historical data from yahoo finance.

    Args: 
        ticker (str): Ticker name.
    """


    df = download_history(ticker)

    fig = px.line(
        df,
        x = 'Date',
        y = 'Close',
        title = f'{ticker} stock price.'
    )

    return fig


