from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Count
from django.db.models import Q
from .app_codes import *
from .models import *
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.db import transaction

# Create your views here.
def home(request):
    title = "Python Ankara | Ankara Python Sevdalıları"
    posts = Post.objects.filter(status=True)[:5]
    slides = Slider.objects.all().order_by("order", "-id")[:5]
    news = Post.objects.filter(status=True, category__slug="haber")
    pypost = Post.objects.filter(Q(status=True) & Q(category__slug="python"))[:2]
    djpost = Post.objects.filter(Q(status=True) & Q(category__slug="django"))[:2]
    events = Post.objects.filter(status=True, category__slug="etkinlik")[:5]
    subposts = [
        {"baslik": "Python", "kod": "python", "icerik": pypost},
        {"baslik": "Django", "kod": "django", "icerik": djpost}
    ]
    if posts:
        big_post = events[0]
    else:
        big_post = None
    return render_to_response("main/index.html", locals(), context_instance=RequestContext(request))


def blog(request):
    siteis = SiteCodes()
    title = "Python Ankara - Blog"
    sf = 1
    postcount = Post.objects.filter(status=True).count()
    maxsflm = 10
    maxsf = int(postcount/maxsflm)
    if maxsf * maxsflm < postcount:
        maxsf += 1
    if request.GET.get('sf') is not None:
        try:
            sf = int(request.GET.get('sf'))
            if sf < 1: sf = 1
        except Exception as e:
            sf = 1
    oncevarmi, sonravarmi, mbas, mson, mon, msn = siteis.get_paging(sf, maxsf)
    posts = Post.objects.filter(status=True)[((sf-1)*maxsflm):(sf*maxsflm)]
    return render_to_response("main/blog.html", locals(), context_instance=RequestContext(request))

def post(request, slug):
    siteis = SiteCodes()
    posts = Post.objects.filter(status=True, slug = slug)
    postdata = None
    if posts is not None:
        postdata = posts[0]
        postid = postdata.id
        aboutauthor = Author.objects.filter(user__username=postdata.author.username)
        otherposts = Post.objects.filter(Q(category__slug=postdata.category.slug) & ~Q(slug = postdata.slug))[:3]
        title = "Python Ankara | " + postdata.title
    ipaddress = siteis.get_client_ip(request)
    hitcontrol = Hit.objects.filter(ip=ipaddress, post__id=postid, datatype='read')
    hitscount = Hit.objects.filter(post__id=postid).count()
    comments = Comment.objects.filter(post__id=postid, status=True).order_by("-pub_datetime")
    if len(hitcontrol) == 0:
        b = Hit(ip=ipaddress, post_id=postid, datatype='read')
        b.save()



    return render_to_response("main/simpleblog.html", locals(), context_instance=RequestContext(request))

@csrf_protect
def messagepost(request, postid, slug):
    if request.method == 'POST':
        siteis = SiteCodes()
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        message = request.POST.get("message", "")
        ipaddress = siteis.get_client_ip(request)
        parentid = 0
        b = Comment(name=name, email=email, message=message, ipaddress=ipaddress,
                    parentid=parentid, post_id=postid)
        b.save()
        hitcontrol = Hit.objects.filter(email=email, post__id=postid, datatype='comment')
        if len(hitcontrol) == 0:
            for i in range(5):
                h = Hit(ip=ipaddress, post_id=postid, datatype='comment', email=email)
                h.save()
            transaction.commit()



    return redirect('post', slug=slug)



def kategori(request, slug):
    siteis = SiteCodes()
    sf = 1
    postcount = Post.objects.filter(status=True, category__slug=slug).count()
    maxsflm = 10
    maxsf = int(postcount/maxsflm)
    if maxsf * maxsflm < postcount:
        maxsf += 1
    if request.GET.get('sf') is not None:
        try:
            sf = int(request.GET.get('sf'))
            if sf < 1: sf = 1
        except Exception as e:
            sf = 1
    oncevarmi, sonravarmi, mbas, mson, mon, msn = siteis.get_paging(sf, maxsf)
    posts = Post.objects.filter(status=True, category__slug=slug)[((sf-1)*maxsflm):(sf*maxsflm)]
    return render_to_response("main/kategori.html", locals(), context_instance=RequestContext(request))


def haber(request):
    title = "Python Ankara - Haberler"
    news = Post.objects.filter(status=True, category__slug="haber")
    return render_to_response("main/haber.html", locals(), context_instance=RequestContext(request))


def video(request):
    title = "Python Ankara - Videolar"
    siteis = SiteCodes()
    firstvideo, videos = siteis.get_youtube_videos()
    return render_to_response("main/video.html", locals(), context_instance=RequestContext(request))

def etkinlik(request):
    title = "Python Ankara - Etkinlikler"
    posts = Post.objects.filter(status=True, category__slug="etkinlik")
    return render_to_response("main/blog.html", locals(), context_instance=RequestContext(request))

def yazarlar(request):
    title = "Python Ankara - Yazarlarımız"
    authors = User.objects.all().order_by("-id")
    return render_to_response("main/yazarlar.html", locals(), context_instance=RequestContext(request))

def iletisim(request):
    title = "Python Ankara - İletişim"
    return render_to_response("main/iletisim.html", locals(), context_instance=RequestContext(request))

def arama(request):
    title = "Python Ankara - Arama"
    param = str(request.GET.get('q')).strip()
    q_results = Post.objects.extra(where = [
                                "{title} @@ plainto_tsquery('english', '{query}' )".format(title = "content", query=param)],
                                params = ['content'])
    return render_to_response("main/search.html", locals(), context_instance=RequestContext(request))

def page_not_found(request):
    title = "Sayfa Bulunamadı"
    response = render_to_response("main/404.html", locals(), context_instance=RequestContext(request))
    response.status_code = 404
    return response

def tags(request, tagid, slug):
    posts = Post.objects.filter(status=True, tags__slug=slug)
    title = "Python Ankara - " + str(slug).capitalize()
    return render_to_response("main/kategori.html", locals(), context_instance=RequestContext(request))
