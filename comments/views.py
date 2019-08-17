from django.shortcuts import render, get_object_or_404, redirect
from blogs.models import Post

from .models import Comment
from .forms import CommentForm


# Create your views here.
def post_comment(request, post_pk):
    # 取得关联的文章对象
    post = get_object_or_404(Post, pk=post_pk)

    # 如果是post请求
    if request.method == 'POST':
        # 构造表单实例
        form = CommentForm(request.POST)

        # 如果请求合法
        if form.is_valid():
            # “commit=False”生成Comment实例，但不保存到数据库
            comment = form.save(commit=False)
            # 设置外键
            comment.post = post
            # 保存到数据库
            comment.save()

            # redirect会调用模型实例的get_absolute_url方法，重定向
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blogs/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(post)
