from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload, name="upload-xml"),
    path("tables.html/", views.upload, name="table"),
]