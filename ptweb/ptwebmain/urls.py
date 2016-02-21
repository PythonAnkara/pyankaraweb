from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^blog/$', views.blog, name="blog"),
    url(r'^kategori/(.+)/$', views.kategori, name="kategori"),
    url(r'^haberler/$', views.haber, name="haber"),
    url(r'^videolar/$', views.video, name="video"),
    url(r'^yazarlar/$', views.yazarlar, name="yazarlar"),
    url(r'^etkinlikler/$', views.etkinlik, name="etkinlik"),
    url(r'^iletisim/$', views.iletisim, name="iletisim"),
    url(r'^messagepost/(?P<postid>[0-9]+)/(?P<slug>.+)$', views.messagepost, name="messagepost"),
    url(r'^arama/$', views.arama, name="arama"),
    url(r'^tags/(?P<tagid>[0-9]+)/(?P<slug>.+)$', views.tags, name="tags"),
    url(r'^(?P<slug>.+)$', views.post, name="post"),
]
