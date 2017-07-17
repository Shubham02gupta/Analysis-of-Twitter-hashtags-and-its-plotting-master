import urllib
import urllib.request
from bs4 import BeautifulSoup


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


ckey="ESAHJglSve3sybJTGt7d3GSnN"
csecret="jRzIueSYb8uH9pgCir6yImsi0jjovymRFrQRZzWuJnSTeslBSi"
atoken="4849454360-qxhs8dJST6v1fiC7a3OFwxa6UY6OYwtGZ10w1LB"
asecret="mWqwshQTZoO7123yaxibvevRwv4ug5PGDnMT9MaWmV95V"


theurl = "http://trends24.in/india/~cloud"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage,"html.parser")

trend_list = []
for item in soup.findAll('ol', {"class":"page-content__tagcloud__list"}):
    for i in item.findAll('a'):
        #i = i.text.strip()
        trend_list.append(i.text.strip())


class listener(StreamListener):
    def on_data(self, data):
        print(data)
        saveFile = open('twitDB.csv', 'a')
        saveFile.write(data)
        saveFile.close()
        return(True)

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=trend_list)