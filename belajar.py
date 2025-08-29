import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Visualisasi Dataset Seaborn")
st.subheader("Informasi Dataset")

datasets = sns.get_dataset_names()
dataset_name = st.sidebar.selectbox("Pilih dataset", datasets)

data = sns.load_dataset(dataset_name)

st.write(f"Dataset : {dataset_name}")
st.write(f"Dimensi data : `{data.shape}`")
st.write(data.tail())

graph_type = st.sidebar.selectbox("Pilih jenis visualisasi", ["Histogram", "Scatter Plot", "Box Plot", "Bar Plot"])

columns = data.columns

if graph_type == "Histogram":
    column = st.sidebar.selectbox("Pilih kolom", data.columns)
    bins = st.sidebar.slider("Jumlah bin", min_value=5, max_value=50, value=20)

    fig, ax = plt.subplots()
    sns.histplot(data[column], bins=bins, kde=True, ax=ax)
    st.pyplot(fig)

elif graph_type == "Scatter Plot":
    column_x = st.sidebar.selectbox("Pilih kolom X :", columns)
    column_y = st.sidebar.selectbox("Pilih kolom y :", columns)
    column_hue = st.sidebar.selectbox("Pilih kolom hue (Opsional) :", [None] + list(columns))

    fig, ax = plt.subplots()
    sns.scatterplot(data, x=column_x, y=column_y, hue=column_hue, ax=ax)
    st.pyplot(fig)

elif graph_type == "Box Plot":
    column_x = st.sidebar.selectbox("Pilih kolom X :", columns)
    column_y = st.sidebar.selectbox("Pilih kolom y :", columns)
    column_hue = st.sidebar.selectbox("Pilih kolom hue (Opsional) :", [None] + list(columns))

    fig, ax = plt.subplots()
    sns.boxplot(data, x=column_x, y=column_y, hue=column_hue, ax=ax)
    st.pyplot(fig)

elif graph_type == "Bar Plot":
    column_x = st.sidebar.selectbox("Pilih kolom X :", columns)
    column_y = st.sidebar.selectbox("Pilih kolom y :", columns)
    column_hue = st.sidebar.selectbox("Pilih kolom hue (Opsional) :", [None] + list(columns))

    fig, ax = plt.subplots()
    sns.barplot(data, x=column_x, y=column_y, hue=column_hue, ax=ax)
    st.pyplot(fig)