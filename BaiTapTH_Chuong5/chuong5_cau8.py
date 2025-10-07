import os

def lay_ten_file_duoi(path):
    # Lấy tên file + phần mở rộng
    return os.path.basename(path)

def lay_ten_file_khong_duoi(path):
    # Lấy tên file, bỏ phần mở rộng
    return os.path.splitext(os.path.basename(path))[0]

# --- Chương trình chính ---
duong_dan = input("Nhập đường dẫn file nhạc: ")

print("Tên file (có phần mở rộng):", lay_ten_file_duoi(duong_dan))
print("Tên file (không có phần mở rộng):", lay_ten_file_khong_duoi(duong_dan))