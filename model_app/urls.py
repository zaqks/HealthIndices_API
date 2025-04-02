from django.urls import path
from .views import model_app, calibrate

app_name = 'model_app'
urlpatterns = [path('', model_app, name='model'), path(
    'calibrate', calibrate, name='calibrate')]
