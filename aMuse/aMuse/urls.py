from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from webinator import  views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^api/', include('api.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webinator', TemplateView.as_view(template_name="webinator/index.html")),

)

#from django.conf import settings

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#    )
