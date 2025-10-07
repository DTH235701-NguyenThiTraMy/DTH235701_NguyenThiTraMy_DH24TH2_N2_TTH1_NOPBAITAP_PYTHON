#Cho 3 hàm
def sum1(n): 
    s = 0 
    while n > 0: 
        s += 1 
        n -= 1 
    return s 
def sum2(): 
    global val 
    s = 0 
    while val > 0: 
        s += 1 
        val -= 1 
    return s 
def sum3(): 
    s = 0 
    for i in range(val, 0, -1): 
        s += 1 
    return s

#Trường hợp 1
def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum2()) 
    print(sum3()) 
main()
"""
Kết quả in ra:
5
5
0
"""

#Trường hợp 2
def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum3()) 
    print(sum2()) 
main()

"""Kết quả in ra:
5
5
5
"""

#Trường hợp 3
def main(): 
    global val 
    val = 5 
    print(sum2()) 
    print(sum1(5)) 
    print(sum3()) 
main()

"""Kết quả in ra:
5
0
5
"""

'''
Tổng kết:
sum1(n) → chỉ phụ thuộc vào tham số n, không ảnh hưởng val.

sum2() → làm giảm val về 0.

sum3() → phụ thuộc vào val hiện tại (nhưng không thay đổi nó).

👉 Vì vậy:

Nếu sum2() chạy trước sum3() → sum3() sẽ ra 0.

Nếu sum3() chạy trước sum2() → sum3() sẽ ra 5.
'''