from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at')
    list_filter = ('user', 'created_at', 'id')
    readonly_fields = ('id', 'created_at', )

    fieldsets = (
        ('Name', {'fields': ('book',)}),
        ('User', {'fields': ('user',)}),
        ('Date', {'fields': ('end_at', 'plated_end_at', 'is_active',)}),
    )

    add_fieldsets = (
        None,
        {'fields': ('book',)}
    )

    search_fields = ('name', 'user')

    ordering = ('id',)

    ordering = ('id',)


admin.site.register(Order, OrderAdmin)