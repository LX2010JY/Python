from django.conf.urls import patterns,url
from polls import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^result/(?P<poll_id>\d+)/$',views.results,name='results'),
    url(r'^vote/(?P<poll_id>\d+)/$', views.vote, name='vote'),
]
