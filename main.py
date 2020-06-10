import streamlit as st
import pandas as pd
import numpy as np




import matplotlib.pyplot as plt

st.header('Play with Normal Distribution!')

mu = st.slider(
  'Select a mean',
  0.0, 100.0, 50.0
)
sigma = st.slider(
  'Select a standard deviation error',
  0.0, 100.0, 10.0
)  # 👈 this is a widget
arr = np.random.normal(mu, sigma**2, size=1000)
plt.hist(arr, bins=100)
plt.title(f'normal distribution ,mu:{mu}, sigma:{sigma}')
st.pyplot()

st.text('Here is the expression.')
st.latex(r'''
N(\mu, \sigma) = \frac{1}{\sqrt{2 \pi }\sigma} exp^{-\frac{(x-\mu)^2}{2{\sigma}^2}}
''')


st.header('Play with Poisson Distribution!')

lambda_ = st.slider(
  'Select a lambda',
  0.0, 100.0, 5.0
)

arr = np.random.poisson(lambda_, size=1000)
plt.hist(arr, bins=100)
plt.title(f'Poisson distribution ,lambda:{lambda_}')
st.pyplot()

st.text('Here is the expression.')
st.latex(r'''
Poisson(\lambda) = \frac{e^{-\lambda}{\lambda}^k}{k!}
''')