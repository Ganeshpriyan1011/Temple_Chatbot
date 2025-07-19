import json

# Load all temple data once
with open("temple.json", "r", encoding="utf-8") as f:
    temples = json.load(f)

def get_specific_temple_info(query):
    query = query.lower()
    for temple in temples:
        name = temple['temple_name'].lower()
        if name in query or name.split()[0] in query:
            response = ""
            if "who built" in query or "built" in query:
                response = f"{temple['temple_name']} was built during the {temple['architecture']['era']} by the {temple['architecture']['dynasty']} dynasty."
            elif "architecture" in query:
                arch = temple['architecture']
                response = f"The architecture of {temple['temple_name']} is {arch['style']} style using {arch['materials']}. Features: {arch['features']}."
            elif "mythology" in query or "legend" in query or "story" in query:
                response = f"Mythology of {temple['temple_name']}: {temple['mythology']}"
            elif "where" in query or "location" in query:
                response = f"{temple['temple_name']} is located in {temple['location']}."
            else:
                response = f"{temple['temple_name']}:\nLocation: {temple['location']}\nDynasty: {temple['architecture']['dynasty']}\nEra: {temple['architecture']['era']}\nMythology: {temple['mythology']}"
            return response
    return "Sorry, I couldn't find any matching temple in the database."

def get_temples_by_location(location):
    if location == "All":
        return temples
    return [t for t in temples if location.lower() in t['location'].lower()]

def get_temples_by_dynasty(dynasty):
    if dynasty == "All":
        return temples
    return [t for t in temples if dynasty.lower() in t['architecture']['dynasty'].lower()]
