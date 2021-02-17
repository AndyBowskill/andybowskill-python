# Generated by Django 3.1.5 on 2021-02-16 17:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210212_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(default='')),
                ('title', models.TextField(max_length=100)),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
            managers=[
                ('blogs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='MyBlog',
        ),
    ]
