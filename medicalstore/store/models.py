from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings 

class Medicine(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

# Create your models here.
