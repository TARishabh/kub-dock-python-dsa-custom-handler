# custom_filter = Review.objects.filter(
#     rating__gt=3,book__price__lt=50
# )

# for review in custom_filter:
#     print(review.book.name,review.book.author.name,review.name,review.comment)


# custom_data = Review.objects.select_related(
#     'book'
# ).select_related(
#     'author'
# ).filter(
#     rating__gt=3,book__price__lt=50
# )

# for review in custom_data:


books = Book.objects.prefetch_related(
    'reviews'
).select_related(
    'author'
).select_related(
    'author__publisher'
).all()

authors = Author.objects.select_related(
    'publisher'
).prefetch_related(
    'books__reviews'
)