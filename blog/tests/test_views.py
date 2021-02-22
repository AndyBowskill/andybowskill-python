from django.test import TestCase, RequestFactory
from django.urls import reverse

from blog.views import index, post_detail

from blog.models import Blog


class BlogViewTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        for blog_number in range(3):
            Blog.blogs.create(id=998 + blog_number, slug=f'testing-blog-{blog_number}', title=f'Testing blog {blog_number}.', date='2021-01-01', content=f'Testing blog {blog_number}.')
 
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_status_code_succeeded(self):
        request = self.factory.get("/")

        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_status_code_succeeded(self):
        request = self.factory.get("/post/testing-2")

        response = post_detail(request, 'testing-blog-2')
        self.assertEqual(response.status_code, 200)

