from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path("hello/", views.say_Hello)
]