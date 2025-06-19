from django.urls import path
from . import views

urlpatterns = [
    path("", views.orders_list, name="orders-list"),
    path("<int:pk>/", views.orders_list, name="orders-list"),
    path("user-orders/", views.user_orders_view, name="user-orders"),
    path("create/", views.create_order, name="create-order"),
    path('<int:pk>/close/', views.close_order, name='order-close'),
]