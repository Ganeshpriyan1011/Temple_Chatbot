import streamlit as st
from chains import generate_answer

st.set_page_config(page_title="TempleGPT", layout="wide")
st.title("TempleGPT 🛕")

query = st.text_input("Ask about any Tamil Nadu temple (mythology or architecture):")

if query:
    with st.spinner("TempleGPT is thinking..."):
        answer = generate_answer(query)
        st.markdown(answer)
