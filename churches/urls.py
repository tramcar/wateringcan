from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact-us/", views.contact_us, name="contact_us"),
    path("pages/<int:page_id>/", views.detail, name="detail"),
    path("pages/<str:page_slug>/", views.detail_slug, name="detail_slug"),
]
