import pytest

from django.test import RequestFactory

from blog.views import index, post_detail

from blog.models import Blog


@pytest.fixture
def setup_test_data():
    ident = 998
    for blog_number in range(3):
        Blog.blogs.create(
            id=ident + blog_number,
            slug=f"testing-blog-{blog_number}",
            title=f"Testing blog {blog_number}.",
            date="2021-01-01",
            content=f"Testing blog {blog_number}.",
        )


@pytest.mark.django_db
class TestBlogView:

    def setup_test_variables(self):
        self.factory = RequestFactory()

    def test_index_status_code_succeeded(self, setup_test_data):
        self.setup_test_variables()
        request = self.factory.get("/")

        response = index(request)
        assert response.status_code == 200

    def test_post_detail_status_code_succeeded(self, setup_test_data):
        self.setup_test_variables()
        request = self.factory.get("/post/testing-2")

        response = post_detail(request, "testing-blog-2")
        assert response.status_code == 200