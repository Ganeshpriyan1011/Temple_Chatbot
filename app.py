import streamlit as st
from chains import generate_answer

st.set_page_config(page_title="TempleGPT", page_icon="🛕")
st.title("TempleGPT 🛕")
st.markdown("Enter a Tamil Nadu temple name to hear its mythology and architecture.")

query = st.text_input("Temple Name")

# 🔧 Add similarity score threshold slider (default = 0.4)
threshold = st.slider("Similarity Threshold (lower = stricter)", min_value=0.1, max_value=1.0, value=0.4, step=0.05)

if st.button("Ask TempleGPT"):
    if query.strip():
        with st.spinner("TempleGPT is processing your question..."):
            result = generate_answer(query, score_threshold=threshold)
        st.success("Answer:")
        st.write(result)
    else:
        st.warning("Please enter a temple name.")
