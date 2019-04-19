from TomeRater import *

Tome_Rater = TomeRater()

# Create some books with some tests:
book_error = Tome_Rater.create_book("Society of Mind", None)  # ISBN missing - error
book_error2 = Tome_Rater.create_book(12345, 12345)  # Book name is not a string
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
book2 = Tome_Rater.create_book("Food for coders", 84372672, 2.54)
book3 = Tome_Rater.create_book("Loops and hoops", 385874323, 64.42)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
novel_error = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll",
                                      12345)  # Same book twice, however ISBN is different and should be accepted
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
nonfiction3 = Tome_Rater.create_non_fiction("Computers", "Graphics", "turbo", 134451313, 34.55)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)
novel4 = Tome_Rater.create_novel("The ABC's of programming", "John Doe", 9284374, 12.45)
novel5 = Tome_Rater.create_novel("That's it!", "Albert Einstein", 1902938478, 25.95)

# Create users with some email tests:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
# Tests for testing erroneous email addresses
Tome_Rater.add_user("E: David Marr", "david@computation.org")  # Duplicate
Tome_Rater.add_user("E: User email without @", "withoutmiukumaukucomputation.org")  # Without @
Tome_Rater.add_user("E: User email without ending", "without@ending")  # Without domain
Tome_Rater.add_user("E: User email without ending and @", "justtextasemail")  # Just a string

# Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, book3, novel1, novel2, nonfiction1, nonfiction3])

# Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(book2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(book3, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel4, "alan@turing.com", 2)


Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 4)
Tome_Rater.add_book_to_user(novel4, "marvin@mit.edu", 1)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)
Tome_Rater.add_book_to_user(novel5, "david@computation.org", 3)
Tome_Rater.add_book_to_user(nonfiction3, "david@computation.org", 2)
Tome_Rater.add_book_to_user(book3, "david@computation.org", 3)


# Sophisticated analysis
# print(Tome_Rater.get_n_most_read_books(3))
# print(Tome_Rater.get_n_most_prolific_readers(3))

# Price
# print(Tome_Rater.get_n_most_expensive_books(3))
# print(Tome_Rater.get_worth_of_user("marvin@mit.edu")) #Prints the sum of the costs of all the books read by this user

# Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
print(Tome_Rater)

# Test set for get n most read books
print(Tome_Rater.get_n_most_read_books(3))
print(Tome_Rater.get_n_most_read_books(12))
print(Tome_Rater.get_n_most_read_books(-1))
print(Tome_Rater.get_n_most_read_books(0))
print(Tome_Rater.get_n_most_read_books(1))

# Test set for get n most expensive books
print(Tome_Rater.get_n_most_expensive_books(3))
print(Tome_Rater.get_n_most_expensive_books(12))
print(Tome_Rater.get_n_most_expensive_books(-1))
print(Tome_Rater.get_n_most_expensive_books(0))
print(Tome_Rater.get_n_most_expensive_books(1))
