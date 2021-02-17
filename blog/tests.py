from django.test import TestCase
from django.urls import reverse

from blog.models import Blog

class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.blogs.create(id=998, title='Testing blog 1.', date='2021-01-01')

    def test_title_max_length(self):
        blog = Blog.blogs.get(id=998)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)
