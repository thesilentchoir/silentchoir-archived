"""silentchoir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

import survey.views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^trigger/$', TemplateView.as_view(template_name='trigger.html'), name='trigger'),
    url(r'^inquire/$', TemplateView.as_view(template_name='inquire.html'), name='inquire'),
    url(r'^legal/$', TemplateView.as_view(template_name='legal.html'), name='legal'),
    url(r'^security/$', TemplateView.as_view(template_name='security.html'), name='security'),
    url(r'^q1-withWhom/$', TemplateView.as_view(template_name='q1-withWhom.html'), name='q1-withWhom'),
    url(r'^q2-email/$', TemplateView.as_view(template_name='q2-email.html'), name='q2-email'),
    url(r'^q3-whenAndWhere/$', TemplateView.as_view(template_name='q3-whenAndWhere.html'), name='q3-whenAndWhere'),
    url(r'^q4-setting/$', TemplateView.as_view(template_name='q4-setting.html'), name='q4-setting'),
    url(r'^q5-identify/$', TemplateView.as_view(template_name='q5-identify.html'), name='q5-identify'),
    url(r'^q6-describe/$', TemplateView.as_view(template_name='q6-describe.html'), name='q6-describe'),
    url(r'^q7-connect/$', TemplateView.as_view(template_name='q7-connect.html'), name='q7-connect'),
    url(r'^q8-resources/$', TemplateView.as_view(template_name='q8-resources.html'), name='q8-resources'),
    url(r'^closing/$', TemplateView.as_view(template_name='closing.html'), name='closing'),
]
