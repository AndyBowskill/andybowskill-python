from django.db import models
from django.db.models.fields import DateField, TextField

class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=50, default="")
    title = TextField()
    date = DateField()
    content = TextField()

    blogs = models.Manager()
