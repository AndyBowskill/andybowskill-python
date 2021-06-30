from django.urls.conf import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:slug>/", views.post_detail, name="post_detail"),
]
