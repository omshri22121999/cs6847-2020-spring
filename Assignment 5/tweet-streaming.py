'''
Tweet Streaming to Kafka Producer

Run the command using "python tweet-streaming.py" 

Make sure you create a topic called "newyork" before running the code
''' 

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, KafkaClient

access_token = "<fill access_token>"
access_token_secret =  "<fill access_token_secret>"
consumer_key =  "<fill consumer_key>"
consumer_secret =  "<fill consumer_secret>"

class StdOutListener(StreamListener):
    def on_data(self, data):
        # producer.send("newyork", data.encode('utf-8'))
        producer.send("california", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient()
producer = KafkaProducer()
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
# stream.filter(locations=[-79.762152,40.496103,-71.856214,45.01585]) # New York
stream.filter(locations=[-124.409591,32.534156,-114.131211,42.009518]) # California
producer.flush()
producer.close()
