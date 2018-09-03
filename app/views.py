from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer
from app.models import Snippet, Game, Asset_server
from app.serializers import SnippetSerializer, GameSerializer, Asset_serverSerializer
from rest_framework import generics
from django.views.generic.list import ListView
from django.http import HttpResponse
import os, markdown

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class Asset_serverList(generics.ListCreateAPIView):
    queryset = Asset_server.objects.all()
    serializer_class = Asset_serverSerializer

class Asset_serverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset_server.objects.all()
    serializer_class = Asset_serverSerializer

class Dashboard(ListView):
    template_name = 'app/index.html'
    context_object_name = "game_list"

    def get_queryset(self):
        game_list = Game.objects.all()
        return game_list

def index(request):
    return render(request, 'app/index.html')

def test(request):
    return render(request, 'app/test.html')

def project(request):
    return render(request, 'app/game.html')

def test_highchart(request):
    return render(request, 'app/test_highchart.html')

def file_download(request):
    # do something...
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FILE_ROOT = os.path.join(BASE_DIR, "app/templates/app/")
    with open('{}visit-sequences.csv'.format(FILE_ROOT)) as f:
        c = f.read()
    return HttpResponse(c)

def dji_file_download(request):
    # do something...
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FILE_ROOT = os.path.join(BASE_DIR, "app/templates/app/")
    with open('{}dji.csv'.format(FILE_ROOT)) as f:
        c = f.read()
    return HttpResponse(c)

def bandwidth(request):
    return render(request, 'app/bandwidth.html')

def fault(request):
    return render(request, 'app/fault.html')

class IndexView(ListView):
    template_name = 'app/game.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        '''
        过滤数据，获取游戏列表，并转换为 html 格式
        return
        '''
        game_list = Game.objects.all
        # for game in game_list:
            # game.body = markdown.markdown(game.body, )
        return game_list
    
    # 为上下文添加其他变量
    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)
