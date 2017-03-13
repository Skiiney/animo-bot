from connection import Connection
import tweepy

auth = tweepy.OAuthHandler(Connection.consumer_key, Connection.consumer_secret)
auth.set_access_token(Connection.token_key,Connection.token_secret)
