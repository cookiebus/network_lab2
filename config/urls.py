from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'network_lab2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'face.views.home'),
    url(r'^result/$', 'face.views.test'),
    url(r'^learn/$', 'face.views.learn'),
    url(r'^ingest/$', 'face.views.ingest'),
)
