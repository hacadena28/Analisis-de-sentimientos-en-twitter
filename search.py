from ast import Str
from cmath import pi
from distutils.command.config import config
from http import client
from re import I, U
import re
from urllib import response
import tweepy
import json
import config
import sentimenAnality
import pandas as pd


cliente = tweepy.Client(bearer_token=config.BEARER_TOKEN)
twitters = []
query = "USA -is:retweet"
def getTotal():
    volumen = cliente.get_recent_tweets_count(query=query)
    return volumen
def getquery():
    q = query.split("-")
    return q[0]
"""volumen = cliente.get_recent_tweets_count(query=query)
for data in volumen.data:
    # Imprime la cantidad de tweet por hora y por dia
    #print(data["start"])
    #print(data["end"])
    print("tweet por hora" )
    print(data["tweet_count"])
    print(" ")
print("Tweet totales")
print(volumen.meta["total_tweet_count"])
"""
def getTweet():
    respuesta = cliente.search_recent_tweets(query=query, max_results=10, tweet_fields=["lang"],
                                             user_fields=["profile_image_url"], expansions=["author_id"])
    return respuesta

respuesta = cliente.search_recent_tweets(query=query, max_results=10, tweet_fields=["lang"],
                                         user_fields=["profile_image_url"], expansions=["author_id"])
usuarios = {u["id"]: u for u in respuesta.includes["users"]}

for tweet in respuesta.data:
    if usuarios[tweet.author_id]:
        usuario = usuarios[tweet.author_id]
        print("id:")
        print(tweet.id)
        print("userName:")
        print(usuario.username)
        print("FotoDePErfil:")
        print(usuario.profile_image_url)
        print("Texto:")
        print(tweet.text)
        print("ID Autor: ")
        print(tweet.author_id)
        print("Idioma")
        print(tweet.lang)

        print("Senmtimiento: ")
        if tweet.lang == "en":
            print(sentimenAnality.sentimiento(tweet.text))
        else:
            if tweet.lang == "es":
              #  print(sentimenAnalitySpanish.sentimiento(tweet.text))
              print(0)

            else:
                print(0)


###
# d1 = respuesta.data
# print(str(d1[0]))
# print(str(d1[1]))
# print(str(d1[2])#)

# print("------------------------------")
# datas = json.dumps(str(respuesta.data)#)

# datas = datas.split("[")
# print(datas)
# datas = datas[1].split("]")
# print(datas)
# datas = datas[0].replace("]", "")
# print(datas#)

# datos2 = datas.split(">,"#)

# i = 0
# for a in datos2:
#    datos2[i] = datos2[i].replace("<", "")
#    datos2[i] = datos2[i].replace(">", "")
#    datos2[i] = datos2[i].split("text=")
#    datos2[i] = datos2[i][0].split("Tweet id=")[1]
#    twitter = Twitter(datos2[i], str(d1[i]))
#    twitters.append(twitter)
#    a = twitters[i]
#    print(a.tweet_id, a.text)
#    i = i + 1
###
###
###
###
