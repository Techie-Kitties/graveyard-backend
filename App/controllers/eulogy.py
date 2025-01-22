import google.generativeai as genai

genai.configure(api_key="")
def generate_eulogy(name, birth_date, death_date, relationships, occupation, personality_traits, hobbies, accomplishments, anecdotes, tone):
    prompt = f"""
    Compose a heartfelt and celebratory eulogy for {name}, who was born on {birth_date} and passed away on {death_date}.
    They are remembered by their {relationships}.
    {name} was known for being {personality_traits}. They worked as a {occupation} and some of their hobbies and interests include {hobbies}. Some of their great accomplishments was {accomplishments}.
    We want this eulogy to focus on the joy of {name}'s life and their positive impact on others. Incorporate any of the anecdotes provided.
    Anecdotes: {anecdotes}
    Use a {tone} tone.
    """

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

name = "John Doe"
birth_date = "January 1, 1950"
death_date = "December 25, 2023"
relationships = "spouse, two children, three grandchildren"
occupation = "Teacher"
personality_traits = "kind, humorous, and patient"
hobbies = "reading, hiking, and playing chess"
accomplishments = "Teaching award"
anecdotes = "He always had a joke ready to cheer people up."
tone = "celebratory"

eulogy_text = generate_eulogy(name, birth_date, death_date, relationships, occupation, personality_traits, hobbies, accomplishments, anecdotes, tone)
print(eulogy_text)