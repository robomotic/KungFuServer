from django.conf.urls import patterns, include, url
from blogengine.views import PostsFeed
from django.views.generic import ListView
from blogengine.models import Category, Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Home page
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        )),

    # Blog posts
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),

    # Categories
    url(r'^categories/?$', ListView.as_view(
        model=Category,
        )),
    url(r'^categories/(?P<categorySlug>\w+)/?$', 'blogengine.views.getCategory'),
    url(r'^categories/(?P<categorySlug>\w+)/(?P<selected_page>\d+)/?$', 'blogengine.views.getCategory'),

    # Comments
    url(r'^comments/', include('django.contrib.comments.urls')),

    # RSS feeds
    url(r'^feeds/posts/$', PostsFeed()),
    # Activity log of coding
    url(r'^activity/', include('codemanager.urls', namespace="codemanager")),
    # Restful API root
    url(r'^api/', include('restapi.urls', namespace='rest_framework')), 
    # API for authentication
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
    

)
