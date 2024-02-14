from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "gsapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("search/", views.SearchView.as_view(), name = "search"),
    path("gourmet_list/", views.gourmet_list, name = "gourmet_list"),
    path("detail/<str:id>/", views.detail_view, name = "detail"),
]
