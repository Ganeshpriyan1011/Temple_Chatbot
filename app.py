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

# Get temple data from both helper functions
all_temples_by_location = get_temples_by_location()
all_temples_by_dynasty = get_temples_by_dynasty()

# Extract unique values
unique_locations = sorted(list(set([t.get('location', 'Unknown') for t in all_temples_by_location])))
unique_dynasties = sorted(list(set([t.get('era', 'Unknown') for t in all_temples_by_dynasty])))

# Dropdowns
selected_location = st.sidebar.selectbox("Temple Location", unique_locations)
selected_dynasty = st.sidebar.selectbox("Built Dynasty (Era)", unique_dynasties)

# Show temples matching location
st.sidebar.markdown("---")
st.sidebar.subheader("Temples in this Location")
for temple in all_temples_by_location:
    if temple.get("location") == selected_location:
        st.sidebar.write(f"- {temple['temple_name']}")

# Show temples matching dynasty (era)
st.sidebar.markdown("---")
st.sidebar.subheader("Temples from this Dynasty")
for temple in all_temples_by_dynasty:
    if temple.get("era") == selected_dynasty:
        st.sidebar.write(f"- {temple['temple_name']}")

# Main Query Interface
query = st.text_input("Ask your question")

if st.button("Ask TempleGPT"):
    if query.strip():
        with st.spinner("TempleGPT is thinking..."):
            response = get_specific_temple_info(query)

        if response.get("answer"):
            st.success("TempleGPT says:")
            st.write(response["answer"])

            # Show image if available
            if response.get("image_url"):
                st.image(response["image_url"], caption="AI-generated image", use_column_width=True)
        else:
            st.error("Sorry, no matching temple found.")
    else:
        st.warning("Please enter a question.")
