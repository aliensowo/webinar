from index import views
from django.urls import path
from django.views import View

app_name='index'

urlpatterns = [
    path('', views.index, name="index"),
    ]

