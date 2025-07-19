import json

# Load JSON data once
with open("temples.json", "r", encoding="utf-8") as file:
    temple_data = json.load(file)

# Get info by question-based query (simplified)
def get_specific_temple_info(query):
    for temple in temple_data:
        if temple["temple_name"].lower() in query.lower():
            return {
                "temple_name": temple["temple_name"],
                "location": temple["location"],
                "deity": temple["deity"],
                "mythology": temple["mythology"],
                "architecture": temple["architecture"],
                "image_url": f"https://source.unsplash.com/600x400/?{temple['temple_name'].replace(' ', '+')}+temple"
            }
    return None

def get_temples_by_location():
    result = {}
    for temple in temple_data:
        loc = temple["location"]
        result.setdefault(loc, []).append(temple)
    return result

def get_temples_by_era():
    result = {}
    for temple in temple_data:
        era = temple["architecture"].get("era", "Unknown")
        result.setdefault(era, []).append(temple)
    return result

def get_temples_by_deity():
    result = {}
    for temple in temple_data:
        deity = temple["deity"]
        result.setdefault(deity, []).append(temple)
    return result
