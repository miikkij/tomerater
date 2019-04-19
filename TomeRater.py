class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}  # Book : Rating

    def get_email(self):
        return self.email

    def change_email(self, address):
        old_email = self.email
        self.email = address
        print("Email of {username} updated from {old} to {new}".format(username=self.name, old=old_email, new=address))

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_books_and_ratings(self):
        return self.books.items()

    def get_average_rating(self):
        total = 0
        valid_ratings_counter = 0
        for value in self.books.values():
            if value is not None:
                total = total + value
                valid_ratings_counter = valid_ratings_counter + 1
        return total / valid_ratings_counter

    def __repr__(self):
        return "User {username}, email: {email}, books read: {read_counter}".format(username=self.name,
                                                                                    email=self.email,
                                                                                    read_counter=len(self.books))

    def __eq__(self, other_user):
        if isinstance(other_user, User) and other_user.name == self.name and other_user.email == self.email:
            return True
        return False

    def __hash__(self):
        return hash(self.email)

class BookInvalidInputParameters(Exception):
    """
    Title, ISBN or Price is invalid
    """

class Book:
    def __init__(self, title, isbn, price=.0):
        if not isinstance(title, str) or not isinstance(isbn, int):
            raise BookInvalidInputParameters("BookInvalidInputParameters Exception info - Title: {title}, ISBN: {isbn}, Price: {price}".format(title=title, isbn=isbn, price=price))
        self.title = title
        self.isbn = isbn
        self.ratings = []
        self.price = price

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, isbn):
        old_isbn = self.isbn
        self.isbn = isbn
        print("ISBN updated from {old} to {new}".format(old=old_isbn, new=isbn))

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        if len(self.ratings) == 0:
            return 0
        total = 0
        count = 0
        for rating in self.ratings:
            total = total + rating
            count = count + 1
        return total / count

    def __eq__(self, other_book):
        if self.title == other_book.get_title() and self.isbn == other_book.get_isbn():
            return True
        return False

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn, price=0):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn, price=0):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}  # User's email mapped to User object
        self.books = {}  # Book object mapped to Users that have read it

    def can_create_book(self, title, isbn):
        if not isinstance(title, str) or not isinstance(isbn, int):
            return False
        isbn_list = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbn_list:
            return False
        else:
            return True

    def create_book(self, title, isbn, price=0):
        if self.can_create_book(title, isbn):
            new_book = Book(title, isbn, price)
            return new_book
        print("Error when trying to create a new book ({title},{isbn}): Book with same ISBN already exists.".format(
            title=title, isbn=isbn))

    def create_novel(self, title, author, isbn, price=0):
        if self.can_create_book(title, isbn) and isinstance(author, str):
            new_book = Fiction(title, author, isbn, price)
            return new_book
        print("Error when trying to create a new novel ({title},{isbn}): Book with same ISBN already exists.".format(
            title=title, isbn=isbn))

    def create_non_fiction(self, title, subject, level, isbn, price=0):
        if self.can_create_book(title, isbn) and isinstance(subject, str) and isinstance(level, str):
            new_book = NonFiction(title, subject, level, isbn, price)
            return new_book
        print(
            "Error when trying to create a new non fiction book ({title},{isbn}): Book with same ISBN already exists.".format(
                title=title, isbn=isbn))

    def add_book_to_user(self, book, email, rating=None):
        if not isinstance(book, Book) and not isinstance(email, str):
            return
        user = self.users.get(email)
        if not user:
            print("No user with email {email}".format(email=email))
        else:
            user.read_book(book, rating)
            book.add_rating(rating)
            book_read_counter = self.books.get(book, 0)
            self.books[book] = book_read_counter + 1

    def valid_email_address(self, email):
        email_rules_accepted_domains = [".org", ".com", ".edu"]
        if "@" not in email or not any(substring in email for substring in email_rules_accepted_domains):
            print("Invalid email ({email}) address when adding user. It must have @-character and has an ending of "
                  ".com, .edu or .org".format(email=email))
            return False
        if email in self.users.keys():
            print("Error when trying to add a new user. User with email: {email} already exists!".format(email=email))
            return False
        return True

    def add_user(self, name, email, user_books=None):
        if not isinstance(name, str) and not isinstance(email, str):
            return
        if not self.valid_email_address(email):
            return
        user = User(name, email)
        self.users[email] = user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email, book.get_average_rating())

    # If n is 0 or less or bigger than amount of books, all books will be returned as sorted list
    def get_n_most_read_books(self, n):
        sorted_list = []
        if not isinstance(n, int):
            return sorted_list
        for book, counter in sorted(self.books.items(), key=lambda item: item[1]):
            sorted_list.append([book, counter])
        return self.get_n_from_list(n, sorted_list, len(self.books))

    def get_n_most_prolific_readers(self, n):
        user_read_most = {}
        sorted_list = []
        if not isinstance(n, int):
            return sorted_list
        for email, user in self.users.items():
            user_read_most[user] = len(user.get_books_and_ratings())
        for user, count_read in sorted(user_read_most.items(), key=lambda item: item[1]):
            sorted_list.append([user, count_read])
        return self.get_n_from_list(n, sorted_list, len(user_read_most))

    def get_n_from_list(self, n, sorted_list, max_n):
        if 0 < n > max_n:
            n = max_n
        sorted_list.reverse()
        return sorted_list[:n]

    def get_n_most_expensive_books(self, n):
        book_price_dict = {}
        sorted_list = []
        for book, counter in self.books.items():
            book_price_dict[book] = book.get_price()
        for book, price in sorted(book_price_dict.items(), key=lambda item: item[1]):
            sorted_list.append([book, book.get_price()])
        return self.get_n_from_list(n, sorted_list, len(book_price_dict))

    def get_worth_of_user(self, email):
        if not self.users.get(email, False):
            return -1
        user = self.users[email]
        worth = 0
        for book, rating in user.get_books_and_ratings():
            worth = worth + book.get_price()
        return worth

    def print_catalog(self):
        print("Current book catalog:")
        for book in self.books.keys():
            print("{title}, {isbn}".format(title=book.get_title(), isbn=book.get_isbn()))

    def print_users(self):
        print("Current list of users:")
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read_book = None
        highest_read_counter = 0
        for book, read_by_user_counter in self.books.items():
            if read_by_user_counter > highest_read_counter:
                highest_read_counter = read_by_user_counter
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        highest_rated_book = None
        highest_average_rating = 0
        for book in self.books.keys():
            average_rating = book.get_average_rating()
            if average_rating > highest_average_rating:
                highest_average_rating = average_rating
                highest_rated_book = book
        return highest_rated_book

    def most_positive_user(self):
        most_positive_user = None
        highest_average_rating = 0
        for user in self.users.values():
            average_rating = user.get_average_rating()
            if average_rating > highest_average_rating:
                highest_average_rating = average_rating
                most_positive_user = user
        return most_positive_user

    def __repr__(self):
        return "TomeRater - Users {user_count}. Books {books_count}".format(user_count=len(self.users),
                                                                            books_count=len(self.books))

    # If users and books matches it is considered as equal
    def __eq__(self, other):
        for email in self.users.keys():
            email_found = False
            for other_email in other.users.keys():
                if email == other_email:
                    email_found = True
            if not email_found:
                return False
        for book in self.books.keys():
            book_found = False
            for other_book in other.books.keys():
                if book == other_book:
                    book_found = True
            if not book_found:
                return False
        return True
