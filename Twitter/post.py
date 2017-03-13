from connection import Connection
from ImageTreatment.Images import ImageInfo
import tweepy

auth = tweepy.OAuthHandler(Connection.consumer_key, Connection.consumer_secret)
auth.set_access_token(Connection.token_key,Connection.token_secret)

api = tweepy.API(auth)

api.update_with_media('1.jpg','teste')

print(ImageInfo.GetImageRes('1.jpg'))
