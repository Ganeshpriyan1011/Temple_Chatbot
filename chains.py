import json
import os

with open("temple.json", "r", encoding="utf-8") as file:
    temples = json.load(file)

def generate_answer(query):
    query_lower = query.lower()
    for temple in temples:
        name = temple["temple_name"].lower()
        if name.split()[0] in query_lower or name in query_lower:
            if "who built" in query_lower or "built" in query_lower:
                return f"{temple['temple_name']} was built during the {temple['architecture']['era']} era."
            elif "architecture" in query_lower:
                arch = temple['architecture']
                return f"The architecture of {temple['temple_name']} is {arch['style']} style using {arch['materials']}. Key features include: {arch['features']}."
            elif "where" in query_lower or "location" in query_lower:
                return f"{temple['temple_name']} is located in {temple['location']}."
            elif "mythology" in query_lower or "story" in query_lower:
                return f"Here is the mythology of {temple['temple_name']}: {temple['mythology']}"
            else:
                return f"{temple['temple_name']}:\nLocation: {temple['location']}\nEra: {temple['architecture']['era']}\nMythology: {temple['mythology']}"
    return "Sorry, I couldn't find any matching temple in the database."
