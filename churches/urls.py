from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pages/<int:page_id>/", views.detail, name="detail"),
    path("pages/<str:page_slug>/", views.detail_slug, name="detail_slug"),
]
