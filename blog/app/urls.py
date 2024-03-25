import statistics
from django.conf import SettingsReference, settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]

urlpatterns += statistics(settings.MEDIA_URL , document_root=settings.MEDIA_root)
