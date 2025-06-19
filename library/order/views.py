from django.shortcuts import redirect, render
from .models import Order
from django.contrib.auth.decorators import login_required
from book.models import Book
from datetime import datetime
from django.utils.timezone import now
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, get_object_or_404

def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})


@login_required
def user_orders_view(request):
    if request.user.is_librarian():
        # Бібліотекар бачить усі замовлення
        orders = Order.objects.select_related('user', 'book').all().order_by('-created_at')
    else:
        # Звичайний користувач бачить тільки свої
        orders = Order.objects.select_related('book').filter(user=request.user).order_by('-created_at')

    return render(request, 'user_orders.html', {'orders': orders})


@login_required
def create_order(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        plated_end_at = request.POST.get("plated_end_at")

        try:
            book = Book.objects.get(pk=book_id)
            user = request.user
            plated_end_at = datetime.fromisoformat(plated_end_at)

            Order.create(user=user, book=book, plated_end_at=plated_end_at)
            return redirect("profile")  # або інше посилання, наприклад, orders-list
        except Exception as e:
            return render(request, "create_order.html", {"books": Book.objects.all(), "error": str(e)})

    return render(request, "create_order.html", {"books": Book.objects.all()})


@staff_member_required
def close_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.end_at is None:
        order.end_at = now()
        order.is_active = False
        order.save()
    return redirect('orders-list')
