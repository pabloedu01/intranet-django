from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class conta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cod_logix = models.IntegerField()
    def __str__(self):
        return self.user.username