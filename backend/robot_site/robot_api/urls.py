from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.calculate_add, name="add"),
    # path("get_token", views.get_csrf_token, name="get_token"),
]
