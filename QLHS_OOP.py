# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 09:16:38 2025
@author: Bùi T Ngọc Ánh
"""

class Diem:
    def __init__(self, toan, van, anh):
        self.toan = toan
        self.van = van
        self.anh = anh

    def tinh_tb(self):
        return round((self.toan + self.van + self.anh) / 3, 2)

    def xeploai(self):
        tb = self.tinh_tb()
        if tb >= 8.5:
            return "Giỏi"
        elif tb >= 7:
            return "Khá"
        elif tb >= 5.5:
            return "Trung bình"
        elif tb >= 4:
            return "Yếu"
        else:
            return "Kém"

    def __str__(self):
        return f"Toán: {self.toan} - Văn: {self.van} - Anh: {self.anh} | TB: {self.tinh_tb()} | Xếp loại: {self.xeploai()}"


class Student:
    def __init__(self, stu_id, fullname, birthday, diem: Diem):
        self.stu_id = stu_id
        self.fullname = fullname
        self.birthday = birthday
        self.diem = diem

    def __str__(self):
        return f"Mã HS: {self.stu_id} - Tên: {self.fullname} - Năm sinh: {self.birthday} | {self.diem}"


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_stu(self, stu_id):
        self.students = [s for s in self.students if s.stu_id != stu_id]

    def list_students(self):
        if not self.students:
            print("Danh sách rỗng.")
        else:
            for s in self.students:
                print(s)

    def find_student_by_id(self, stu_id):
        for s in self.students:
            if s.stu_id == stu_id:
                return s
        return None


# Chương trình chính
school = School()

while True:
    print("\n---- Quản lý học sinh ----")
    print("1. Thêm học sinh")
    print("2. Xóa học sinh")
    print("3. Xem danh sách học sinh")
    print("4. Tìm kiếm học sinh theo ID")
    print("0. Thoát")
    choice = input("Chọn: ")

    if choice == "1":
        stu_id = input("Mã HS: ")
        fullname = input("Họ tên: ")
        birthday = input("Năm sinh: ")
        toan = float(input("Điểm Toán: "))
        van = float(input("Điểm Văn: "))
        anh = float(input("Điểm Anh: "))
        d = Diem(toan, van, anh)
        s = Student(stu_id, fullname, birthday, d)
        school.add_student(s)
        print("Đã thêm học sinh!")

    elif choice == "2":
        stu_id = input("Nhập mã HS cần xóa: ")
        school.remove_stu(stu_id)
        print("Đã xóa!")

    elif choice == "3":
        school.list_students()

    elif choice == "4":
        stu_id = input("Nhập mã HS cần tìm: ")
        found = school.find_student_by_id(stu_id)
        if found:
            print("Thông tin học sinh:")
            print(found)
        else:
            print("Không tìm thấy học sinh!")

    elif choice == "0":
        break

    else:
        print("Lựa chọn không hợp lệ.")
