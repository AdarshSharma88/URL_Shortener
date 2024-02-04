from django.db import models
from django.contrib.auth.models import User
class LongToShort(models.Model):
	Long_url = models.URLField(max_length=500)
	short_url = models.CharField(max_length= 50,unique = True)
	date = models.DateField(auto_now_add = True)
	clicks=models.IntegerField(default = 0)
# Create your models here.

class UserAuthentication(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
