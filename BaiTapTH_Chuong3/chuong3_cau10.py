print("Chương trình tính biểu thức S(x,n) = x + (x^2/2!) + (x^3/3!) +...+ (x^n/n!) ")
x=int(input("Nhập x: ")) 
n=int(input("Nhập N: ")) 
s=0 
for i in range(1,n+1): 
    tu=x**i 
    mau=1 
    for j in range(1,i+1): 
        mau=mau*j 
    s=s+(tu/mau) 
print("s({0},{1}) = {2}".format(x,n,s)) 