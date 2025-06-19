from .models import Book
from django.shortcuts import redirect, render

def books_info(request):
    sort_by = request.GET.get('sort', '')
    books = Book.objects.all()

    if sort_by == 'name_asc':
        books = books.order_by('name')
    elif sort_by == 'name_desc':
        books = books.order_by('-name')
    elif sort_by == 'count_asc':
        books = books.order_by('count')
    elif sort_by == 'count_desc':
        books = books.order_by('-count')

    return render(request, 'books_info.html', {'books': books, 'selected_sort': sort_by})


def book_detail(request, pk):
    book = Book.get_by_id(pk)
    return render(request, 'book_detail.html', {'book': book})
