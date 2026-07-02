import streamlit as st
from functions.plot import plot_history

st.title('Stocks History')
st.write('Look the stock values.')

ticker = st.sidebar.text_input(
    'Choose the ticker:',
    value = 'NVDA'
)

fig = plot_history(ticker)
st.plotly_chart(fig)