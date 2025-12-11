import streamlit as st
from transformers import pipeline

@st.cache_resource
def get_translator():
    return pipeline(
        "translation",
        model="facebook/nllb-200-distilled-600M",
        device_map="auto",
        torch_dtype="auto"
    )

pipe = get_translator()

st.set_page_config(page_title="Dzonglish", page_icon="Bhutan Flag")

st.title("Bhutan Flag Dzonglish")
st.markdown("**Free Dzongkha ↔ English translator for Bhutan**")

direction = st.radio("Direction", ["English → Dzongkha", "Dzongkha → English"])
text = st.text_area("Type or paste text here", "Gross National Happiness", height=150)

if st.button("Translate", type="primary"):
    src = "eng_Latn" if "English" in direction else "dzo_Tibt"
    tgt = "dzo_Tibt" if "English" in direction else "eng_Latn"
    result = pipe(text, src_lang=src, tgt_lang=tgt, max_length=400)[0]["translation_text"]
    st.success(result)

st.caption("Live at https://ngadamo-dzonglish.streamlit.app")
