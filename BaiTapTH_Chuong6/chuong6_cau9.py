# Hàm kiểm tra số nguyên tố
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập dãy số tự nhiên từ bàn phím
s = input("Nhập dãy số (các số cách nhau bằng dấu cách): ")
M = [int(x) for x in s.split()]

# Phân loại
le = [x for x in M if x % 2 != 0]
chan = [x for x in M if x % 2 == 0]
nguyen_to = [x for x in M if la_nguyen_to(x)]
khong_nguyen_to = [x for x in M if not la_nguyen_to(x)]

# Xuất kết quả
print("\n📋 Kết quả xử lý mảng:")
print("Dãy số lẻ:", le, f"→ Có {len(le)} số lẻ")
print("Dãy số chẵn:", chan, f"→ Có {len(chan)} số chẵn")
print("Dãy số nguyên tố:", nguyen_to)
print("Dãy số không phải nguyên tố:", khong_nguyen_to)