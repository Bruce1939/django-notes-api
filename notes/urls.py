from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("<str:pk>/", views.query_notes, name="note"),
    path("", views.get_add_notes, name="notes"),
]
