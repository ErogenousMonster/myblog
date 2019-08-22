from django.urls import path
from . import views
from blogs.feeds import AllPostsRssFeed


app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('tag/<int:pk>', views.TagView.as_view(), name='tag'),
    path('all/rss/', AllPostsRssFeed(), name='rss'),
    # path('search/', views.search, name='search')
]
