import streamlit as st
from transformers import pipeline
import torch

# Load the translator (first load takes ~30s, then cached)
@st.cache_resource
def load_translator():
    return pipeline(
        "translation",
        model="facebook/nllb-200-distilled-600M",
        device=0 if torch.cuda.is_available() else -1
    )

translator = load_translator()

# Page config for nice look
st.set_page_config(
    page_title="Dzonglish",
    page_icon="🇧🇹",
    layout="wide"
)

# Header with Bhutan vibe
st.title("🇧🇹 Dzonglish: Dzongkha ↔ English Translator")
st.markdown("**Free AI tool for Bhutan** – Tuned for GNH, tourism, and daily life. No sign-up needed!")

# UI layout
col1, col2 = st.columns([3, 1])

with col1:
    input_text = st.text_area(
        "Enter text to translate:",
        height=150,
        placeholder="e.g., 'Gross National Happiness guides Bhutan’s development.'"
    )

with col2:
    direction = st.radio(
        "Direction:",
        ["English → Dzongkha", "Dzongkha → English"],
        index=0
    )

# Translate button
if st.button("Translate! 🪔", type="primary", use_container_width=True):
    if input_text.strip():
        with st.spinner("Translating..."):
            src_lang = "eng_Latn" if "English" in direction else "dzo_Tibt"
            tgt_lang = "dzo_Tibt" if "English" in direction else "eng_Latn"
            result = translator(
                input_text,
                src_lang=src_lang,
                tgt_lang=tgt_lang,
                max_length=400
            )[0]["translation_text"]
            st.success("**Translation:**")
            st.markdown(f"```{result}```")
    else:
        st.warning("Please enter some text to translate!")

# Footer
st.markdown("---")
st.markdown(
    "*Powered by Meta's NLLB-200. Built for Bhutan with ❤️. [Source on GitHub](https://github.com/ngadamo/dzonglish-app)*"
)
