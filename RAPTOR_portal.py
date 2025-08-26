import streamlit as st
import pandas as pd
import base64

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="RAPTOR: Rapid Phage Finder",
    layout="centered"
)

# ---- CUSTOM CSS ----
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #7ec8e3, #cb9cc5);
}
h1, h2, h3, .stTextInput label, .stFileUploader label {
    color: #1a1a1a;
    text-align: center;
}
.upload-box {
    border: 2px dashed #aa44cc;
    padding: 2rem;
    border-radius: 12px;
    background-color: rgba(255, 255, 255, 0.7);
    text-align: center;
}
.upload-instruction {
    font-size: 1.2rem;
    color: #5c2672;
    margin-top: 1rem;
}
.file-list {
    margin-top: 1rem;
}
hr {
    border: 1px solid #eee;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Icosahedron.svg/1920px-Icosahedron.svg.png", width=70)
st.markdown("<h1>RAPTOR: Rapid Phage Finder</h1>", unsafe_allow_html=True)
st.markdown("<h3>Upload bacterial genome(s)</h3>", unsafe_allow_html=True)

# ---- FILE UPLOAD SECTION ----
with st.container():
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)

    uploaded_files = st.file_uploader(
        "Drag files to upload or click to browse",
        type=["fasta", "fa", "fna"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    st.markdown('<div class="upload-instruction">Drag files to upload<br>or click below</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- FILE LIST + PROCESSING (Placeholder) ----
if uploaded_files:
    st.markdown("### Uploaded Genomes")
    for file in uploaded_files:
        st.markdown(f"- 📄 `{file.name}`")

    st.markdown("✅ Files uploaded. Analysis modules coming soon...")

else:
    st.info("Awaiting FASTA file upload...")