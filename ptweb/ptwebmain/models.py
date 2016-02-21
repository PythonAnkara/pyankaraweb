from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class CommonInfo(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        abstract = True


class Tag(CommonInfo):

    def __str__(self):
        return self.title


class Category(CommonInfo):

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    pub_datetime = models.DateTimeField(auto_now=True)
    content = RichTextField()
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    thumbn = models.ImageField(upload_to='thumbnails',
                               height_field='thumbn_height',
                               width_field='thumbn_width')
    thumbn_height = models.PositiveIntegerField(default=60)
    thumbn_width = models.PositiveIntegerField(default=60)

    class Meta:
        ordering = ['-pub_datetime']

    """
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('ptwebmain.views.details', args=[str(self.id)])
    """

    def __str__(self):
        return "{0} ({1})".format(self.title, self.category.title)


class Slider(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='sliderimages')
    href = models.CharField(max_length=255)
    order = models.IntegerField()

    def __str__(self):
        return "{}. {} ({})".format(self.id, self.title, self.order)


class Hit(models.Model):
    ip = models.CharField(max_length=15)
    post = models.ForeignKey(Post)
    date = models.DateField(auto_now=True)
    datatype = models.CharField(max_length=50, default='read')
    email = models.CharField(max_length=255, default="#")
    def __str__(self):
        return "{}. {} ({})".format(self.date, self.ip, self.post.title)

class Author(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField(max_length=1000)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    google = models.CharField(max_length=100)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    ipaddress = models.GenericIPAddressField(protocol='IPv4')
    message = models.CharField(max_length=5000)
    pub_datetime = models.DateTimeField(auto_now=True)
    parentid = models.IntegerField()
    post = models.ForeignKey(Post)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{0} ({1}) - {2}".format(self.name, self.message, self.status)
