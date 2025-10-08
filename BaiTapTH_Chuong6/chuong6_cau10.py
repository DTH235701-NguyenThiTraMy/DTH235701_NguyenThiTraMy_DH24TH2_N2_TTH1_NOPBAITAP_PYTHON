# hàm nhập ma trận
def nhap_matrix(ten):
    hang = int(input(f"Nhập số hàng của ma trận {ten}: "))
    cot = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    matrix = []
    for i in range(hang):
        row = [float(x) for x in input(f"Hàng {i+1}: ").split()]
        while len(row) != cot:
            print("Số phần tử không khớp, nhập lại hàng này!")
            row = [float(x) for x in input(f"Hàng {i+1}: ").split()]
        matrix.append(row)
    return matrix

# cộng
def cong_matrix(A, B):
    hang = len(A)
    cot = len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(cot)] for i in range(hang)]
    return C

# hoán vị
def hoan_vi_matrix(M):
    hang = len(M)
    cot = len(M[0])
    return [[M[j][i] for j in range(hang)] for i in range(cot)]

# Nhập 2 ma trận A và B
A = nhap_matrix("A")
B = nhap_matrix("B")

# Cộng 2 ma trận
print("\n🔹 Ma trận tổng (A + B):")
C = cong_matrix(A, B)
for row in C:
    print(row)

# Hoán vị A và B
print("\n🔹 Ma trận hoán vị của A:")
for row in hoan_vi_matrix(A):
    print(row)

print("\n🔹 Ma trận hoán vị của B:")
for row in hoan_vi_matrix(B):
    print(row)