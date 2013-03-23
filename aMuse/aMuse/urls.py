from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include('api.urls')),
    (r'^webinator/', include('webinator.urls')),
    (r'^kiosk/', include('kiosk.urls')),
    (r'^grappelli/', include('grappelli.urls')),
)

