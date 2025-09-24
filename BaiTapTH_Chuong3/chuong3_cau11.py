print("Chương trình kiểm tra số nguyên tố")
while True: 
    n=int(input("Nhập 1 số nguyên dương: ")) 
    dem=0 
    for i in range(1,n+1): 
         if n % i ==0 : 
            dem+=1 
    if dem==2: 
        print(n,"Là số nguyên tố") 
    else: 
        print(n,"Không là số nguyên tố") 
    hoi=input("Bạn có muốn kiểm tra tiếp không?(c/k):") 
    if hoi is "k": 
        break 
print("BYE!")