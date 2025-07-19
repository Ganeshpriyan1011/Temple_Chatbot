import json

with open("temple.json", "r", encoding="utf-8") as f:
    temples = json.load(f)

# Get all unique locations
def get_temples_by_location(selected=None):
    locations = sorted(set(t["location"] for t in temples))
    if selected:
        return [t["temple_name"] for t in temples if selected in t["location"]]
    return ["Select"] + locations

# Get all unique dynasties
def get_temples_by_dynasty(selected=None):
    dynasties = sorted(set(t.get("architecture", {}).get("dynasty", "Unknown") for t in temples))
    if selected:
        return [t["temple_name"] for t in temples if selected in t.get("architecture", {}).get("dynasty", "")]
    return ["Select"] + dynasties

# Main Query Handler
def get_specific_temple_info(query):
    query = query.lower()
    matched_temple = None

    for temple in temples:
        if temple["temple_name"].lower() in query:
            matched_temple = temple
            break

    if not matched_temple:
        return {"answer": "Sorry, I couldn't find any matching temple in the database."}

    answer = "Please ask about location, deity, mythology, architecture, or who built the temple."

    if "location" in query:
        answer = f"{matched_temple['temple_name']} is located in {matched_temple.get('location', 'location info not available')}."
    elif "deity" in query or "god" in query:
        answer = f"The presiding deity is {matched_temple.get('deity', 'not specified')}."
    elif "mythology" in query or "legend" in query:
        answer = matched_temple.get("mythology", "Mythology not available.")
    elif "architecture" in query or "style" in query:
        arch = matched_temple.get("architecture", {})
        answer = (
            f"Architecture of {matched_temple['temple_name']}:\n"
            f"- Style: {arch.get('style', 'N/A')}\n"
            f"- Era: {arch.get('era', 'N/A')}\n"
            f"- Materials: {arch.get('materials', 'N/A')}\n"
            f"- Features: {arch.get('features', 'N/A')}"
        )
    elif "who built" in query or "built by" in query or "dynasty" in query:
        answer = f"This temple was built by the {matched_temple.get('architecture', {}).get('dynasty', 'Unknown Dynasty')} dynasty."

    # Add image if available
    return {
        "answer": answer,
        "image_url": matched_temple.get("image_prompt", None)
    }
