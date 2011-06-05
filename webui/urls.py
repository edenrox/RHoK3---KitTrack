from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webui.views.home', name='home'),
    # url(r'^webui/', include('webui.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^kit/ship', 'webui.views.kit_ship'),
    url(r'^kit/track', 'webui.views.kit_track'),
    #url(r'^kit/usage', 'kit.usage'),
    #url(r'^kit/progress', 'kit.progress'),
    url(r'^kit/(\d)/history', 'webui.views.kit_history'),
    
    #url(r'^location/pending', 'location.pending'),
    #url(r'^location/(\d)/pending', 'location.pending_list'),
)
