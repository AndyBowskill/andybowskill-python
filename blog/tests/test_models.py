import pytest

from blog.models import Blog

@pytest.fixture
def setup_test_data():
    ident = 998
    
    Blog.blogs.create(
        id=ident,
        slug="testing-blog-1",
        title="Testing blog 1.",
        date="2021-01-01",
        content="Testing blog 1.",
    )


@pytest.mark.django_db
class TestBlogModel:

    _ident = 998

    def test_id_primary_key_is_true(self, setup_test_data):
        blog = Blog.blogs.get(id=self._ident)
        primary_key = blog._meta.get_field("id").primary_key
        assert primary_key == True

    def test_blog_max_length(self, setup_test_data):
        blog = Blog.blogs.get(id=self._ident)
        max_length = blog._meta.get_field("slug").max_length
        assert max_length == 50

    def test_blog_default_is_blank(self, setup_test_data):
        blog = Blog.blogs.get(id=self._ident)
        slug_default = blog._meta.get_field("slug").default
        assert slug_default == ""

    def test_title_max_length(self, setup_test_data):
        blog = Blog.blogs.get(id=self._ident)
        max_length = blog._meta.get_field("title").max_length
        assert max_length == 100