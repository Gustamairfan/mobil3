import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk memuat data
def load_data():
    data = pd.read_csv('mobil.csv')  # Ganti dengan path file data Anda
    return data

# Fungsi untuk menampilkan data tabel
def show_data_table(data):
    st.subheader('Data Tabel')
    st.dataframe(data)

# Fungsi untuk menampilkan informasi data
def show_data_info(data):
    st.subheader('Informasi Data')
    st.write(f"Jumlah Baris: {data.shape[0]}")
    st.write(f"Jumlah Kolom: {data.shape[1]}")

# Fungsi untuk menampilkan statistik deskriptif
def show_data_stats(data):
    st.subheader('Statistik Deskriptif')
    st.write(data.describe())

# Fungsi untuk menampilkan visualisasi data
def show_data_visualization(data):
    st.subheader('Visualisasi Data')

    # Histogram
    st.write('Histogram')
    selected_column = st.selectbox('Pilih Kolom', data.columns)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data[selected_column].dropna(), kde=True, ax=ax)
    st.pyplot(fig)

    # Scatter plot
    st.write('Scatter Plot')
    selected_x = st.selectbox('Pilih Kolom (sumbu x)', data.columns)
    selected_y = st.selectbox('Pilih Kolom (sumbu y)', data.columns)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=data, x=selected_x, y=selected_y, ax=ax)
    st.pyplot(fig)

# Main program
def main():
    st.title('Program Analisis Data')

    # Memuat data
    data = load_data()

    # Sidebar
    menu_options = ['Data Table', 'Informasi Data', 'Statistik Deskriptif', 'Visualisasi Data']
    selected_option = st.sidebar.selectbox('Pilih Menu', menu_options)

    if selected_option == 'Data Table':
        show_data_table(data)
    elif selected_option == 'Informasi Data':
        show_data_info(data)
    elif selected_option == 'Statistik Deskriptif':
        show_data_stats(data)
    elif selected_option == 'Visualisasi Data':
        show_data_visualization(data)

# Menjalankan program
if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()
