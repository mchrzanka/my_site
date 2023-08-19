from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request, "book_store/index.html", {
        "books": books,
        "total_num_of_books": num_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(id=id) # database=local 
    # except:
    #     raise Http404() #I didn't add this template, but if I had one it would show a 404 page
    
    #we need this so much that django has a method for the above
    book = get_object_or_404(Book, slug=slug) 

    context={
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    }
    return render(request, "book_store/book_detail.html", context)