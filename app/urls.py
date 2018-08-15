from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views


urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^game/$', views.GameList.as_view()),
    url(r'^game/(?P<pk>[0-9]+)/$', views.GameDetail.as_view()),
    url(r'^gamelist/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^index$', views.index, name='index')
]

urlpatterns = format_suffix_patterns(urlpatterns)
