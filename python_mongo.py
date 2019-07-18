from pymongo import  MongoClient

host = "localhost"
port = 27017
client = MongoClient(host, port)
mydb = client["library"]
book_collection = mydb["books"]


client.close()

book = { "title": "Pride and Prejusice", "author": "Jane Austen" }
new_id = book_collection.insert_one(book)
print("Inserted book with id %s" % new_id.inserted_id)

new_books = [
    {"title": "Persuasion", "author": "Jane Austen"},
    {"title": "Northanger Abbey", "author": "Jane Austen"}
]
new_ids = book_collection.insert_many(new_books)

print("Inserted IDs")
for id in new_ids.inserted_ids:
    print(id)

#FIND ONE BOOK BY TITLE
'''
myquery = {"title": "Persuasion"}

doc = book_collection.find_one(myquery)


if doc is not None:
    print(doc)
else:
    print("Book not found: Persuasion")
'''

#FIND MANY BOOKS OF THE SAME AUTHOR

'''
authorquery = {"author": "Jane Austen" }
books = book_collection.find(authorquery)


for book in books:
    print(book)
if books.retrieved == 0:
    print("Author not found: Jane Austen")
else:
    print(" %s books found with author Jane Austen" % books.retrieved)

'''
#Change the title of one book from Persuasion to Northanger Abbey
'''
myquery = {"name": "Northanger Abbey"}
newvalues = {"$set": {"name": "Persuasion"}}

result = book_collection.update_one(myquery, newvalues)
print("%d documents matched, %d documents updated"
    %(result.matched_count, result.modified_count))

'''
#Change the author from Jane Austen to Austen, J throughout
'''
myquery = {"author": "Jane Austen"}
newvalues = {"$set": {"author": "Austen, J"}}

result = book_collection.update_many(myquery, newvalues)
print("%d documents matched, %d documents updated"
    %(result.matched_count, result.modified_count))
    '''

#delete one book
'''
book = {"title": "Pride and Predjudice", "author": "Austen, J"}
results = book_collection.delete_one(book)
print("\n Deleted %d books" % (results.deleted_count))
'''
#delete all documents in the collection with author Austen J
'''
results = book_collection.delete_many({"author": "Jane Austen"})
print ("\nDeleted %d books" %(results.deleted_count))
'''