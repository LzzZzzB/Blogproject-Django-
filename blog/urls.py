#blog/urls.py

from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'), # name是这个url别名, views.index叫做处理函数,调用views.py里面的index函数
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'), #'^post/(?P<pk>[0-9]+)/$', post开头,/结尾, ()里面是捕获组,从URL中捕获匹配的字符串作为关键字传给detail
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]