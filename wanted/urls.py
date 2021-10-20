from django.urls import path
from .views      import Post, PostModify, SignUp, SignIn

urlpatterns = [
    path("post", Post.as_view()),
    path("post/<int:post_id>", PostModify.as_view()),
    path("signup", SignUp.as_view()),
    path("signin", SignIn.as_view()),
]