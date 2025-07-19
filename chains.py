import json

# Load the data once
with open("temple.json", "r", encoding="utf-8") as file:
    temples = json.load(file)

# Extract unique values for assessments
def get_all_temples():
    return temples

def get_all_locations():
    return sorted(set(t["location"] for t in temples))

def get_all_eras():
    return sorted(set(t["architecture"]["era"] for t in temples))

def get_all_deities():
    return sorted(set(t["deity"] for t in temples))

# Filter temples by specific criteria
def get_temples_by_location(location):
    return [t["temple_name"] for t in temples if t["location"] == location]

def get_temples_by_era(era):
    return [t["temple_name"] for t in temples if t["architecture"]["era"] == era]

def get_temples_by_deity(deity):
    return [t["temple_name"] for t in temples if t["deity"] == deity]

# Main query function
def get_specific_temple_info(query):
    for temple in temples:
        if query.lower() in temple["temple_name"].lower() or query.lower() in temple.get("mythology", "").lower():
            return {
                "answer": f"**{temple['temple_name']}**, located in *{temple['location']}*, is dedicated to **{temple['deity']}**. It was built during the **{temple['architecture']['era']}** era in **{temple['architecture']['style']}** style. Key features include: {temple['architecture']['features']}. Mythology: {temple['mythology']}",
                "image_url": generate_image_url(temple["image_prompt"])
            }
    return {"answer": "Sorry, I couldn't find any matching temple in the database."}

# Dummy image function (you can replace this with real image generation later)
def generate_image_url(prompt):
    return "https://via.placeholder.com/600x400.png?text=" + prompt.replace(" ", "+")
