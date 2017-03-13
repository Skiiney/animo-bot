from connection import Connection
import sys
sys.path.insert(0, '/home/cap/Documentos/animo-bot/ImageTreatment/')
from Images import ImageInfo
import tweepy
import os

auth = tweepy.OAuthHandler(Connection.consumer_key, Connection.consumer_secret)
auth.set_access_token(Connection.token_key,Connection.token_secret)

api = tweepy.API(auth)
filename = str(os.path.splitext(os.path.basename(r'/home/cap/Documentos/animo-bot/Twitter/Andrea del Sarto - Charity.jpg'))[0])
artistName = filename.split('-')[0]
paitingName = filename.split('-')[1]


#para postar com imagem
#api.update_with_media('coloqueimagem.jgp', 'conteudo do tweet')
