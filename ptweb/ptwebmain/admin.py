from django.contrib import admin

from .models import *

# Register your models here.
class CommonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class PostAdmin(CommonAdmin):
    pass

class AllAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, CommonAdmin)
admin.site.register(Category, CommonAdmin)
admin.site.register(Slider, CommonAdmin)
admin.site.register(Hit, AllAdmin)
admin.site.register(Author, AllAdmin)
admin.site.register(Comment, AllAdmin)
