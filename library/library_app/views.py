from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Borrow
from .forms import BookForm
from django.contrib import messages
from .models import ContactMessage  # Import the model

def home(request):
    books = Book.objects.all()
    return render(request, 'library_app/home.html', {'books': books})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.available:
      
        book.available = False
        book.save()
        return redirect('borrow_list')  # Redirect to borrow details page

    return redirect('home')  # If not available, go back

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library_app/add_book.html", {"form": form})

@login_required
def borrow_list(request):
    borrowed_books = Borrow.objects.filter(user=request.user)
    return render(request, 'borrow_list.html', {'borrowed_books': borrowed_books})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(name=name, email=email, message=message)

        messages.success(request, "Your message has been sent successfully!")  # Success message
        return redirect('contact')  # Redirect to the contact page

    return render(request, 'contact.html')