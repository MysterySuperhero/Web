from django.conf.urls import patterns, include, url
from django.contrib import admin
import debug_toolbar
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^$', 'ask_nazarkov.views.index', name="index"),
    url(r'^base$', 'ask_nazarkov.views.base'),
    url(r'^index$', 'ask_nazarkov.views.index'),
    url(r'^register$', 'ask_nazarkov.views.register'),
    url(r'^login$', 'ask_nazarkov.views.login'),
    url(r'^question/.*$', 'ask_nazarkov.views.question'),
    url(r'^new_question$', 'ask_nazarkov.views.new_question'),
    url(r'^helloworld', 'ask_nazarkov.views.helloworld'),
    url(r'^parameters', 'ask_nazarkov.views.getparameters'),
    url(r'^search/$', 'ask_nazarkov.views.search'),
    url(r'^tag/(?P<tagname>.*)', 'ask_nazarkov.views.tag'),
)
