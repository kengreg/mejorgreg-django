from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mejorgreg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'htmlpublic.views.home', name='home'),
    url(r'^plus/(\d+)$','htmlpublic.views.plus', name='plus'),
     url(r'^minus/(\d+)$','htmlpublic.views.minus', name='minus'),
     url(r'^categoria/(\d+)$','htmlpublic.views.categoria', name='categoria'),
     url(r'^add/$','htmlpublic.views.add', name='add'),
)
