from django.db import models
from django.db.models.fields import DateField, TextField


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.SlugField(max_length=50, default="")
    title = TextField(max_length=100)
    date = DateField()
    content = TextField()

    blogs = models.Manager()

    def __str__(self) -> str:
        return self.title
