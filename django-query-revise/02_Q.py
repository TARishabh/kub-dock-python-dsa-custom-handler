""" 
A Q object in Django allows you to create complex queries 
by combining multiple conditions using logical operators like AND and OR
. This is especially useful when you need to filter data based on multiple criteria.
"""

from django.db.models import Q

books = Book.objects.filter(
    Q(title__icontains='Django') | Q(publication_date__gt='2021-01-01')
)