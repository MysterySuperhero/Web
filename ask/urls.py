from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^helloworld', 'ask_nazarkov.views.helloworld'),
    url(r'^parameters', 'ask_nazarkov.views.getparameters'),
    url(r'^', 'ask_nazarkov.views.helloworld'),
)
