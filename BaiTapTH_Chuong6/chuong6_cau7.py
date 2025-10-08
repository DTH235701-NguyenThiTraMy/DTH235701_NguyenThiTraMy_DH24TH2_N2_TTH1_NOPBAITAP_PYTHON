def nhap_day_tang():
    while True:
        s = input("Nhập dãy số cách nhau bằng dấu cách: ")
        try:
            lst = [int(x) for x in s.split()]
            
            # Kiểm tra dãy có tăng dần hay không
            if all(lst[i] < lst[i+1] for i in range(len(lst)-1)):
                print("Dãy hợp lệ:", lst)
                break
            else:
                print("Dãy không tăng dần, vui lòng nhập lại!\n")
        except ValueError:
            print("Lỗi: chỉ được nhập số nguyên, vui lòng nhập lại!\n")

# Gọi hàm
nhap_day_tang()