from django.urls import path
from . import views

urlpatterns=[
    path('', views.BerandaView.as_view(), name='beranda')
]