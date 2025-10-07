import math

# Nhập tọa độ điểm A
xA = float(input("Nhập hoành độ xA: "))
yA = float(input("Nhập tung độ yA: "))

# Nhập tọa độ điểm B
xB = float(input("Nhập hoành độ xB: "))
yB = float(input("Nhập tung độ yB: "))

# Tính độ dài đoạn AB
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Xuất kết quả
print("Độ dài đoạn AB là:", AB)
