# Nhập giá trị a, b và phép toán
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Nhập phép toán (+, -, *, /): ")

# Xử lý phép toán
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b != 0:
        result = a / b
    else:
        result = "Lỗi: Không thể chia cho 0"
else:
    result = "Phép toán không hợp lệ!"

# Xuất kết quả
print("Kết quả:", result)
