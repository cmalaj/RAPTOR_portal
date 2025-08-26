import streamlit as st
import pandas as pd
import base64
import time
import numpy as np

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
    gap: 1.00rem;  
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
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("<h4>Upload bacterial genome</h4>", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)

# ---- FILE UPLOADER (Styled) ----
uploaded_files = st.file_uploader(
    "Drag and drop files here",
    type=["fasta", "fa", "fna"],
    accept_multiple_files=True,
    label_visibility="collapsed" 
)


# ---- FILE LIST + MOCK PROCESSING ----
if uploaded_files:
    st.markdown("### Uploaded Genomes")
    for file in uploaded_files:
        st.markdown(f"- 📄 `{file.name}`")

    # Display spinner while "processing"
    with st.spinner("Running PADLOC, profiling defences, and predicting phage infectivity..."):
        time.sleep(5)  # simulate processing time

    # Generate fake prediction results
    phage_list = ["Phage_GE9K", "Phage_LG65", "Phage_J5TC", "Phage_EB1D", "Phage_6281", "Phage_4ELK"]
    prediction_scores = np.random.uniform(0.4, 0.99, size=len(phage_list))

    results_df = pd.DataFrame({
        "Phage": phage_list,
        "Predicted Probability of Infection": prediction_scores
    }).sort_values("Predicted Probability of Infection", ascending=False).reset_index(drop=True)

    # Round and format
    results_df["Predicted Probability of Infection"] = results_df["Predicted Probability of Infection"].apply(lambda x: f"{x:.2f}")

    st.markdown("### Predicted Phage Infectivity Scores")
    st.dataframe(results_df.style.highlight_max(axis=0, color='#D2F4EA'))
