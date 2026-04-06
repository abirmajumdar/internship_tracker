from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('',views.home),
    path('internships/', views.internship_list),
    path('internships/<int:id>/', views.internship_detail),
]