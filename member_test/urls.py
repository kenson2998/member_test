"""member_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sema_member.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #練習cookie和session
    url(r'^set_cookie/$',set_cookie ),
    url(r'^get_cookie/$',get_cookie ),
    url(r'^set_session/(\w+)/(\w+)$',set_session ),
    url(r'^get_session/(\w+)$',get_session ),
    url(r'^del_session/$', del_session),
    url(r'^vote/$', vote),

    #
    url(r'^$',index ),
    url(r'^login/$',login ),
    url(r'^logout/$', logout),
    url(r'^sign/',sign ),
    url(r'^createacc/$', createacc),
    url(r'^database/$', database),
    url(r'^show/', show),
    url(r'^chatroom/', chatroom),
    url(r'^fresh/', fresh),
    url(r'^msg/', msg),
    url(r'^champ/',champ_know ),
    url(r'^champ_p/', champ_p)
    ]
