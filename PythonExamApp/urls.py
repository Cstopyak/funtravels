from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path("register", views.register),
    path("travels", views.travels),
    path("logout", views.logout),
    path("login", views.login),
    path("travels/<int:ItemId>", views.travelinfo),
    path("addtrip", views.addtrip),
    path("uploadtrip", views.uploadtrip),
    
    path("jointrip/<int:ItemId>", views.jointrip),
    path("removetrip/<int:ItemId>", views.removetrip),
    path("deletetrip/<int:ItemId>", views.deletetrip),
]