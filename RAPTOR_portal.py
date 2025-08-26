import streamlit as st
import pandas as pd
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{encoded}"

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="RAPTOR: Rapid Phage Finder",
    layout="centered"
)

# ---- CSS: Background + Styling ----
st.markdown("""
<style>
/* Full gradient background */
.stApp {
    background: linear-gradient(to bottom, #7ec8e3, #7ec8e3, #FFFFFF, #cb9cc5, #cb9cc5);
    background-attachment: fixed;
}

/* Headings and label text */
h1, h2, h3, .stTextInput label, .stFileUploader label {
    color: #1a1a1a;
    text-align: center;
}

/* Inline logo + title */
.header-inline {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    margin-bottom: 1rem;
}

.logo {
    width: 80px;
    height: auto;
}

.title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1a1a1a;
    margin: 0;
}

/* File uploader styling */
section[data-testid="stFileUploaderDropzone"] {
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 0.75rem;  /* 👈 Adds spacing between icon, title, subtext */
    font-size: 1.25rem;

    border: 2px dashed #aa44cc;
    border-radius: 15px;
    padding: 3rem;
    background-color: rgba(255, 255, 255, 0.8);
    text-align: center;
}

/* Enlarge icon and drag-drop text inside uploader */
section[data-testid="stFileUploaderDropzone"] svg,
section[data-testid="stFileUploaderDropzone"] p {
    transform: scale(1.2);
}

/* Hide default outer uploader border */
div[data-testid="stFileUploader"] > div:first-child {
    border: none;
}

/* Instruction text below uploader */
.upload-instruction {
    font-size: 1.2rem;
    color: #5c2672;
    text-align: center;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
logo_base64 = get_base64_image("RAPTOR_logo.png")

st.markdown(f"""
<div class="header-inline">
    <img src="{logo_base64}" class="logo">
    <h1 class="title">RAPTOR: Rapid Phage Finder</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("<h3>Upload bacterial genome</h3>", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)

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
