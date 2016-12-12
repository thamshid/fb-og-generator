from django.conf.urls import url

from web.views import *

urlpatterns = [
    url(r'^(?P<link>.*)/$', login, name='login'),
    ]
