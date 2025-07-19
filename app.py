import streamlit as st
from chains import (
    get_specific_temple_info,
    get_temples_by_location,
    get_temples_by_era,
    get_temples_by_deity
)

st.set_page_config(page_title="TempleGPT - Tamil Nadu Temples", layout="wide")
st.title("TempleGPT: Explore Tamil Nadu's Sacred Temples")
st.markdown("---")

# Chat prompt query
st.header("🔍 Ask a Question About a Temple")
user_input = st.text_input("Enter your question:", "Who built Madurai Meenakshi Amman Temple?")
if st.button("Search Temple Info"):
    response = get_specific_temple_info(user_input)
    if response:
        st.subheader(response["temple_name"])
        st.image(response.get("image_url", f"https://source.unsplash.com/600x400/?{response['temple_name'].replace(' ', '+')}+temple"), use_column_width=True)
        st.markdown(f"**Location**: {response['location']}")
        st.markdown(f"**Deity**: {response['deity']}")
        st.markdown(f"**Mythology**: {response['mythology']}")
        st.markdown("**Architecture Details:**")
        arch = response['architecture']
        st.markdown(f"- Style: {arch.get('style', '-')}")
        st.markdown(f"- Era: {arch.get('era', '-')}")
        st.markdown(f"- Materials: {arch.get('materials', '-')}")
        st.markdown(f"- Features: {arch.get('features', '-')}")
    else:
        st.warning("Temple information not found. Please rephrase your query.")

st.markdown("---")

# 🧭 Sidebar filters
with st.sidebar:
    st.header("📍 Explore Temples by Location")
    all_temples_by_location = get_temples_by_location()
    location_list = sorted(all_temples_by_location.keys())
    selected_location = st.selectbox("Choose a location", location_list)
    if selected_location:
        for temple in all_temples_by_location[selected_location]:
            st.text(f"{temple['temple_name']}")
            st.markdown(f"• Deity: {temple['deity']}")
            st.markdown(f"• Era: {temple['architecture'].get('era', '-')}")
            st.markdown("---")

    st.header("🏛️ Explore Temples by Era")
    all_temples_by_era = get_temples_by_era()
    era_list = sorted(all_temples_by_era.keys())
    selected_era = st.selectbox("Choose an era", era_list)
    if selected_era:
        for temple in all_temples_by_era[selected_era]:
            st.text(f"{temple['temple_name']}")
            st.markdown(f"• Location: {temple['location']}")
            st.markdown(f"• Deity: {temple['deity']}")
            st.markdown("---")

    st.header("🕉️ Explore Temples by Deity")
    all_temples_by_deity = get_temples_by_deity()
    deity_list = sorted(all_temples_by_deity.keys())
    selected_deity = st.selectbox("Choose a deity", deity_list)
    if selected_deity:
        for temple in all_temples_by_deity[selected_deity]:
            st.text(f"{temple['temple_name']}")
            st.markdown(f"• Location: {temple['location']}")
            st.markdown(f"• Era: {temple['architecture'].get('era', '-')}")
            st.markdown("---")
