"""
Aggregation refers to computing a single value from a set of values, 
such as sums or averages. Django provides several aggregation functions like 
Count, Sum, Avg, etc.
"""

"""
Annotation adds calculated fields to your QuerySets, 
allowing you to aggregate values per group of results. 
This is useful when you want to see computed values alongside your QuerySet results.
"""

authors_book_average = Author.objects.annotate(
    avg_book_price = Avg('book__price')
)

author_total_price_of_books = Author.objects.annotate(
    total_price = Sum('book__price')
)