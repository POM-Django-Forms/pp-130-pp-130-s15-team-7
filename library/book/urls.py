from django.urls import path
from . import views

urlpatterns = [
    path("", views.books_info, name='books-info'),
    path("<int:pk>/", views.book_detail, name='book-detail'),
]