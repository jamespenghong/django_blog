from blogsite.models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]
# 将一个函数注册成为模板标签，可以直接在模板使用

@register.simple_tag
def archives():
    return Post.objects.dates('create_time','month',order='DESC')
# 这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，
# 且是 Python 的 date 对象，精确到月份，降序排列。

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
