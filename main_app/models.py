from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
class Crew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    members = ArrayField(
    models.CharField(max_length=50),
    size=5,
)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('crews_detail', kwargs={'pk': self.id})