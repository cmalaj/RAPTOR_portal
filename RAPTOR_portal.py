import streamlit as st
import pandas as pd

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="RAPTOR: Rapid Phage Finder",
    layout="centered"
)

# ---- CUSTOM CSS FIX ----
st.markdown("""
<style>
/* Full screen gradient background */
.stApp {
    background: linear-gradient(to bottom, #7ec8e3, #cb9cc5);
    background-attachment: fixed;
}

/* Center header text and upload instruction */
h1, h2, h3, .stTextInput label, .stFileUploader label {
    color: #1a1a1a;
    text-align: center;
}

/* Upload area styling */
.upload-area {
    border: 2px dashed #aa44cc;
    padding: 2rem;
    border-radius: 15px;
    background-color: rgba(255, 255, 255, 0.6);
    margin-top: 1rem;
    margin-bottom: 2rem;
    text-align: center;
}

/* Hide Streamlit's default upload box background */
section[data-testid="stFileUploaderDropzone"] {
    background-color: transparent;
    border: none;
}

.upload-instruction {
    font-size: 1.2rem;
    color: #5c2672;
    margin-top: 1rem;
}

hr {
    border: 1px solid #eee;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.image("RAPTOR_logo.png", width=70)
st.markdown("<h1>RAPTOR: Rapid Phage Finder</h1>", unsafe_allow_html=True)
st.markdown("<h3>Upload bacterial genome(s)</h3>", unsafe_allow_html=True)

# ---- FILE UPLOAD SECTION ----
with st.container():
    st.markdown('<div class="upload-area">', unsafe_allow_html=True)

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

    st.success("Files uploaded. Analysis modules coming soon...")

else:
    st.info("Awaiting FASTA file upload...")