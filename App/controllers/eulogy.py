import os

import google.generativeai as genai
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
config = os.path.join(PARENT_DIR, 'key.json')

with open(config, 'r') as file:
    config_data = json.load(file)

api_key = config_data.get('genai_api_key')
genai.configure(api_key=api_key)
def generate_eulogy(name, birth_date, death_date, relationships, occupation, personality_traits, hobbies, accomplishments, anecdotes, tone):
    prompt = f"""
    Compose a heartfelt and celebratory eulogy for {name}, who was born on {birth_date} and passed away on {death_date}.
    They are remembered by their {relationships}.
    {name} was known for being {personality_traits}. They worked as a {occupation} and some of their hobbies and interests include {hobbies}. Some of their great accomplishments was {accomplishments}.
    We want this eulogy to focus on the joy of {name}'s life and their positive impact on others. Incorporate any of the anecdotes provided.
    Anecdotes: {anecdotes}
    Use a {tone} tone. Make the response as long as possible for testing.
    """

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
# name = "John Doe"
# birth_date = "January 1, 1950"
# death_date = "December 25, 2023"
# relationships = "spouse, two children, three grandchildren"
# occupation = "Teacher"
# personality_traits = "kind, humorous, and patient"
# hobbies = "reading, hiking, and playing chess"
# accomplishments = "Teaching award"
# anecdotes = "He always had a joke ready to cheer people up."
# tone = "celebratory"
#
#
# eulogy_text = generate_eulogy(name, birth_date, death_date, relationships, occupation, personality_traits, hobbies, accomplishments, anecdotes, tone)
# print(eulogy_text)