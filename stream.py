from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

ckey="ASfenRJcyi4b8r9NjPVzFex8m"
csecret="WMYSrpfA82DQHNpiTPB6XFkjZgMxFphG1hu4wXKLIoZCZm3aW1"
atoken="798767325772029952-lcpNI5IOTozzniYRXblWHcfNYYUJoTa"
asecret="fqWAC8kGtzU1CBrxAcwtdd68VADpwZFf5Y9ivsi00qmkb"

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