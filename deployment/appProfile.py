import streamlit as st

def app():
    # Page Title
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>😷 Selamat Datang di <span style='color:#FF5733'>PPEye</span></h1>", unsafe_allow_html=True)
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
     # TEAM PROFILE SECTION
    st.markdown("<h1 style='font-size: 48px; text-align: center;'>TIM KAMI</h1>", unsafe_allow_html=True)
    # Create four columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display each image in its respective column
    with col1:
        st.image("images/kalis.jpg", use_container_width=True)
        st.write("<p style='text-align: center;'>Lis Wahyuni</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: center;font-weight: bold;'>Mentor</p>", unsafe_allow_html=True)

    with col2:
        st.image("images/pesoy.png", use_container_width=True)
        st.write("<p style='text-align: center;'>Gregorius Yoseph Radityo</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: center;font-weight: bold;'>Project Manager, Data Engineer</p>", unsafe_allow_html=True)

    with col3:
        st.image("images/bilal.png", use_container_width=True)
        st.write("<p style='text-align: center;'>Putra Fisabil Muhammad</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: center;font-weight: bold;'>Data Engineer, Data Scientist, & Data Anotator</p>", unsafe_allow_html=True)

    with col4:
        st.image("images/rafi.png", use_container_width=True)
        st.write("<p style='text-align: center;'>Rafi Arya Siregar</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: center;font-weight: bold;'>Data Analyst & Data Anotator</p>", unsafe_allow_html=True)

    with col5:
        st.image("images/rifqi.png", use_container_width=True)
        st.write("<p style='text-align: center;'>Rifqi Munif Imanullah</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: center;font-weight: bold;'>Data Scientist & Data Anotator</p>", unsafe_allow_html=True)

    st.markdown("---")

    # Kontak
    st.markdown("### 📞 Kontak Kami")
    st.markdown("""
    Jika Anda ingin berdiskusi lebih lanjut atau tertarik dengan implementasi sistem PPEye, silakan hubungi kami:

    - 📧 **Email:** [yoseph.radityo@gmail.com](mailto:yoseph.radityo@gmail.com)
    - 📧 **Email:** [bilalputra17@gmail.com](mailto:bilalputra17@gmail.com)
    - 📧 **Email:** [rafaryasiregar@gmail.com](mailto:rafaryasiregar@gmail.com) 
    - 📧 **Email:** [imanullahrifqi@gmail.com](mailto:imanullahrifqi@gmail.com)             
    """)

    st.markdown("---")
    st.success("Terima kasih telah mengunjungi PPEye! 👏")