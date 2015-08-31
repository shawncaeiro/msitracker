from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'/history', views.history, name='history'),
    url(r'/timeEntry', views.timeEntry, name='timeEntry'),
    url(r'', views.profile, name='profile'),
    url(r'accounts/profile/', views.index, name='index'),
)