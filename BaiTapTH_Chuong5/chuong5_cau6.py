import re

def NegativeNumberInStrings(s):
    # Tìm tất cả các số âm: dấu trừ '-' theo sau là ít nhất 1 chữ số
    numbers = re.findall(r'-\d+', s)
    # In từng số âm tìm được
    for num in numbers:
        print(num)

chuoi = input("Nhập chuỗi: ")
print("Các số nguyên âm trong chuỗi là:")
NegativeNumberInStrings(chuoi)