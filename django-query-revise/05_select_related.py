"""
select_related is used for optimizing queries by
performing a SQL join and retrieving related objects in the same query, 
which is useful for foreign key relationships.
"""

books_with_authors = Book.objects.select_related('author').all()

for book in books_with_authors:
    print(book.title, book.author.name)  # Accessing author without extra query

books_with_authors = Book.objects.select_related(
    'author'
).all()

for book in books_with_authors:
    print(book.title, book.author.name)



"""
Problem Solved:
Without select_related, if you loop through all books and access the author
for each book, Django would issue a separate query for each author,
leading to multiple database hits (the "N+1 query problem")
"""

"""
When to Use:
Only for Foreign Key and One-to-One Relationships: It’s 
designed for relationships where only one related object
exists (like a Book having one Author).
"""