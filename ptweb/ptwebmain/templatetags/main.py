from django import template
from pyquery import PyQuery as pq
import urllib, hashlib
import datetime
from ..models import *


register = template.Library()

@register.filter(name='description')
def description(obj, attribute):
    obj = "<html><head></head><body>" + obj + "</body></html>"
    d = pq(obj)
    plist = list(d('body'))
    p = ""
    kelimehavuz = []
    for i in plist:
        for k in pq(i).text().strip().split(' '):
            if len(kelimehavuz) < attribute:
                kelimehavuz.append(k.strip())
    return " ".join(kelimehavuz)

@register.filter(name='modhesapla')
def modhesapla(obj, attribute):
    return obj % attribute

@register.filter(name='avatargetir')
def avatargetir(email, size=200):
    if email.strip() == "":
        email = "info@pythonturkiye.com"
    default = ""

    # construct the url
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.encode("utf-8").lower()).hexdigest() + "?"
    gravatar_url += urllib.parse.urlencode({'d':default.encode("utf-8"), 's':str(size)})
    return gravatar_url

@register.filter(name='userposts')
def userposts(uname, sayimi=0):
    posts = Post.objects.filter(status=True, author__username=uname)
    if sayimi == 0:
        return posts
    return len(posts)

@register.filter(name='counter')
def counter(obj):
    return len(obj)

@register.filter(name='datediffr')
def datediffr(obj):
    now = datetime.datetime.now()
    lasttweetat =  obj + datetime.timedelta(hours=+2)
    c = now - lasttweetat
    snc = divmod(c.days * 86400 + c.seconds, 60)
    if snc[0] <= 1440:
        if snc[0] < 60:
            return "{} saniye önce" + str(snc[0])
        return "{} saat önce".format(str(int(snc[0]/60)))
    else:
        return obj

@register.filter(name='textsplit')
def textsplit(obj, size):
    if len(str(obj).split(' ')) > size:
        ret = " ".join(str(obj).split(' ')[:size])
        ret += " ..."
        return ret
    return obj

@register.filter(name='getcommentcounts')
def getcommentcounts(obj):
    return len(Comment.objects.filter(status=True, post__id=obj))
