import math

# Nhập n
n = int(input("Nhập n: "))

# Bắt đầu tính từ trong ra ngoài
S = math.sqrt(2)  # căn trong cùng
for i in range(1, n):  # lặp n-1 lần nữa
    S = math.sqrt(2 + S)

# Xuất kết quả
print(f"S({n}) = {S}")
