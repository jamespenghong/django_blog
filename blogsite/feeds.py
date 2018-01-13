from django.contrib.syndication.views import Feed

from .models import Post

class AllPostsRssFeed(Feed):
    title = '彭洪的博客'
    link = '/'
    description = '博客测试文章'
    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' %(item.category,item.title)

    def item_description(self, item):
        return item.body

#添加RSS聚合阅读，RSS（Really Simple Syndication）是一种描述和同步网站内容的格式，它采用 XML 作为内容传递的格式。简单来说就是网站可以把内容包装成符合 RSS 标准的 XML 格式文档。
# 一旦网站内容符合一个统一的规范，那么人们就可以开发一种读取这种规范化的 XML 文档的工具来聚合各大网站的内容。
