from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("entries/<str:title>", views.entry, name="entry"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("randompg", views.randompg, name="randompg"),
]
