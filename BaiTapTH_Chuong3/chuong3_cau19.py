def S(x, n):
    term = x
    total = term
    for k in range(0, n):
        term = term * x * x / ((2*k + 2) * (2*k + 3))
        total += term
    return total

print('Tính giá trị biểu thức: S(x,n) = x + (x^3/3!) + (x^5/5!) +...+ (x^2n+1/(2n+1)!)')
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
print("S(x,n) =", S(x, n))
