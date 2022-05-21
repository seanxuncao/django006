from django.db import models

# Create your models here.
class Blog(models.Model):
    # title
    title = models.CharField(max_length=200)
    # pub_date
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # image
    image = models.ImageField(upload_to="images/")