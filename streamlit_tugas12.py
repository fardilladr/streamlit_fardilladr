import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("🐱 Tugas Streamlit - fardilladr")

st.text(
    "Kucing adalah hewan mamalia yang lucu dan menggemaskan.\n"
    "Banyak orang memelihara kucing karena sifatnya yang mandiri.")
st.header("Tentang Kucing")
st.subheader("Hewan Peliharaan Favorit")
st.write(
    "Ini adalah file tugas Streamlit baru.\n"
    "Disimpan di folder streamlit_fardilladr."
    )
data = {
    "Nama": ["Milo", "Mela", "Mori"],
    "Umur": [5, 4, 1]
    }
df = pd.DataFrame(data)

st.subheader("Data Kucing")
st.dataframe(df)
fig, ax = plt.subplots()
ax.bar(df["Nama"], df["Umur"])
ax.set_xlabel("Nama")
ax.set_ylabel("Umur")
st.pyplot(fig)