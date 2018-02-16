# djangotemplates/example/urls.py

from django.conf.urls import url
from silentchoir import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^intro/$', views.IntroPageView.as_view(), name='intro'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]