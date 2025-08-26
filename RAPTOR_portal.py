import streamlit as st
import pandas as pd

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="RAPTOR: Rapid Phage Finder",
    layout="centered"
)

# ---- CSS: Background + Aligned Upload Styling ----
st.markdown("""
<style>
/* Full gradient background */
.stApp {
    background: linear-gradient(to bottom, #7ec8e3, #FFFFFF, #cb9cc5);
    background-attachment: fixed;
}

/* Headings and text alignment */
h1, h2, h3, .stTextInput label, .stFileUploader label {
    color: #1a1a1a;
    text-align: center;
}

/* Style the native Streamlit uploader dropzone */
section[data-testid="stFileUploaderDropzone"] {
    border: 2px dashed #aa44cc;
    border-radius: 15px;
    padding: 2rem;
    background-color: rgba(255, 255, 255, 0.7);
    text-align: center;
}

/* Hide the default outer uploader border */
div[data-testid="stFileUploader"] > div:first-child {
    border: none;
}

/* Instruction text below uploader */
.upload-instruction {
    font-size: 1.2rem;
    color: #5c2672;
    text-align: center;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.image("RAPTOR_logo.png", width=120)
st.markdown("<h1>RAPTOR: Rapid Phage Finder</h1>", unsafe_allow_html=True)
st.markdown("<h3>Upload bacterial genome</h3>", unsafe_allow_html=True)

# ---- FILE UPLOADER (Styled) ----
uploaded_files = st.file_uploader(
    "Drag and drop files here",
    type=["fasta", "fa", "fna"],
    accept_multiple_files=True,
    label_visibility="collapsed" 
)


# ---- FILE LIST + PROCESSING (Placeholder) ----
if uploaded_files:
    st.markdown("### Uploaded Genomes")
    for file in uploaded_files:
        st.markdown(f"- 📄 `{file.name}`")
    st.success("File uploaded. Analysing files... (This is a placeholder for actual processing)")
