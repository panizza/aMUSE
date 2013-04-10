from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout


urlpatterns = patterns('webinator.views',
        url(r'^$', 'index', name='index'),
        url(r'^experience/(?P<experience_id>\d+)/$', 'action_list', name='action_list'),
        url(r'^login/', login,  name='login'),
        url(r'^logout/', logout, {'next_page': '/webinator/'}, name='logout'),
        url(r'^preview/', 'experience_preview', name='preview'),
        url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
         'reset_password_new_user', name='reset_password_new_user'),
        url(r'^qr/$', 'qr_code_generator', name='qr_code_generator'),

        url(r'^action/(?P<action_id>\d+)/edit/$', 'edit_action', name='edit_action'),
        url(r'^action/(?P<action_id>\d+)/delete/$', 'delete_action', name='delete_action'),
        url(r'^experience/(?P<experience_id>\d+)/delete/$', 'delete_experience', name='delete_experience'),



)
