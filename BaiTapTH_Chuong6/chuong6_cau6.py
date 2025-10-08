import random

# Nhập vào số lượng phần tử
N = int(input("Nhập số lượng phần tử N: "))

# Tạo list gồm N số ngẫu nhiên KHÔNG TRÙNG NHAU trong khoảng 0–100
lst = random.sample(range(0, 101), N)

# Xuất kết quả
print("Danh sách ngẫu nhiên:", lst)