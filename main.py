import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# 乱数シード固定
np.random.seed(0)

# sidebarにおけるパラメータ設定
st.sidebar.markdown('Set Parameter')
lambda_ = st.sidebar.number_input(
  'input lambda',
  min_value=1,
  max_value=100,
  value=10
)
n = st.sidebar.number_input('input n', value=50)
p = lambda_ / n
st.sidebar.markdown(f'calculated p is **{p}**')
size = st.sidebar.number_input('sample size', value=1000)

st.header('Comparison between Poisson and Binomial')
# グラフ設定
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
# ポアソン分布
points = np.random.poisson(lambda_, size=size)
sns.distplot(points, hist=False, bins=100, ax=ax, label='Poisson')
# 二項分布
points = np.random.binomial(n, p, size=size)
sns.distplot(points, hist=False, bins=100, ax=ax, label='Binomial')
ax.legend(loc='upper right', fontsize='xx-large')
fig.tight_layout()

# 可視化
st.subheader('Visualization of distributions')
st.pyplot(fig)

# 数式表現
st.subheader('Mathematical expression')
st.text('Poisson distribution is defined by:')
st.latex(r'''
Po(\lambda) = \frac{\lambda^x e^{-\lambda}}{x!}
''')
st.text('Binomial distribution is defined by:')
st.latex(r'''
Bin(n, p) = {}_n \mathrm{C} _x p^x (1-p)^{n-x}
''')
