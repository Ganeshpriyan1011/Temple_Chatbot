import json

# Load temple dataset
with open("temples.json", "r", encoding="utf-8") as file:
    temple_data = json.load(file)

# 📌 Temple Q&A
def get_specific_temple_info(query):
    for temple in temple_data:
        if temple["temple_name"].lower() in query.lower():
            return {
                "temple_name": temple["temple_name"],
                "location": temple["location"],
                "deity": temple["deity"],
                "mythology": temple["mythology"],
                "architecture": temple["architecture"]
            }
    return None

# 📍 Group by location
def get_temples_by_location():
    result = {}
    for temple in temple_data:
        loc = temple["location"]
        result.setdefault(loc, []).append(temple)
    return result

# 🏛 Group by era
def get_temples_by_era():
    result = {}
    for temple in temple_data:
        era = temple["architecture"].get("era", "Unknown")
        result.setdefault(era, []).append(temple)
    return result

# 🙏 Group by deity
def get_temples_by_deity():
    result = {}
    for temple in temple_data:
        deity = temple["deity"]
        result.setdefault(deity, []).append(temple)
    return result
