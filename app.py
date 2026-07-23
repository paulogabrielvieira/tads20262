import streamlit as st
from functions.plot import plot_history
from functions.backtest import ma_strategy

st.title('Stocks History')
st.write('Look the stock values.')

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

fig = plot_history(ticker)
st.plotly_chart(fig)

df = ma_strategy(
    ticker = ticker,
    ma_short = ma_short_window,
    ma_long = ma_long_window
)

st.dataframe(df)