from django.urls import include, path

from .views import home
from apptrackerapp.views import *
from apptrackerapp import views

app_name = 'apptrackerapp'

urlpatterns = [
    path('', home, name='home'),
]