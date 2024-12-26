"""
related_name -> This is the name that will be used to access the 
reverse relationship from Author to Book. Instead of the default book_set, 
you'll now use books when referring to all books associated with an author

author = Author.objects.get(id=1)
books = author.books.all()  # Fetch all books by this author
"""

"""
related_query_name -> This name is used when you want to filter the 
Author model based on related Book objects in queries

# Querying authors based on the price of their books
authors_with_expensive_books = Author.objects.filter(book__price__gt=20)
"""



books_with_authors = Books.objects.select_related('author').all()

books_with_review = Book.objects.prefetch_related(
    'reviews'
).select_related(
    'author'
).all()