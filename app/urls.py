from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views


urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^game/$', views.GameList.as_view()),
    url(r'^game/(?P<pk>[0-9]+)/$', views.GameDetail.as_view()),
    url(r'^asset/$', views.Asset_serverList.as_view()),
    url(r'^asset/(?P<pk>[0-9]+)/$', views.Asset_serverDetail.as_view()),
    url(r'^gamelist/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^index$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^visit-sequences.csv$', views.file_download, name='file_download'),
    url(r'^project/$', views.project, name='project'),
    url(r'^test_highchart/$', views.test_highchart, name='test_highchart'),
    url(r'^indexview/$', views.IndexView.as_view(), name='indexview'),
    url(r'^bandwidth/$', views.bandwidth, name='bandwidth'),
    url(r'^fault/$', views.fault, name='fault'),
    url(r'^fault/dji.csv$', views.dji_file_download, name='dji_file_download'),
    url(r'^dji.csv$', views.dji_file_download, name='dji_file_download'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
