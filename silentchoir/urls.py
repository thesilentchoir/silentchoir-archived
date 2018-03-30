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
from django.conf.urls import url
from silentchoir import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^legal/$', views.LegalPageView.as_view(), name='legal'),
    url(r'^security/$', views.SecurityPageView.as_view(), name='security'),
    url(r'^trigger/$', views.TriggerPageView.as_view(), name='trigger'),
    url(r'^q1-withWhom/$', views.WithWhomPageView.as_view(), name='q1-withWhom'),
    url(r'^q2-email/$', views.EmailPageView.as_view(), name='q2-email'),
    url(r'^q3-whenAndWhere/$', views.WhenAndWherePageView.as_view(), name='q3-whenAndWhere'),
    url(r'^q4-setting/$', views.SettingPageView.as_view(), name='q4-setting'),
    url(r'^q5-identify/$', views.IdentifyPageView.as_view(), name='q5-identify'),
    url(r'^q6-describe/$', views.DescribePageView.as_view(), name='q6-describe'),
    url(r'^q7-connect/$', views.ConnectPageView.as_view(), name='q7-connect'),
    url(r'^q8-resources/$', views.ResourcesPageView.as_view(), name='q8-resources'),
    url(r'^closing/$', views.ClosingPageView.as_view(), name='closing'),
    url(r'^inquire/$', views.InquirePageView.as_view(), name='inquire'),
    url(r'^humans/$', views.InquirePageView.as_view(), name='humans'),
]