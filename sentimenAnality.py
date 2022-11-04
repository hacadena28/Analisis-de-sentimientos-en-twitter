from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia= SentimentIntensityAnalyzer()
def sentimiento(frase):
    resultado = sia.polarity_scores(frase)

    return resultado["compound"]

