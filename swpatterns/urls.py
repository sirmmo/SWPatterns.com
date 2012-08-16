from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pattern.views.index', name='home'),
    url(r'^patterns/all$', "pattern.views.all"),
    url(r'^patterns/random$', "pattern.views.random"),
    url(r'^patterns/list$', "pattern.views.list_patterns"),
    url(r'^patterns/(?P<id>\d+)$', "pattern.views.get_pattern"),
    
    url(r'^tags/list$', "pattern.views.list_tags"),
    url(r'^tags/(?P<id>\d+)$', "pattern.views.get_tag"),
    
    url(r'^langs/list$', "pattern.views.list_langs"),
    url(r'^langs/(?P<id>\d+)$', "pattern.views.get_lang"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
