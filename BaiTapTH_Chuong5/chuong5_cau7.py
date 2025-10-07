def toi_uu_danh_tu(s):
    # Bước 1: Xóa khoảng trắng đầu & cuối
    s = s.strip()
    # Bước 2: Tách từ (loại bỏ khoảng trắng dư thừa)
    words = s.split()
    # Bước 3: Viết hoa chữ đầu, còn lại viết thường
    words = [w.capitalize() for w in words]
    # Bước 4: Ghép lại thành chuỗi hoàn chỉnh
    return " ".join(words)


# --- Chương trình chính ---
chuoi = input("Nhập chuỗi danh từ: ")
chuoi_toi_uu = toi_uu_danh_tu(chuoi)
print("Chuỗi sau khi tối ưu:", chuoi_toi_uu)
