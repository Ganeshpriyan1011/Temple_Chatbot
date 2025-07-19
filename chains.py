import json
import hashlib

# Load temple dataset
with open("temple.json", "r", encoding="utf-8") as file:
    temple_data = json.load(file)

# 🔧 Generate a consistent image URL per temple using hash
def get_image_url(temple_name):
    hash_sig = hashlib.md5(temple_name.encode()).hexdigest()
    clean_name = temple_name.lower().replace(" ", "+")
    return f"https://source.unsplash.com/600x400/?{clean_name}+temple&sig={hash_sig}"

# 📌 Temple Q&A
def get_specific_temple_info(query):
    for temple in temple_data:
        if temple["temple_name"].lower() in query.lower():
            return {
                "temple_name": temple["temple_name"],
                "location": temple["location"],
                "deity": temple["deity"],
                "mythology": temple["mythology"],
                "architecture": temple["architecture"],
                "image_url": get_image_url(temple["temple_name"])
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
