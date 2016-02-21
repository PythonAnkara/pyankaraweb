from .models import *
from django.db.models import Count
from .app_codes import *
from django.db.models.functions import Coalesce

def main_template(request):
    siteis = SiteCodes()
    b_news = Post.objects.filter(status=True, category__slug="haber")
    r_pupular_posts = Hit.objects.values("post__id", "post__title", "post__slug",
                                         "post__pub_datetime",
                                         "post__thumbn").annotate(dcount=Count("post__id")).order_by('-dcount')[:4]
    r_recent_posts = Post.objects.filter(status=True).order_by("-pub_datetime")[:4]
    r_recent_comments = Comment.objects.filter(status=True).order_by("-pub_datetime")[:4]
    r_facebook_like_count = siteis.get_facebook_like_count()
    #r_facebook_like_count = 271
    r_yeni_video = siteis.get_youtube_videos()
    #r_yeni_video = [""]
    r_pictures = siteis.get_facebook_photos()
    f_pictures = r_pictures[:8]
    f_tweets = siteis.get_tweets()
    return {
        'b_news': b_news,
        'r_pupular_posts': r_pupular_posts,
        'r_recent_posts': r_recent_posts,
        'r_facebook_like_count': r_facebook_like_count,
        'r_yeni_video': r_yeni_video[0],
        'r_pictures': r_pictures,
        'f_pictures': f_pictures,
        'f_tweets': f_tweets,
        'r_recent_comments': r_recent_comments
    }
