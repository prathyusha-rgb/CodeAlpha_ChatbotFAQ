import streamlit as st
from googletrans import Translator, LANGUAGES

# Page config
st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="centered")

# Title
st.title("🌐 Language Translation Tool")
st.markdown("Translate text between any languages easily!")

# Initialize translator
translator = Translator()

# Build language options
language_options = {v.title(): k for k, v in LANGUAGES.items()}
language_names = sorted(language_options.keys())

# Input Section
st.subheader("Enter Text")
input_text = st.text_area("Type your text here:", height=150, placeholder="Hello, how are you?")

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", ["Auto Detect"] + language_names)

with col2:
    target_lang = st.selectbox("Target Language", language_names, index=language_names.index("Telugu"))

# Translate Button
if st.button("Translate 🔄", use_container_width=True):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some text to translate.")
    else:
        try:
            # Get language code
            src_code = "auto" if source_lang == "Auto Detect" else language_options[source_lang]
            tgt_code = language_options[target_lang]

            # Translate
            with st.spinner("Translating..."):
                result = translator.translate(input_text, src=src_code, dest=tgt_code)

            # Show Result
            st.subheader("✅ Translated Text")
            st.success(result.text)

            # Show detected language if auto
            if source_lang == "Auto Detect":
                detected = LANGUAGES.get(result.src, result.src).title()
                st.info(f"🔍 Detected Source Language: **{detected}**")

            # Copy hint
            st.caption("📋 You can select and copy the translated text above.")

        except Exception as e:
            st.error(f"❌ Translation failed: {str(e)}\nMake sure you have internet connection and googletrans installed.")

# Footer
st.markdown("---")
st.markdown("**How to use:** Enter text → Choose languages → Click Translate!")
st.markdown("Built with `googletrans` + `Streamlit` 🐍")
