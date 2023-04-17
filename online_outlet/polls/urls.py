from django.urls import path

from . import views

urlpatterns = [
    path("home/name=<str:name>/", views.index, name="index"),
]
