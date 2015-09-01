from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'/history', views.history, name='history'),
    url(r'/teamHistory', views.teamHistory, name='teamHistory'),
    url(r'/timeEntry', views.timeEntry, name='timeEntry'),
    url(r'/unlinkedAccount', views.unlinkedAccount, name='unlinkedAccount'),
    url(r'/index2', views.index2, name='index2'),

    url(r'', views.profile, name='profile'),
    url(r'accounts/profile/', views.index, name='index'),
)