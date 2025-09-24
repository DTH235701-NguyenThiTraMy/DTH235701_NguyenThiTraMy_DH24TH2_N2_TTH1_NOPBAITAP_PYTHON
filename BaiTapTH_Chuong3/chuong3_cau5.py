def check_values(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, " j =", j, " k =", k)

# Các bộ giá trị cần kiểm tra
cases = [
    ("(a)", 3, 5, 7),
    ("(b)", 3, 7, 5),
    ("(c)", 5, 3, 7),
    ("(d)", 5, 7, 3),
    ("(e)", 7, 3, 5),
    ("(f)", 7, 5, 3)
]

# Chạy và in kết quả
for label, i, j, k in cases:
    print(label, end=" ")
    check_values(i, j, k)
