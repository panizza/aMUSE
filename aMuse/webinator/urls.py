from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout



urlpatterns = patterns('webinator.views',
        url(r'^$', 'index', name='index'),
        url(r'^experience/(?P<experience_id>\d+)/$', 'action_list', name='action_list'),
        url(r'^login/', login,  name='login'),
        url(r'^logout/', logout, {'next_page': '/webinator/'}, name='logout'),
        url(r'^story/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/', 'story_preview', name='story_preview'),
        url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
         'reset_password_new_user', name='reset_password_new_user'),
        url(r'^qr/$', 'qr_code_generator', name='qr_code_generator'),

        url(r'^action/(?P<action_id>\d+)/edit/$', 'edit_action', name='edit_action'),
        url(r'^action/(?P<action_id>\d+)/delete/$', 'delete_action', name='delete_action'),
        url(r'^action/(?P<action_id>\d+)/info/$', 'action_info', name='action_info'),
        url(r'^scan/(?P<scan_id>\d+)/info/$', 'scan_info', name='scan_info'),
        url(r'^experience/(?P<experience_id>\d+)/delete/$', 'delete_experience', name='delete_experience'),
        url(r'^experience/(?P<experience_id>\d+)/add/$', 'add_new_action', name='add_new_action'),
        url(r'^experience/(?P<experience_id>\d+)/publish/$', 'publish_experience', name='publish_experience'),
        url(r'^experience/(?P<experience_id>\d+)/confirm/$', 'confirm_publish', name='confirm_publish'),
        url(r'^experience/(?P<experience_id>\d+)/preview/$', 'preview_experience', name='preview_experience'),
        url(r'^experience/(?P<experience_id>\d+)/show/$', 'show_preview', name='show_preview'),
        url(r'^error/(?P<error_id>\d+)$', 'view_error', name='view_error'),

)
