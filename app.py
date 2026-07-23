import streamlit as st
from functions.plot import plot_history
from functions.backtest import ma_strategy

ticker = st.sidebar.text_input(
    'Choose the ticker:',
    value = 'NVDA'
)

ma_short_window = st.sidebar.number_input(
    "MA Short",
    min_value = 1,
    max_value = 100,
    value = 9,
    step = 1
)

ma_long_window = st.sidebar.number_input(
    "MA Long",
    min_value = 1,
    max_value = 300,
    value = 72,
    step = 1
)


tab1, tab2 = st.tabs([
    'History', 'MA Strategy'
])

with tab1:
    st.title('Stocks History')
    st.write('Look the stock values.')

    fig = plot_history(ticker)
    st.plotly_chart(fig)

with tab2:
    st.title('MA Strategy')
    st.write('Look your portfolio')
    df = ma_strategy(
        ticker = ticker,
        ma_short = ma_short_window,
        ma_long = ma_long_window
    )
    st.dataframe(df)