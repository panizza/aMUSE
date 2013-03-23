from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^webinator/', include('webinator.urls')),
    url(r'^kiosk/', include('kiosk.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
)

