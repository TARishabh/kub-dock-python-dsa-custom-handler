""" 
An F expression in Django allows you to reference model field values directly
in your queries, enabling you to make comparisons between different fields in 
the same model instance.
"""

from django.db.models import F

# Write a query using F expressions to find all books where the
# publication year is greater than the year of the author's birth.

books = Book.objects.filter(
    publication_date__year__gt=F('author__birth_date__year')
)