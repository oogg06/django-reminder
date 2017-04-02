from __future__ import unicode_literals

from django.db import models

# Create your models here.


class EmailAccount(models.Model):
    login           =   models.CharField(max_length=40)
    password        =   models.CharField(max_length=80)
    stmp_server     =   models.CharField(max_length=80)
    tcp_port        =   models.IntegerField()
    
    
    
class GMailAccount(EmailAccount):
    def __init__(self, _stmp_server):
        super(smtp_server=_smtp_server)