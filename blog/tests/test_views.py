from django.test import TestCase

from blog.models import Blog


class TestBlogView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.blogs.create(
            id=1,
            slug="testing-blog-1",
            title="Testing blog 1.",
            date="2021-01-01",
            content="Testing blog 1.",
        )

    def test_index_status_code_succeeded(self):
        response = self.client.get("/", secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "I'm Andy, a software developer with 15 plus years of real-life experience.",
        )

    def test_post_detail_status_code_succeeded(self):
        response = self.client.get("/post/testing-blog-1/", secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Testing blog 1")
