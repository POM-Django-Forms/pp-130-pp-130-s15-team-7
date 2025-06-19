from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'count')
    list_filter = ('name', 'description', 'count', 'id')
    readonly_fields = ('id', 'description',)

    fieldsets = (
        ('Name', {'fields': ('name',)}),
        ('Info', {'fields': ('description', 'count')})
    )

    add_fieldsets = (
        (None, {'fields': ('name', 'description', 'count')}),
    )

    ordering = ('id',)
    search_fields = ('name',)

admin.site.register(Book, BookAdmin)