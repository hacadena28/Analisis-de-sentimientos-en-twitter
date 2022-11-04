from classifier import SentimentClassifier
clf = SentimentClassifier()
frase = "esta horrible la pelicula"


resultado = clf.predict(frase)
print(resultado)
#def sentimiento(frase):
   # resultado = clf.predict(frase)

   # return resultado

#print(sentimiento)