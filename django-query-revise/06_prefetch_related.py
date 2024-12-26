""" 
prefetch_related is used to optimize database queries by 
reducing the number of database hits. It fetches related objects in a single query
and caches them for later use, which can significantly improve performance when dealing
with many-to-many or reverse one-to-many relationships.

In other words:
prefetch_related is used when you need to efficiently retrieve many related objects,
such as when you want to fetch an author and all of their books.

Unlike select_related, which performs an SQL join, prefetch_related
 performs two separate queries:

One query to retrieve the main objects (e.g., Author).
A second query to retrieve all related objects (e.g., Book), and then
Django handles the in-memory joining of the two.
"""

"""
When to use:
Use it for Many-to-One and Many-to-Many relationships
where there are multiple related objects (e.g., one author has many books).
"""

author_all_books = Author.objects.prefetch_related(
    'books'
).all()

for author in author_all_books:
    for book in author:
        print(author.name, book.title)
