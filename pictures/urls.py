from django.urls import path
from pictures import views

app_name = "pictures"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.image_upload, name="image_upload"),
    path("images/", views.image_list, name="image_list"),
    path("delete/<int:pk>/", views.image_delete, name="image_delete"),
]
