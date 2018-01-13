from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView
from django.db.models import Q


class IndexView(ListView):
    model = Post
    template_name = 'blogsite/index.html'
    context_object_name = 'post_list'     #使用类视图方法进行改写
    paginate_by = 2  #设置分页，每页显示的数量




# def index(request):
#     post_list = Post.objects.all()
#     return render(request, 'blogsite/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_vies()   #如果有人访问，那么浏览量加一
    post.body = markdown.markdown(post.body, [
        'extra',
        'codehilite',
        'toc',
    ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list,
    }
    return render(request, 'blogsite/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month)
    return render(request, 'blogsite/index.html', context={'post_list': post_list})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request,'blogsite/index.html',context={'post_list':post_list})


class TagView(ListView):
    model = Post
    template_name = 'blogsite/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request,'blogsite/index.html')
    post_list = Post.objects.filter(Q(title__icontains=q) |Q(body__icontains=q))
    return render(request,'blogsite/index.html',{
        'error_msg':error_msg,
        'post_list':post_list,
    })