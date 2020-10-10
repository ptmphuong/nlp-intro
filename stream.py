from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

ckey="put-your-key-here"
csecret="put-your-key-here"
atoken="put-your-key-here"
asecret="put-your-key-here"

# accesstoken = "798767325772029952-lcpNI5IOTozzniYRXblWHcfNYYUJoTa"
# accesstokensecret = "fqWAC8kGtzU1CBrxAcwtdd68VADpwZFf5Y9ivsi00qmkb"

class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value = s.sentiment(tweet)
        print(tweet)
        print(sentiment_value)


        output = open("out.txt","a")
        output.write(sentiment_value)
        output.write('\n')
        output.close()

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["election"])