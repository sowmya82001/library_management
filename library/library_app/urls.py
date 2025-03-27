from django.urls import path
from . import views
from .views import borrow_book, borrow_list
from .views import book_list, add_book
from .views import contact_view  # Import the view

urlpatterns = [
    path('', views.home, name='home'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('borrow-list/', views.borrow_list, name='borrow_list'),  # View borrowed books
    path('books/', book_list, name='book_list'),
    path("books/add/", add_book, name="add_book"),
    path('contact/', contact_view, name='contact'),  # Contact page URL
]
