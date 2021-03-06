"""bjtquestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from quiz.views import *
from users.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^login/$', weblogin),
    url(r'^loginback/$', webloginback),
    url(r'^logout/$', weblogout),
    url(r'^main/$', main),
    url(r'^quiz/$', quiz),
    url(r'^submit/$', submit),
    url(r'^admin_interface/$', admin_interface),
    url(r'^admin_interface/history/$', history),
    url(r'^admin_interface/questions/$', questions),
    url(r'^question/query/$', query_question),
    url(r'^question/modify/$', modify_question),
    url(r'^question/delete/$', delete_question),
    url(r'^question/add/$', add_question),
    #url(r'^finished/$', finished),
    url(r'^rankings/$', rankings),
    url(r'^endquiz/$', endquiz),
    url(r'^readquestions/$', readquestions),
]
