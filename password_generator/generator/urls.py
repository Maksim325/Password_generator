from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='generator-home'),
    path('about/', views.about, name='generator-about'),
]