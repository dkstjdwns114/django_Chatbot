from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chattrain', views.chattrain, name='chattrain'),
]