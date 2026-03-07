#python -m pip install google-genai
def short(character, setting, choice):
    client = genai.Client(api_key="AIzaSyD2gUJiANyaJUoRmk6Am-JGZbbEY2z9D_s")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= "This is the character in the life simulation game: " + character + "; This is a short summary of what happened before: " + setting + "; and in this life simulation game, this is the option chosen: " + choice + "; please extend the short summary with one extra line around 10 words breifly, you only have to reply one sentence, so to summarise what happened in this stage like describing what are they gonna do next, also whenever you tryikng to refer to the character, use You, like sayihng to them, but use less 'you', Also dun use fancy words, keep it simple. As this is a summary for them to check what happened before."
    )
    return response.text

def summary(shortSummaries):
    return None

