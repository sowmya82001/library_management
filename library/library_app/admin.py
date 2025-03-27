from django.contrib import admin
from .models import Book, Borrow
from .models import ContactMessage  # Import the model

admin.site.register(Book)
admin.site.register(Borrow)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Show in admin list
    search_fields = ('name', 'email')  # Enable search
    ordering = ('-created_at',)  # Sort by latest messages
