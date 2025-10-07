import math

# Nhập a và x từ bàn phím
a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

# Kiểm tra điều kiện hợp lệ
if a > 0 and a != 1 and x > 0:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x}")
else:
    print("Giá trị không hợp lệ! Cần có: a > 0, a ≠ 1, x > 0.")
