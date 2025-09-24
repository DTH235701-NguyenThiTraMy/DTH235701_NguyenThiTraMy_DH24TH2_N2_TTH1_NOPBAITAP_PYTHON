def doc_so(n):
    don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 10:
        return don_vi[n]
    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + don_vi[n % 10]
    else:
        chuc = n // 10
        dv = n % 10
        ket_qua = don_vi[chuc] + " mươi"
        if dv == 0:
            return ket_qua
        elif dv == 1:
            return ket_qua + " mốt"
        elif dv == 5:
            return ket_qua + " lăm"
        else:
            return ket_qua + " " + don_vi[dv]

# --- Nhập số từ bàn phím ---
n = int(input("Nhập số n (0-99): "))

if 0 <= n <= 99:
    print("Cách đọc:", doc_so(n))
else:
    print("Vui lòng nhập số từ 0 đến 99")
