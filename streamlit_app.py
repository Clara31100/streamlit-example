import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
"""
# Graph

 few lines of code
"""

def main():
    # Titre de l'application
    st.title("Graphique Ridgeline avec Streamlit")

    # Générer des données de test
    np.random.seed(0)
    data = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])

    # Créer un graphique ridgeline avec seaborn
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=data, fill=True)
    plt.title('Graphique Ridgeline')
    plt.xlabel('Valeurs')
    plt.ylabel('Densité')
    plt.legend(data.columns)
    st.pyplot()

if __name__ == "__main__":
    main()

