from .models import Book
from django.shortcuts import redirect, render, get_object_or_404
from .forms import BookForm
from author.models import Author

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

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            # Додаємо авторів
            authors_text = form.cleaned_data.get('authors_text', '')
            if authors_text:
                author_names = [name.strip() for name in authors_text.split(',') if name.strip()]
                for full_name in author_names:
                    parts = full_name.split()
                    if len(parts) == 3:
                        name, patronymic, surname = parts
                    elif len(parts) == 2:
                        name, surname = parts
                        patronymic = ''
                    elif len(parts) == 1:
                        name = parts[0]
                        patronymic = ''
                        surname = ''
                    else:
                        continue

                    author, created = Author.objects.get_or_create(
                        name=name,
                        patronymic=patronymic,
                        surname=surname
                    )
                    book.authors.add(author) 

            return redirect('books-info')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'book': book})
