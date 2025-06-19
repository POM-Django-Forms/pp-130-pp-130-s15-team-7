from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name', 'email', 'id')
    readonly_fields = ('id', 'is_active',)

    fieldsets = (
        ('Info for login', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Role', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'is_superuser',
            ),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('id',)

admin.site.register(CustomUser, CustomUserAdmin)