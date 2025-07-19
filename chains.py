import json

# Load data from JSON
def load_temple_data():
    with open("temple_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


# Get unique temple locations
def get_temples_by_location(data):
    locations = sorted(list(set([t["location"]["district"] for t in data if "location" in t and "district" in t["location"]])))
    return locations


# Get unique temple dynasties (based on architecture era)
def get_temples_by_dynasty(data):
    dynasties = sorted(list(set([t["architecture"]["era"] for t in data if "architecture" in t and "era" in t["architecture"]])))
    return dynasties


# Filter temples by a selected location
def filter_temples_by_location(data, selected_location):
    return [t["name"] for t in data if t.get("location", {}).get("district") == selected_location]


# Filter temples by a selected dynasty (era)
def filter_temples_by_dynasty(data, selected_dynasty):
    return [t["name"] for t in data if t.get("architecture", {}).get("era") == selected_dynasty]


# Process user queries
def get_specific_temple_info(query):
    # You can replace this with LangChain or vector search logic later
    if "meenakshi" in query.lower():
        return {
            "answer": "The Meenakshi Temple was built by the Pandya dynasty and is located in Madurai. It is renowned for its Dravidian architecture and mythological association with Goddess Meenakshi and Lord Sundareswarar.",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Meenakshi_Amman_Temple.jpg"
        }
    else:
        return {
            "answer": "Sorry, I couldn't find any matching temple in the database.",
            "image_url": None
        }
