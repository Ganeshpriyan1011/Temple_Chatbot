import streamlit as st
from chains import (
    get_specific_temple_info,
    get_temples_by_location,
    get_temples_by_dynasty,
    get_temples_by_deity
)

st.set_page_config(page_title="TempleGPT 🛕", page_icon="🛕", layout="wide")

st.title("TempleGPT 🛕")
st.markdown("Ask about Tamil Nadu temples: architecture, builders, mythology, and more.")

# Sidebar Assessments
st.sidebar.header("📍 Temple Assessments")

# Location
selected_location = st.sidebar.selectbox("Temple Location", get_temples_by_location())
st.sidebar.subheader("Temples in this Location")
for temple in get_temples_by_location(selected_location):
    st.sidebar.write(f"- {temple}")

st.sidebar.markdown("---")

# Era/Dynasty
selected_dynasty = st.sidebar.selectbox("Built Dynasty (Era)", get_temples_by_dynasty())
st.sidebar.subheader("Temples by this Dynasty")
for temple in get_temples_by_dynasty(selected_dynasty):
    st.sidebar.write(f"- {temple}")

st.sidebar.markdown("---")

# Deity
selected_deity = st.sidebar.selectbox("Main Deity", get_temples_by_deity())
st.sidebar.subheader("Temples with this Deity")
for temple in get_temples_by_deity(selected_deity):
    st.sidebar.write(f"- {temple}")

st.markdown("---")

# Main Prompt
query = st.text_input("Ask your question")

if st.button("Ask TempleGPT"):
    if query.strip():
        with st.spinner("TempleGPT is thinking..."):
            response = get_specific_temple_info(query)
        st.success("TempleGPT says:")
        st.markdown(response["answer"])
    else:
        st.warning("Please enter a question.")
