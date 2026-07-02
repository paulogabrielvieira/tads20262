import pandas as pd
import yfinance as yf

def download_history(
    ticker:str,
    multi_level_index:bool = False
)-> pd.DataFrame:
    """ 
    Download historical data from yahoo finance.

    Args:
        ticker (str): Ticker name.
        multi_level_inde (bool): Remove/include multi index.    
    """

    df = yf.download(
        tickers = ticker,
        multi_level_index = multi_level_index
    ).reset_index()

    return df    