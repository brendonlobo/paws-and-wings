from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class memory(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="post_image",blank=True)
    date = models.DateField(("Date"),default=datetime.date.today)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User,related_name= 'post_like')


class Comment(models.Model):
    post = models.ForeignKey(memory ,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField(("Date"),default=datetime.date.today)
    
    