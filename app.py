import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline(
        "translation",
        model="facebook/nllb-200-distilled-600M",
        torch_dtype="auto",
        device_map="auto"
    )

translator = load_model()

st.set_page_config(page_title="Dzonglish", page_icon="Bhutan Flag")

st.title("Bhutan Flag Dzonglish")
st.markdown("### Free Dzongkha ↔ English translator for Bhutan")

col1, col2 = st.columns([3,1])
with col1:
    text = st.text_area("Enter text", height=150, placeholder="Type anything here...")
with col2:
    direction = st.radio("Direction", ["English → Dzongkha", "Dzongkha → English"])

if st.button("Translate Bhutan Flag", type="primary", use_container_width=True):
    if text.strip():
        with st.spinner("Translating..."):
            src = "eng_Latn" if "English" in direction else "dzo_Tibt"
            tgt = "dzo_Tibt" if "English" in direction else "eng_Latn"
            result = translator(text, src_lang=src, tgt_lang=tgt, max_length=500)[0]["translation_text"]
            st.success(result)
    else:
        st.warning("Please type some text first")

st.caption("Made with love for Bhutan • 100% free • https://github.com/ngadamo/dzonglish")
