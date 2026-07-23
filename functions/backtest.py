import pandas as pd
import vectorbt as vbt

def ma_strategy(          
    ticker:str,
    ma_short:int = 9,
    ma_long:int = 72
) -> pd.DataFrame:
    """ 
    Trading strategy using moving average.

    Args:
        ticker (str): Ticker name.
        ma_short (int): Short moving average. Default is 9.
        ma_long (int): Long moving average. Default is 72.
    """

    price = (
      vbt.YFData
        .download(ticker)
        .get('Close')
    )

    mas = vbt.MA.run(price, window=ma_short)
    mal = vbt.MA.run(price, window=ma_long)

    entries = mas.ma_crossed_above(mal)
    exits = mas.ma_crossed_below(mal)

    portfolio = vbt.Portfolio.from_signals(
        close = price,
        entries = entries,
        exits = exits,
        init_cash = 10_000,
        fees = 0.001,      # 0.1%
        slippage = 0.001   # 0.1%
    )

    df = (
        portfolio
            .stats()
            .to_frame('Value')
    )

    return df