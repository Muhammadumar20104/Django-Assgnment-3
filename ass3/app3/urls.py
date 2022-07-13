from django.urls import path
from . import views
urlpatterns = [path('create', views.create),
               path('update/<d>',views.update),
               path('read/<d>',views.read)]