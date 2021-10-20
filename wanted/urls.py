from django.urls import path

urlpatterns = [
    path("", Post.as_view()),
    path("<int:post_id>", PostModify.as_view())
]