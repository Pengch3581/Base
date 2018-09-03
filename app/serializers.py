from django.contrib.auth.models import User, Group
from app.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Game, Asset_server
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'create_time', 'status')

class Asset_serverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset_server
        fields = ('id', 'dno', 'pid', 'rid',
                  'parent_id', 'model', 'service_lable', 'service_code', 'r_size', 'status', 'cpu_num', 'cpu', 'mem', 'mem_desc', 'disk',
                  'disk_desc', 'raid_info', 'raid', 'os', 'hostname', 'create_time', 'mac_out', 'mac_in', 'mark')

