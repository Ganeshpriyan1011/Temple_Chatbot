import streamlit as st
from chains import get_specific_temple_info, get_temples_by_location, get_temples_by_dynasty
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="TempleGPT 🛕", page_icon="🛕", layout="wide")

st.title("TempleGPT 🛕")
st.markdown("Ask about Tamil Nadu temples: architecture, builders, mythology, and more.")

# Load all temples once
all_temples_by_location = get_temples_by_location("All")
all_temples_by_dynasty = get_temples_by_dynasty("All")

# Unique locations and dynasties for dropdowns
unique_locations = sorted(list(set([t['location'] for t in all_temples_by_location])))
unique_dynasties = sorted(list(set([t['architecture']['dynasty'] for t in all_temples_by_dynasty])))

# Sidebar - Location and Dynasty Filters
st.sidebar.header("📍 Temple Assessment")
selected_location = st.sidebar.selectbox("Temple Location", ["All"] + unique_locations)
selected_dynasty = st.sidebar.selectbox("Built Dynasty", ["All"] + unique_dynasties)

st.sidebar.markdown("---")
st.sidebar.subheader("Temples in this Location")
filtered_by_location = get_temples_by_location(selected_location)
for temple in filtered_by_location:
    st.sidebar.write(f"🛕 {temple['temple_name']}")

st.sidebar.markdown("---")
st.sidebar.subheader("Temples by this Dynasty")
filtered_by_dynasty = get_temples_by_dynasty(selected_dynasty)
for temple in filtered_by_dynasty:
    st.sidebar.write(f"🏛️ {temple['temple_name']}")

# Main Query Interface
query = st.text_input("Ask your question")

if st.button("Ask TempleGPT"):
    if query.strip():
        with st.spinner("TempleGPT is thinking..."):
            response = get_specific_temple_info(query)
        st.success("TempleGPT says:")
        st.write(response)

        # Optional: Auto-generate image using prompt (if you have a local/gen API or placeholder)
        if "temple_name" in query.lower():
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Big_Temple_Thanjavur.jpg/1280px-Big_Temple_Thanjavur.jpg", caption="Sample temple image", use_column_width=True)
    else:
        st.warning("Please enter a question.")
