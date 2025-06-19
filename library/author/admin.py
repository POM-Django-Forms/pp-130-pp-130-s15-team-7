from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic')
    list_filter = ('name', 'surname', 'patronymic', 'id')
    readonly_fields = ('id',)

    fieldsets = (
        ('Personal info', {'fields': ('name', 'surname', 'patronymic')}),
        ('About books', {'fields': ('books',)})
    )

    add_fieldsets = (
        None, {'fields': ('name', 'surname', 'patronymic')},
    )

    search_fields = ('name',)
    ordering = ('id',)

admin.site.register(Author, AuthorAdmin)
