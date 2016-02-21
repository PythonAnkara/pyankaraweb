from .models import *
import urllib.parse
import urllib.request
import json
import os
from django.conf import settings
import urllib, hashlib
import tweepy


class SiteCodes:
    def __init__(self):
        pass

    def get_sliders(self):
        slides = Slider.objects.all()
        return slides

    def get_post_data(self, postid):
        posts = Post.objects.filter(id=postid)
        if posts is not None:
            return posts[0]

    def get_posts(self, category_slug=None):
        posts = Post.objects.filter(categories__slug=category_slug)
        return posts

    def get_news(self):
        news = Post.objects.filter(categories__slug="haber")
        return news

    def get_all_posts(self):
        blogs = Post.objects.all()
        return blogs

    def get_last_news(self):
        news = Post.objects.filter(categories__slug="haber").order_by("-pub_datetime")
        return news[:10]

    def get_youtube_videos(self):
        apikey = settings.YOUTUBE_API_KEY
        channelid = settings.YOUTUBE_CHANNEL_ID
        url = "https://www.googleapis.com/youtube/v3/search?part=snippet,id&order=date&maxResults=50&channelId=%s&key=%s" % (channelid, apikey)
        response = urllib.request.urlopen(url)
        jsondata = response.read()
        data = json.loads(jsondata.decode('utf-8'))
        ret = []
        for i in data['items']:
            if i['id']['kind'] != 'youtube#video':
                continue
            dg = {
                'videoid': i['id']['videoId'],
                'title': i['snippet']['title'],
                'description': i['snippet']['description'],
                'thumbnails': {
                    'small': i['snippet']['thumbnails']['default']['url'],
                    'medium': i['snippet']['thumbnails']['medium']['url']
                },
                'pubdate': i['snippet']['publishedAt']
            }
            ret.append(dg.copy())
        return ret[0], ret[1:]

    def get_pictures(self):
        return os.listdir("{base}/media/pictures".format(base=settings.BASE_DIR))


    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_facebook_like_count(self):
        access_token = settings.FACEBOOK_ACCESS_TOKEN
        url = "https://graph.facebook.com/v2.5/pythonankara?fields=id,name,likes&access_token=" + access_token
        response = urllib.request.urlopen(url)
        jsondata = response.read()
        data = json.loads(jsondata.decode('utf-8'))
        return int(data["likes"])

    def get_facebook_photos(self):
        access_token = settings.FACEBOOK_ACCESS_TOKEN
        url = "https://graph.facebook.com/v2.5/pythonankara/photos/?type=uploaded&fields=source,name&limit=10&access_token=" + access_token
        response = urllib.request.urlopen(url)
        jsondata = response.read()
        data = json.loads(jsondata.decode('utf-8'))
        return data['data']


    def get_user_avatar(self, email, id):
        # import code for encoding urls and generating md5 hashes

        # Set your variables here
        default = "http://pyankara.org/{}.jpg".format(str(id))
        size = 40

        # construct the url
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
        return gravatar_url

    def get_tweets(self):
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET_KEY)
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN_KEY, settings.TWITTER_ACCESS_TOKEN_SECRET_KEY)
        try:
            api = tweepy.API(auth)
            public_tweets = api.user_timeline(screen_name='ThePSF', count=3)
            return public_tweets
        except Exception as e:
            return []
        #for tweet in public_tweets:
        #    print(type(tweet.created_at))

    def get_paging(self, sf, maxsf):
        oncevarmi = False
        sonravarmi = False
        mon = 0
        msn = 0
        mh = (sf % 4)
        if mh == 0 : mh = 4
        mbas = (int(((sf - mh) / 4)) * 4) + 1
        if mbas > 1:
            oncevarmi = True
            mon = mbas - mh
        mson = mbas + 4
        if mson < maxsf:
            sonravarmi = True
            msn = mson
        return (oncevarmi, sonravarmi, mbas, mson, mon, msn)


class AdminCodes:
    def __init__(self):
        pass
