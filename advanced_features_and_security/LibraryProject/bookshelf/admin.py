from django.contrib import admin
from .models import Book
from .models import CustomUser

admin.site.register(CustomUser,  CustomUserAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
admin.site.register(Book)
# Register your models here.
