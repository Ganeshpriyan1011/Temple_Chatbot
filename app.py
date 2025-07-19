import streamlit as st
from chains import get_specific_temple_info, get_temples_by_location, get_temples_by_dynasty
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="TempleGPT 🛕", page_icon="🛕", layout="wide")

st.title("TempleGPT 🛕")
st.markdown("Ask about Tamil Nadu temples: architecture, builders, mythology, and more.")

# Sidebar - Location and Dynasty Filters
st.sidebar.header("📍 Temple Assessment")
selected_location = st.sidebar.selectbox("Temple Location", get_temples_by_location())
selected_dynasty = st.sidebar.selectbox("Built Dynasty", get_temples_by_dynasty())

st.sidebar.markdown("---")
st.sidebar.subheader("Temples in this Location")
for temple in get_temples_by_location(selected_location):
    st.sidebar.write(f"- {temple}")

st.sidebar.markdown("---")
st.sidebar.subheader("Temples by this Dynasty")
for temple in get_temples_by_dynasty(selected_dynasty):
    st.sidebar.write(f"- {temple}")

# Main Query Interface
query = st.text_input("Ask your question")

if st.button("Ask TempleGPT"):
    if query.strip():
        with st.spinner("TempleGPT is thinking..."):
            response = get_specific_temple_info(query)
        st.success("TempleGPT says:")
        st.write(response["answer"])

        # Show image if available
        if response.get("image_url"):
            st.image(response["image_url"], caption="AI-generated image", use_column_width=True)
    else:
        st.warning("Please enter a question.")
