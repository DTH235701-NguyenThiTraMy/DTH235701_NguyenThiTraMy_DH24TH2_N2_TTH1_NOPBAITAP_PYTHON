'''def fibonacci(n): 
    if n<=2 : 
        return 1 
    return fibonacci(n-1)+fibonacci(n-2) 
 
def listfibo(n): 
    for i in range(1,n+1): 
        print(fibonacci(i),end='\t') 
 
print(fibonacci(9)) 
 
listfibo(9) '''
# Hàm 1: Trả về số Fibonacci tại vị trí thứ n
def fib_n(n):
    if n <= 0:
        return None  # trường hợp không hợp lệ
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_n(n - 1) + fib_n(n - 2)

# Hàm 2: Trả về danh sách Fibonacci từ 1 -> n
def fib_list(n):
    return [fib_n(i) for i in range(1, n + 1)]


N = int(input("Nhập N: "))
print(f"Số Fibonacci tại vị trí {N} là:", fib_n(N))
print(f"Dãy Fibonacci từ 1 đến {N} là:", fib_list(N))
