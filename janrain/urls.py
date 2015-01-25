from django.conf.urls import patterns, url

urlpatterns = patterns('janrain.views',
    url(r'^login/$', 'login', name='janrain_login'),
    url(r'^logout/$', 'logout', name='janrain_logout'),
    url(r'^loginpage/$', 'loginpage', name='janrain_loginpage'),
)
