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
    url(r'^intro/$', views.IntroPageView.as_view(), name='intro'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^legal/$', views.LegalPageView.as_view(), name='legal'),
    url(r'^consent/$', views.ConsentPageView.as_view(), name='consent'),
    url(r'^trigger/$', views.TriggerPageView.as_view(), name='trigger'),
    url(r'^q1-withWhom/$', views.WithWhomPageView.as_view(), name='q1-withWhom'),
    url(r'^q2-comfortLevel/$', views.ComfortLevelPageView.as_view(), name='q2-comfortLevel'),
    url(r'^q3-email/$', views.EmailPageView.as_view(), name='q3-email'),
    url(r'^q4-when/$', views.WhenPageView.as_view(), name='q4-when'),
    url(r'^q5-setting/$', views.SettingPageView.as_view(), name='q5-setting'),
    url(r'^q6-where/$', views.WherePageView.as_view(), name='q6-where'),
    url(r'^q7-identity/$', views.IdentityPageView.as_view(), name='q7-identity'),
    url(r'^q8-social/$', views.SocialPageView.as_view(), name='q8-social'),
    url(r'^q9-describe/$', views.DescribePageView.as_view(), name='q9-describe'),
    url(r'^q10-resources/$', views.ResourcesPageView.as_view(), name='q10-resources'),
    url(r'^q11-connect/$', views.ConnectPageView.as_view(), name='q11-connect'),
    url(r'^closing/$', views.ClosingPageView.as_view(), name='closing'),
]