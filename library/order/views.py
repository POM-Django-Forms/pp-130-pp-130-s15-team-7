from django.shortcuts import redirect, render, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib.admin.views.decorators import staff_member_required
from .forms import OrderForm

def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'orders_list.html', {'orders': orders})


@login_required
def user_orders_view(request):
    if request.user.role == 1:
        orders = Order.objects.select_related('user', 'book').all().order_by('-created_at')
    else:
        orders = Order.objects.select_related('book').filter(user=request.user).order_by('-created_at')

    return render(request, 'user_orders_list.html', {'orders': orders})


@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect("orders-list")
    else:
        form = OrderForm()
    return render(request, "create_order.html", {"form": form})
    

@staff_member_required
def close_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.end_at is None:
        order.end_at = now()
        order.is_active = False
        order.save()
    return redirect('orders-list')