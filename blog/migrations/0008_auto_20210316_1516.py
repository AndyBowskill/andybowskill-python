# Generated by Django 3.1.5 on 2021-03-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_auto_20210303_1347"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(default="", max_length=100),
        ),
    ]
