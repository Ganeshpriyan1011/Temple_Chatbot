import json

# Load the temple JSON dataset
with open("temple.json", "r", encoding="utf-8") as file:
    temple_data = json.load(file)

# Add image URL dynamically if not already present
def add_image_url(temple):
    if "image_url" not in temple or not temple["image_url"]:
        temple["image_url"] = f"https://source.unsplash.com/600x400/?{temple['temple_name'].replace(' ', '+')}+temple"
    return temple

# Prompt-based search
def get_specific_temple_info(question):
    for temple in temple_data:
        if temple['temple_name'].lower() in question.lower():
            return add_image_url(temple)
    return None

# Location-based
def get_temples_by_location():
    location_dict = {}
    for temple in temple_data:
        location = temple['location']
        temple = add_image_url(temple)
        location_dict.setdefault(location, []).append(temple)
    return location_dict

# Era-based
def get_temples_by_era():
    era_dict = {}
    for temple in temple_data:
        era = temple['architecture'].get('era', 'Unknown')
        temple = add_image_url(temple)
        era_dict.setdefault(era, []).append(temple)
    return era_dict

# Deity-based
def get_temples_by_deity():
    deity_dict = {}
    for temple in temple_data:
        deity = temple['deity']
        temple = add_image_url(temple)
        deity_dict.setdefault(deity, []).append(temple)
    return deity_dict
