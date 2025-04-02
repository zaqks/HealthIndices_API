from django.urls import path
from .views import media_server

urlpatterns = [path("media/<path:path>", media_server)]
