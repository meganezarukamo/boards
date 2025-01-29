from django.urls import path
from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/create/", views.create_post, name="create_post"),  # 作成
    path("post/edit/<int:post_id>/", views.edit_post, name="edit_post"),  # 修正
    path("post/", views.read_post, name="read_post"),  # 一覧表示
    path("post/delete/<int:post_id>/", views.delete_post, name="delete_post"),  # 削除
]
