from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    member1_name = models.CharField(max_length=50)
    member2_name = models.CharField(max_length=50)
    member3_name = models.CharField(max_length=50, blank=True)
    member4_name = models.CharField(max_length=50, blank=True)
    member5_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.names