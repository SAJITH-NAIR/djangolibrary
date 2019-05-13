from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.Booklists.as_view(), name='booklist'),
    path('view/', views.Bookview.as_view(), name='bookadd'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='bookdelete'),
    path('update/<int:pk>', views.BookUpdate.as_view(), name='bookupdate'),
    path('sort/', views.Sort.as_view(), name='booksort'),
    path('sort2/', views.Sort2.as_view(), name='booksort2'),

    # path('sort/<int:pk>', views.Search.as_view(), name='booksearch'),
    # path('home/', views.AboutView.as_view(), name='home'),
]