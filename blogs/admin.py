from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


# 将models注册到后台admin界面
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
