#download: python -m pip install google-genai
from google import genai
client = genai.Client(api_key="AIzaSyAtoTehAB8OhFQEFIxpxMHVAHLMQiXn6-0")
def short(character, setting, choice):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= "This is the character in the life simulation game: " + character + "; This is a short summary of what happened before: "
         + setting + "; and in this life simulation game, this is the option chosen: " + choice + "; please extend the short summary with one extra line around 10 words breifly, you must only have to reply one sentence, so to summarise what happened in this stage like describing what are they gonna do next, also whenever you tryikng to refer to the character, use You, like sayihng to them, but use less 'you', Also dun use fancy words, keep it simple. As this is a summary for them to check what happened before."
    )
    return response.text

def summary(shortSummaries):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = "This is a text based game where user can pick to change their gender, background, education, career path, relationship, etc. " \
        "according to what is happening at each stage so to get the most out of their life. " \
        "And each time a choice is picked, the stage is recorded, and the gender they were in is recorded as well in the format of " \
        "'gender: storyline(what they did)', I will be providing the tracks below, and please write me a short summary with an interpretation of the story, " \
        "focusing on how the gender equality causes the main character to gain more or less, and how the society treat people in LGBTQ differently. " \
        "relate the story to something like for example, girls are more talented in artistic/music related, boys has more potential in men have higher salaries and women are treated unfairly in career, return me the summary and make this sounds meaningful around 150 words"
    )
    

