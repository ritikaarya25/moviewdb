from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    Name = models.CharField(max_length=300)
    Director = models.CharField(max_length=300)
    cast = models.CharField(max_length=300)
    description = models.TextField(1000)
    release_date = models.DateField()
    average_rating = models.FloatField(default=0)
    image = models.URLField(default=None,null=True)

    def __str__(self):
        return self.Name
    
    def __unicode__(self):
        return self.Name
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
    