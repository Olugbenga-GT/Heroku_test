from django.urls import  path
from . import views


urlpatterns = [
    path('home/', views.index, name = 'index-page'),
    path('register/', views.register, name = 'register')

]