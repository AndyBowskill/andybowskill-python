from django.test import TestCase

from blog.models import Blog


class TestBlogModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.blogs.create(
            id=1,
            slug="testing-blog-1",
            title="Testing blog 1.",
            date="2021-01-01",
            content="Testing blog 1.",
        )

    def test_id_primary_key_is_true(self):
        blog = Blog.blogs.get(id=1)
        primary_key = blog._meta.get_field("id").primary_key
        self.assertTrue(primary_key)

    def test_slug_max_length(self):
        blog = Blog.blogs.get(id=1)
        max_length = blog._meta.get_field("slug").max_length
        self.assertEquals(max_length, 100)

    def test_slug_default_is_blank(self):
        blog = Blog.blogs.get(id=1)
        slug_default = blog._meta.get_field("slug").default
        self.assertEquals(slug_default, "")

    def test_title_max_length(self):
        blog = Blog.blogs.get(id=1)
        max_length = blog._meta.get_field("title").max_length
        self.assertEquals(max_length, 100)
