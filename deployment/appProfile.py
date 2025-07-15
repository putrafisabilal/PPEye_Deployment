import streamlit as st
from PIL import Image

def app():
    # Page Title
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>👷‍♂️ Selamat Datang di <span style='color:#FF5733'>PPEye</span></h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Sistem AI untuk Deteksi Kepatuhan Alat Pelindung Diri (APD)</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Latar Belakang Section
    st.markdown("### 📌 Latar Belakang")
    st.markdown("""
    PT Mayora Indah Tbk menghadapi tantangan serius dalam menjaga kepatuhan penggunaan APD di area produksi — sesuai standar **GMP** dan **ISO 9001**.  
    Pengawasan manual seringkali **tidak efektif**, memakan waktu, dan berisiko tinggi terhadap kualitas serta keamanan produk.

    🧠 Oleh karena itu, kami hadirkan solusi cerdas berupa sistem AI bernama **PPEye**, untuk membantu perusahaan:
    - ✅ Mendeteksi kelengkapan APD secara otomatis
    - ✅ Meningkatkan kepatuhan pekerja
    - ✅ Menjaga standar keamanan pangan & produk
    """)

    st.markdown("---")

    # Apa itu PPEye?
    st.markdown("### 🤖 Apa itu PPEye?")
    st.markdown("""
    **PPEye** adalah sistem berbasis **Artificial Intelligence** yang menggunakan **object detection (YOLOv8)**  
    untuk mendeteksi keberadaan dan kelengkapan APD karyawan di area produksi secara **real-time**.

    🎯 Tujuan utamanya adalah menciptakan lingkungan kerja yang:
    - Aman
    - Sesuai standar industri
    - Bebas kesalahan pengawasan manual
    """)

    st.markdown("---")

    # Kontak
    st.markdown("### 📞 Kontak Kami")
    st.markdown("""
    Jika Anda ingin berdiskusi lebih lanjut atau tertarik dengan implementasi sistem PPEye, silakan hubungi kami:

    - 📧 **Email:** [PPEye.ai@gmail.com](mailto:ppEye.ai@gmail.com)  
    - 📱 **WhatsApp:** +62 812-3456-7890  
    - 🌐 **Website:** [www.ppeye.id](http://www.ppeye.id) *(Coming Soon)*  
    """)

    st.markdown("---")
    st.success("Terima kasih telah mengunjungi PPEye! 👏")