def toi_uu_chuoi(s):
    # Loại bỏ khoảng trắng ở đầu & cuối, tách từ bằng split()
    # rồi ghép lại bằng một khoảng trắng duy nhất
    s = s.strip()
    s = " ".join(s.split())
    return s

# --- Chương trình chính ---
chuoi = input("Nhập chuỗi: ")
chuoi_toi_uu = toi_uu_chuoi(chuoi)
print("Chuỗi sau khi tối ưu:", chuoi_toi_uu)
