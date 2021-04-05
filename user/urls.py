from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.show_user_info, name="show_user_info"),
]