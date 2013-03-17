from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

import webinator.views

urlpatterns = patterns('webinator.views',
        url(r'^login/(?P<error>\w+)','show_login_error',name='login-fail'),
        url(r'^login',login,name='login'),
        url(r'^logout/', logout, name='logout'),
        url(r'^logging/','do_login'),
)
