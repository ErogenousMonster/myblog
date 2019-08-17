from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    """类别数据库"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签数据库"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章数据库"""
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文，用TextField来储存大量文本
    body = models.TextField()

    # 文章创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要可为空
    excerpt = models.CharField(max_length=200, blank=True)

    # 设置外键
    # 一篇文章只能有多个分类，属于一对多关系
    # 而标签和文章属于多对多关系
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，这里User是从 django.contrib.auth.models 中导入的
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 阅读量
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.pk})

    # 增加阅读量
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
