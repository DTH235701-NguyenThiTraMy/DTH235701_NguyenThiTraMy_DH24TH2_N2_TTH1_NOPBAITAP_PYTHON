#code ban đầu
'''
done = False
n, m = 0, 100
while not done and n != m:
    n = int(input())
    if n < 0:
        done = True
    print("n =", n)
'''

#code viết bằng break
n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print("n =", n)