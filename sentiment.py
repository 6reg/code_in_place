import nltk.sentiment
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()

def main():
    while True:
        user_text = input('? ')
        score = get_sentiment(user_text)
        reaction = get_reaction(score)
        print(reaction)
        print(score)
        print('')

def get_reaction(score):
    """
    Parameter score: a float between -1 and +1
    Return: an emoji as a string
    """
    if score > 0.5:
        return "Happy"
    if score > 0:
        return "Okay"
    if score == 0:
        return "Meh"
    if score < -0.5:
        return "Upset"
    if score < 0:
        return "Mad"
main()
