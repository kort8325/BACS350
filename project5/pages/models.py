from django.db import models
from django.urls import reverse

class Post(models.Model):
    name = models.CharField(max_length=50)
    identity = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    body = models.TextField(default='post')

    def __str__(self):
        return f'{self.name} - {self.identity}'
    
    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)])

# Create your models here.
