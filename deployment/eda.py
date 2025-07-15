import streamlit as st
import os
from PIL import Image

# st.set_page_config(page_title="EDA Page", layout="wide")

def app():
    st.title("Exploratory Data Analysis (EDA)")
    st.write("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    """)

    # folder images
    folder_path = "images"
    
    
    # EDA 1
    st.header("Distribusi Label Pada Dataset")

    # Buka gambar dan tampilkan
    eda1 = os.path.join(folder_path, "eda1.png")  # pastikan file ini ada
    image1 = Image.open(eda1)
    st.image(image1, caption="")

    st.markdown("""
                """)
    
    # EDA 2
    st.header("Distribusi Resolusi Gambar per Subset")

    # Buka gambar dan tampilkan
    eda2 = os.path.join(folder_path, "eda2.png")  # pastikan file ini ada
    image2 = Image.open(eda2)
    st.image(image2, caption="")

    st.markdown("""
                """)
    
    # EDA 3
    st.header("Heatmap Bounding Box")

    # Buka gambar dan tampilkan
    eda3 = os.path.join(folder_path, "eda3.png")  # pastikan file ini ada
    image3 = Image.open(eda3)
    st.image(image3, caption="")

    st.markdown("""
                """)
    
    # EDA 4
    st.header("Distribusi Rasio Bounding Box")

    # Buka gambar dan tampilkan
    eda4 = os.path.join(folder_path, "eda4.png")  # pastikan file ini ada
    image4 = Image.open(eda4)
    st.image(image4, caption="")

    st.markdown("""
                """)
    
    # EDA 5
    st.header("Heatmap Distribusi Letak Bounding Box Setiap Label")

    # Buka gambar dan tampilkan
    eda5 = os.path.join(folder_path, "eda5.png")  # pastikan file ini ada
    image5 = Image.open(eda5)
    st.image(image5, caption="")

    st.markdown("""
                """)
