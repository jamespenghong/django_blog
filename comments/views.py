from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .models import Comment
from .forms import CommentForm
from blogsite.models import Post

def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk = post_pk)
    # form = CommentForm(request.POST)  # 构造表单
    if request.method == 'POST':
        form = CommentForm(request.POST)  #构造表单
        if form.is_valid():    #检查数据合法性
            comment = form.save(commit=False)   #这个地方一定要注意是false，因为是外键。
            comment.post = post
            comment.save()
            return redirect(post)
            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
        else:
            comment_list = post.comment_set.all() #反向查询所有的评论
            context ={
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blogsite/detail.html',context=context)
    return redirect(post)