from django import template
from pyquery import PyQuery as pq
import datetime

register = template.Library()

@register.filter(name='description')
def description(obj, attribute):
    obj = "<html>" + obj + "</html>"
    d = pq(obj)
    plist = list(d('p'))
    p = ""
    for i in plist:
        if len(pq(i).text().strip().split(' ')) >= attribute:
            pi = pq(i).text()
            psyc = 0
            for j in pi.strip().split(' '):
                if psyc >= attribute:
                    break
                p += j + " "
                psyc += 1
            break
    return p

@register.filter(name='modhesapla')
def modhesapla(obj, attribute):
    return obj % attribute
