import streamlit as st
from chains import (
    get_specific_temple_info,
    get_all_locations, get_temples_by_location,
    get_all_eras, get_temples_by_era,
    get_all_deities, get_temples_by_deity
)

st.set_page_config(page_title="TempleGPT 🛕", page_icon="🛕", layout="wide")
st.title("TempleGPT 🛕")
st.markdown("Ask about Tamil Nadu temples: architecture, builders, mythology, and more.")

# Sidebar: Filters
st.sidebar.header("📍 Temple Assessment")

# Location filter
location = st.sidebar.selectbox("Temple Location", ["Select"] + get_all_locations())
if location != "Select":
    st.sidebar.subheader("Temples at this Location")
    for temple in get_temples_by_location(location):
        st.sidebar.markdown(f"- {temple}")

# Era filter
era = st.sidebar.selectbox("Built Dynasty / Era", ["Select"] + get_all_eras())
if era != "Select":
    st.sidebar.subheader("Temples from this Era")
    for temple in get_temples_by_era(era):
        st.sidebar.markdown(f"- {temple}")

# Deity filter
deity = st.sidebar.selectbox("Deity", ["Select"] + get_all_deities())
if deity != "Select":
    st.sidebar.subheader("Temples for this Deity")
    for temple in get_temples_by_deity(deity):
        st.sidebar.markdown(f"- {temple}")

# Query interface
st.markdown("---")
query = st.text_input("Ask your question about a temple")

if st.button("Ask TempleGPT"):
    if query.strip():
        with st.spinner("TempleGPT is thinking..."):
            result = get_specific_temple_info(query)
        st.success("TempleGPT says:")
        st.write(result["answer"])
        if result.get("image_url"):
            st.image(result["image_url"], caption="AI-generated image", use_column_width=True)
    else:
        st.warning("Please enter a question.")
