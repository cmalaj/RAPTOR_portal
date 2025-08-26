import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(page_title="Phage Infection Predictor", layout="wide")

st.title("🔬 Bacterial Genome → Phage Infection Predictor Portal")

st.markdown("""
Upload a bacterial genome FASTA file. The portal will:
1. Annotate defence systems (via PADLOC)
2. Build a defence profile
3. Predict which phages from our library are likely to infect the bacterium.
""")

# ---------------------
# Placeholder Functions
# ---------------------

def run_padloc(fasta_str):
    # Placeholder for PADLOC pipeline call
    st.info("Running PADLOC annotation (placeholder)...")
    return {"RM": True, "CBASS": False, "Druantia": True}  # dummy result

def build_defence_profile(padloc_results):
    # Placeholder: convert PADLOC JSON to binary presence/absence
    st.info("Building defence system profile (placeholder)...")
    profile = {k: int(v) for k, v in padloc_results.items()}
    return pd.DataFrame([profile])

def predict_phage_infectivity(defence_profile_df):
    # Placeholder: run prediction using trained CatBoost model
    st.info("Running CatBoost prediction (placeholder)...")
    dummy_phage_scores = {
        "Phage_GE9K": 0.92,
        "Phage_LG65": 0.15,
        "Phage_EB1D": 0.74
    }
    return pd.DataFrame.from_dict(dummy_phage_scores, orient="index", columns=["Predicted Score"]).sort_values("Predicted Score", ascending=False)

# ---------------------
# Upload and Processing
# ---------------------

uploaded_file = st.file_uploader("Upload bacterial genome (FASTA format)", type=["fasta", "fa", "fna"])

if uploaded_file is not None:
    fasta_content = uploaded_file.read().decode("utf-8")
    st.text_area("FASTA Preview", fasta_content[:1000], height=200)

    # --- Run Pipeline ---
    with st.spinner("Processing uploaded genome..."):
        padloc_results = run_padloc(fasta_content)
        defence_profile_df = build_defence_profile(padloc_results)
        phage_preds_df = predict_phage_infectivity(defence_profile_df)

    # --- Results Display ---
    st.subheader("📊 Predicted Phage Infectivity Scores")
    st.dataframe(phage_preds_df.style.background_gradient(cmap="viridis", axis=0))

else:
    st.warning("Please upload a FASTA file to begin.")