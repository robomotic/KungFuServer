from django.conf.urls import patterns, url

from codemanager import views


urlpatterns = patterns('',
    # ex: /activity/
    url(r'^$', views.index, name='index'),
    # ex: /activity/5/
    url(r'^(?P<activity_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /username
    url(r'^update/$', views.updateFromClient, name='update'),
)
