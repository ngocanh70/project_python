# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 20:56:02 2025

@author: Bùi T Ngọc Ánh
"""

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"ID:{self.book_id} - {self.title} ({self.author}) - Còn {self.quantity} quyển"
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

class Borrower(Person):
    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self.borrowed_books = []

    def __str__(self):
        return f"ID:{self.person_id} - {self.name} - Đang mượn: {self.borrowed_books}"
class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    # Thêm sách
    def add_book(self, title, author, quantity):
        book_id = len(self.books) + 1
        self.books.append(Book(book_id, title, author, quantity))

    # Xem danh sách sách
    def show_books(self):
        for book in self.books:
            print(book)

    # Thêm người mượn
    def add_borrower(self, name):
        borrower_id = len(self.borrowers) + 1
        self.borrowers.append(Borrower(borrower_id, name))

    # Xem danh sách người mượn
    def show_borrowers(self):
        for br in self.borrowers:
            print(br)

    # Mượn sách
    def borrow_book(self, borrower_id, book_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        borrower = next((br for br in self.borrowers if br.person_id == borrower_id), None)

        if book and borrower and book.quantity > 0:
            book.quantity -= 1
            borrower.borrowed_books.append(book_id)
            print("✅ Mượn sách thành công!")
        else:
            print("❌ Không thể mượn sách!")

    # Trả sách
    def return_book(self, borrower_id, book_id):
        borrower = next((br for br in self.borrowers if br.person_id == borrower_id), None)
        if borrower and book_id in borrower.borrowed_books:
            borrower.borrowed_books.remove(book_id)
            book = next((b for b in self.books if b.book_id == book_id), None)
            if book:
                book.quantity += 1
            print("✅ Trả sách thành công!")
        else:
            print("❌ Không thể trả sách!")
library = Library()

while True:
    print("\n===== QUẢN LÝ THƯ VIỆN (OOP) =====")
    print("1. Thêm sách")
    print("2. Xem sách")
    print("3. Thêm người mượn")
    print("4. Xem người mượn")
    print("5. Mượn sách")
    print("6. Trả sách")
    print("0. Thoát")

    choice = input("Chọn: ")
    if choice == "1":
        title = input("Tên sách: ")
        author = input("Tác giả: ")
        quantity = int(input("Số lượng: "))
        library.add_book(title, author, quantity)
    elif choice == "2":
        library.show_books()
    elif choice == "3":
        name = input("Tên người mượn: ")
        library.add_borrower(name)
    elif choice == "4":
        library.show_borrowers()
    elif choice == "5":
        library.show_books()
        book_id = int(input("ID sách: "))
        library.show_borrowers()
        borrower_id = int(input("ID người mượn: "))
        library.borrow_book(borrower_id, book_id)
    elif choice == "6":
        library.show_borrowers()
        borrower_id = int(input("ID người trả: "))
        book_id = int(input("ID sách trả: "))
        library.return_book(borrower_id, book_id)
    elif choice == "0":
        break
    else:
        print("❌ Lựa chọn không hợp lệ!")
