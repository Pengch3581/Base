from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
# Create your models here.

# Game table
class Game(models.Model):
    STATUS = (
        (0, 'enable'),
        (1, 'disable'),
    )
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS)

# asset table
class Asset_server(models.Model):
    dno = models.CharField(max_length=50)
    pid = models.IntegerField()
    rid = models.IntegerField()
    parent_id = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50)
    service_lable = models.CharField(max_length=50, null=True)
    service_code = models.CharField(max_length=50, null=True)
    r_size = models.IntegerField()
    status = models.IntegerField()
    cpu_num = models.IntegerField()
    cpu = models.CharField(max_length=200)
    mem = models.IntegerField()
    mem_desc = models.CharField(max_length=100, null=True)
    disk = models.IntegerField()
    disk_desc = models.CharField(max_length=100, null=True)
    raid_info = models.CharField(max_length=100, null=True)
    raid = models.CharField(max_length=100, null=True)
    os = models.CharField(max_length=100, null=True)
    hostname = models.CharField(max_length=100, null=True)
    create_time = models.DateField(auto_now=True, null=True)
    mac_out = models.CharField(max_length=100, null=True)
    mac_in = models.CharField(max_length=100, null=True)
    mark = models.CharField(max_length=100, null=True)

# project 
class Project(models.Model):
    pflag = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    principalid = models.IntegerField()
    des = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=50, null=True)
    syncTime = models.DateField(auto_now=True, null=True)
    aliveServiceCount = models.IntegerField(null=True)
    getAliveTime = models.DateField(auto_now=True, null=True)
    syncTimePartners = models.DateField(auto_now=True, null=True)
    project_type = models.IntegerField()
    zoon = models.CharField(max_length=50, null=True)
    bstyle = models.IntegerField(null=True)

# bandwidth
class Bandwidth(models.Model):
    pass

