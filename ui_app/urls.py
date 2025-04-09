from django.urls import path
from .views import ui_app, calibrate, score

urlpatterns = [path('', ui_app), path(
    'calibrate', calibrate), path('score', score)]
