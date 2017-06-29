from ..models import Post
from django import template
from ..models import Post, Category

register = template.Library()


@register.simple_tag #将get_recent_post装饰为register.simple_tag(注册)
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:5]


@register.simple_tag
def archives():  #这里与base.html里面的 92行 {% archives as date_list %} archives对应,意思是调用archives()作为list
    return Post.objects.dates('created_time', 'month', order='DESC')
    # month为精度,order=desc表示降序排列


@register.simple_tag
def get_categories():
    return Category.objects.all()