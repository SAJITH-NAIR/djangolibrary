from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.Booklist.as_view(), name='booklist'),
    path('view/', views.Bookview.as_view(), name='bookview'),
]