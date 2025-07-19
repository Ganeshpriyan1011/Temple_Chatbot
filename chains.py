import json
import difflib

# Load temple data
with open("temple.json", "r", encoding="utf-8") as f:
    temple_data = json.load(f)

def get_specific_temple_info(query):
    query = query.lower()
    best_match = None
    best_score = 0

    for temple in temple_data:
        score = 0
        combined_text = " ".join([
            temple["temple_name"],
            temple["location"],
            temple["deity"],
            temple["mythology"],
            temple["architecture"]["style"],
            temple["architecture"]["era"],
            temple["architecture"]["materials"],
            temple["architecture"]["features"]
        ]).lower()

        matches = difflib.SequenceMatcher(None, query, combined_text).ratio()
        if matches > best_score:
            best_score = matches
            best_match = temple

    if best_score > 0.3:
        answer = f"**Temple Name:** {best_match['temple_name']}\n\n"
        answer += f"**Location:** {best_match['location']}\n"
        answer += f"**Deity:** {best_match['deity']}\n"
        answer += f"**Mythology:** {best_match['mythology']}\n\n"
        answer += "**Architecture:**\n"
        answer += f"- Style: {best_match['architecture']['style']}\n"
        answer += f"- Era: {best_match['architecture']['era']}\n"
        answer += f"- Materials: {best_match['architecture']['materials']}\n"
        answer += f"- Features: {best_match['architecture']['features']}\n"

        return {
            "answer": answer,
            "image_url": None  # You can add image generation later
        }
    else:
        return {
            "answer": "Sorry, I couldn't find any matching temple in the database.",
            "image_url": None
        }

def get_temples_by_location(selected_location=None):
    if not selected_location:
        locations = sorted(list(set(t["location"] for t in temple_data)))
        return locations
    return [t["temple_name"] for t in temple_data if t["location"] == selected_location]

def get_temples_by_dynasty(selected_dynasty=None):
    if not selected_dynasty:
        eras = sorted(list(set(t["architecture"]["era"] for t in temple_data)))
        return eras
    return [t["temple_name"] for t in temple_data if t["architecture"]["era"] == selected_dynasty]

def get_temples_by_deity(selected_deity=None):
    if not selected_deity:
        deities = sorted(list(set(t["deity"] for t in temple_data)))
        return deities
    return [t["temple_name"] for t in temple_data if t["deity"] == selected_deity]
