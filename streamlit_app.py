import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import folium
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


def main():
    # Créer la carte Folium
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

    # Ajouter un marqueur
    folium.Marker(location=[48.8566, 2.3522], popup='Paris').add_to(m)


    # Convertir la carte Folium en HTML
    m.save("map.html")

    # Afficher la carte HTML dans Streamlit
    st.markdown('<iframe src="map.html" width="100%" height="500"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()



# Créer la carte Folium
map = folium.Map(location=[0, 0], zoom_start=2)
# Ajouter un marqueur aux coordonnées (0, 0)
folium.Marker([0, 0]).add_to(map)

# Afficher la carte dans Streamlit
st.write(map._repr_html_(), unsafe_allow_html=True)

