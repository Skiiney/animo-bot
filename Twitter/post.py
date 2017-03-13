from connection import Connection
from twitter import *
twitter = Twitter(
      auth=OAuth(Connection.token_key, Connection.token_secret, Connection.consumer_key, Connection.consumer_secret))
twitter.statuses.update(
    status="alo")
