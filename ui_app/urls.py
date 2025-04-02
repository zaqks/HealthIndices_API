from django.urls import path
from .views import ui_app, calibrate

urlpatterns = [path('', ui_app), path('calibrate', calibrate)]
