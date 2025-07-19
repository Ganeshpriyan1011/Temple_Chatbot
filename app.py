import streamlit as st
from chains import generate_answer

st.set_page_config(page_title="TempleGPT", page_icon="🛕")
st.title("TempleGPT 🛕")
st.markdown("Enter a Tamil Nadu temple name to hear its mythology and architecture.")

query = st.text_input("Temple Name")

if st.button("Ask TempleGPT"):
    if query.strip():
        with st.spinner("TempleGPT is processing your question..."):
            result = generate_answer(query)
        st.success("Answer:")
        st.write(result)
    else:
        st.warning("Please enter a temple name.")
