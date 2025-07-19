import streamlit as st
from chains import get_specific_temple_info, get_temples_by_location, get_temples_by_era, get_temples_by_deity

st.set_page_config(page_title="TempleGPT - Tamil Nadu Temples", layout="wide")
st.title("TempleGPT: Explore Tamil Nadu's Sacred Temples")
st.markdown("---")

# 🔍 Ask a Question Section
st.header("🔍 Ask a Question About a Temple")
user_input = st.text_input("Enter your question:", "Who built Madurai Meenakshi Amman Temple?")
if st.button("Search Temple Info"):
    response = get_specific_temple_info(user_input)
    if response:
        st.subheader(response["temple_name"])
        st.markdown(f"**Location**: {response['location']}")
        st.markdown(f"**Deity**: {response['deity']}")
        st.markdown(f"**Mythology**: {response['mythology']}")
        st.markdown("**Architecture Details:**")
        arch = response["architecture"]
        st.markdown(f"- Style: {arch.get('style', '-')}")
        st.markdown(f"- Era: {arch.get('era', '-')}")
        st.markdown(f"- Materials: {arch.get('materials', '-')}")
        st.markdown(f"- Features: {arch.get('features', '-')}")
    else:
        st.warning("Temple information not found. Please rephrase your query.")

st.markdown("---")

# 📍 Sidebar for Location / Era / Deity
with st.sidebar:
    st.header("📍 Explore Temples")

    # Location-based
    st.subheader("By Location")
    all_by_location = get_temples_by_location()
    loc = st.selectbox("Choose Location", sorted(all_by_location.keys()))
    if loc:
        for temple in all_by_location[loc]:
            st.text(f"• {temple['temple_name']} (Deity: {temple['deity']})")

    # Era-based
    st.subheader("By Era")
    all_by_era = get_temples_by_era()
    era = st.selectbox("Choose Era", sorted(all_by_era.keys()))
    if era:
        for temple in all_by_era[era]:
            st.text(f"• {temple['temple_name']} ({temple['location']})")

    # Deity-based
    st.subheader("By Deity")
    all_by_deity = get_temples_by_deity()
    deity = st.selectbox("Choose Deity", sorted(all_by_deity.keys()))
    if deity:
        for temple in all_by_deity[deity]:
            st.text(f"• {temple['temple_name']} ({temple['location']})")
