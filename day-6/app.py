# project-1 idea simple banking system with bunch of features

# defining parent class account 

# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self._balance = balance   # encapsulated
#         self.transactions = []

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid deposit amount")
#             return
        
#         self._balance += amount
#         self.transactions.append(f"Deposited: {amount}")
#         print(f"{amount} deposited successfully")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid withdrawal amount")
#             return
        
#         if amount > self._balance:
#             print("Insufficient balance")
#             return
        
#         self._balance -= amount
#         self.transactions.append(f"Withdrawn: {amount}")
#         print(f"{amount} withdrawn successfully")

#     def get_balance(self):
#         return self._balance

#     def show_transactions(self):
#         print(f"\nTransaction history for {self.name}:")
#         for t in self.transactions:
#             print(t)
            
# # inheretance
# # children classes

# class SavingsAccount(Account):
#     MIN_BALANCE = 1000

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid withdrawal amount")
#             return
        
#         if self._balance - amount < self.MIN_BALANCE:
#             print("Cannot withdraw: Minimum balance requirement violated")
#             return
        
#         self._balance -= amount
#         self.transactions.append(f"Withdrawn: {amount}")
#         print(f"{amount} withdrawn successfully (Savings)")
        
        
# class CurrentAccount(Account):
#     OVERDRAFT_LIMIT = 5000

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid withdrawal amount")
#             return
        
#         if self._balance - amount < -self.OVERDRAFT_LIMIT:
#             print("Overdraft limit exceeded")
#             return
        
#         self._balance -= amount
#         self.transactions.append(f"Withdrawn: {amount}")
#         print(f"{amount} withdrawn successfully (Current)")
        
        
        
# # Create accounts
# savings = SavingsAccount("Albert", 5000)
# current = CurrentAccount("John", 2000)

# # Test Savings
# savings.deposit(1000)
# savings.withdraw(4500)   # should fail (min balance)
# savings.withdraw(3000)
# print("Savings Balance:", savings.get_balance())
# savings.show_transactions()

# # Test Current
# current.withdraw(6000)   # allowed (overdraft)
# current.withdraw(2000)   # may exceed limit
# print("Current Balance:", current.get_balance())
# current.show_transactions()


# project-2 library management 

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_available = True

    def __str__(self):
        return f"{self.book_id} - {self.title}"
    
    
class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} ({self.reader_id})"
    
class Library:
    def __init__(self):
        self.books = {}
        self.readers = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def register_reader(self, reader):
        self.readers[reader.reader_id] = reader

    def issue_book(self, book_id, reader_id):
        if book_id not in self.books:
            print("Book not available")
            return
        
        if reader_id not in self.readers:
            print("Invalid reader")
            return
        
        book = self.books[book_id]
        reader = self.readers[reader_id]

        if not book.is_available:
            print("Book already issued")
            return
        
        book.is_available = False
        reader.borrowed_books.append(book)
        print(f"{book.title} issued to {reader.name}")

    def return_book(self, book_id, reader_id):
        if book_id not in self.books or reader_id not in self.readers:
            print("Invalid book/reader")
            return
        
        book = self.books[book_id]
        reader = self.readers[reader_id]

        if book not in reader.borrowed_books:
            print("Reader didn't borrow this book")
            return
        
        book.is_available = True
        reader.borrowed_books.remove(book)
        print(f"{book.title} returned by {reader.name}")
        
library = Library()

# Add books
b1 = Book(1, "Python Basics")
b2 = Book(2, "Data Structures")

library.add_book(b1)
library.add_book(b2)

# Add user
u1 = Reader(101, "Albert")
library.register_reader(u1)

# Issue & Return
library.issue_book(1, 101)
library.issue_book(1, 101)   # should fail

library.return_book(1, 101)
library.return_book(1, 101)  # should fail

