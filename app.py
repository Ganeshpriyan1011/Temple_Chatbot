import streamlit as st
from chains import get_specific_temple_info, get_temples_by_location, get_temples_by_era, get_temples_by_deity

st.set_page_config(page_title="TempleGPT - Tamil Nadu Temples", layout="wide")
st.title("TempleGPT: Explore Tamil Nadu's Sacred Temples")

st.markdown("---")

# Prompt-based query
st.header("🔍 Ask a Question About a Temple")
user_input = st.text_input("Enter your question:", "Who built Madurai Meenakshi Amman Temple?")
if st.button("Search Temple Info"):
    response = get_specific_temple_info(user_input)
    if response:
        st.subheader(response["temple_name"])
        st.image(f"https://source.unsplash.com/600x400/?{response['temple_name'].replace(' ', '+')}+temple", use_column_width=True)
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

# Location-based assessment
st.header("📍 Explore by Location")
all_temples_by_location = get_temples_by_location()
selected_location = st.selectbox("Select a location:", sorted(list(all_temples_by_location.keys())))
if selected_location:
    for temple in all_temples_by_location[selected_location]:
        st.subheader(temple["temple_name"])
        st.image(f"https://source.unsplash.com/600x400/?{temple['temple_name'].replace(' ', '+')}+temple", use_column_width=True)
        st.markdown(f"**Deity**: {temple['deity']}")
        st.markdown(f"**Era**: {temple['architecture'].get('era', '-')}")
        st.markdown("---")

# Era-based assessment
st.header("🏛️ Explore by Era (Dynasty)")
all_temples_by_era = get_temples_by_era()
selected_era = st.selectbox("Select an era:", sorted(list(all_temples_by_era.keys())))
if selected_era:
    for temple in all_temples_by_era[selected_era]:
        st.subheader(temple["temple_name"])
        st.image(f"https://source.unsplash.com/600x400/?{temple['temple_name'].replace(' ', '+')}+temple", use_column_width=True)
        st.markdown(f"**Location**: {temple['location']}")
        st.markdown(f"**Deity**: {temple['deity']}")
        st.markdown("---")

# Deity-based assessment
st.header("🕉️ Explore by Deity")
all_temples_by_deity = get_temples_by_deity()
selected_deity = st.selectbox("Select a deity:", sorted(list(all_temples_by_deity.keys())))
if selected_deity:
    for temple in all_temples_by_deity[selected_deity]:
        st.subheader(temple["temple_name"])
        st.image(f"https://source.unsplash.com/600x400/?{temple['temple_name'].replace(' ', '+')}+temple", use_column_width=True)
        st.markdown(f"**Location**: {temple['location']}")
        st.markdown(f"**Era**: {temple['architecture'].get('era', '-')}")
        st.markdown("---")
