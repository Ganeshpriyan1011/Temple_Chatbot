import json
import os
import difflib

# Load temple data
with open("temple.json", "r", encoding="utf-8") as file:
    temples = json.load(file)

def get_temples_by_location(location_filter=None):
    if location_filter:
        return [t["temple_name"] for t in temples if location_filter.lower() in t["location"].lower()]
    return list(set(t["location"] for t in temples))

def get_temples_by_dynasty(dynasty_filter=None):
    if dynasty_filter:
        return [t["temple_name"] for t in temples if dynasty_filter.lower() in t["architecture"]["era"].lower()]
    return list(set(t["architecture"]["era"] for t in temples))

def get_temples_by_deity(deity_filter=None):
    if deity_filter:
        return [t["temple_name"] for t in temples if deity_filter.lower() in t["deity"].lower()]
    return list(set(t["deity"] for t in temples))

def get_specific_temple_info(query):
    query_lower = query.lower()
    
    best_match = None
    highest_ratio = 0.0

    for temple in temples:
        name = temple["temple_name"].lower()
        location = temple["location"].lower()
        combined = f"{name} {location}"

        # Find best approximate match
        match_score = difflib.SequenceMatcher(None, combined, query_lower).ratio()
        if match_score > highest_ratio:
            highest_ratio = match_score
            best_match = temple

    if best_match and highest_ratio > 0.4:
        architecture = best_match["architecture"]
        return {
            "answer": (
                f"**Temple Name**: {best_match['temple_name']}\n\n"
                f"**Location**: {best_match['location']}\n\n"
                f"**Deity**: {best_match['deity']}\n\n"
                f"**Mythology**: {best_match['mythology']}\n\n"
                f"**Architecture**:\n"
                f"- Style: {architecture['style']}\n"
                f"- Era/Dynasty: {architecture['era']}\n"
                f"- Materials: {architecture['materials']}\n"
                f"- Features: {architecture['features']}"
            ),
            "image_url": generate_image_url(best_match["image_prompt"])
        }
    else:
        return {"answer": "Sorry, I couldn't find any matching temple in the database."}

def generate_image_url(prompt):
    # Use a placeholder or stable diffusion endpoint later
    return f"https://dummyimage.com/600x400/cccccc/000000&text={'+'.join(prompt.split())}"
