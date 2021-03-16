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

    return Blog.blogs.get(id=ident)


@pytest.mark.django_db
class TestBlogModel:
    def test_id_primary_key_is_true(self, setup_test_data):
        blog = setup_test_data
        primary_key = blog._meta.get_field("id").primary_key
        assert primary_key == True

    def test_slug_max_length(self, setup_test_data):
        blog = setup_test_data
        max_length = blog._meta.get_field("slug").max_length
        assert max_length == 100

    def test_slug_default_is_blank(self, setup_test_data):
        blog = setup_test_data
        slug_default = blog._meta.get_field("slug").default
        assert slug_default == ""

    def test_title_max_length(self, setup_test_data):
        blog = setup_test_data
        max_length = blog._meta.get_field("title").max_length
        assert max_length == 100
