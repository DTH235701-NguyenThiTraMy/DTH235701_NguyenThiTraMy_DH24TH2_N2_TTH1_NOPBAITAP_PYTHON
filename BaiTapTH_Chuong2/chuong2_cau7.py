#Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím. 

'''
1. Hàm input() (cơ bản nhất)
Dùng để nhập dữ liệu dưới dạng chuỗi (str).
ví dụ:  name = input("Nhập tên của bạn: ")
        print("Xin chào,", name)

2. Ép kiểu khi nhập
Vì input() trả về chuỗi, nên muốn nhập số phải ép kiểu
    2.1 Số nguyên (int)
        age = int(input("Nhập tuổi: "))
        print("Tuổi của bạn là:", age)
    2.2 Số thực (float)
        score = float(input("Nhập điểm trung bình: "))
        print("Điểm trung bình:", score)

3. Nhập nhiều giá trị trên một dòng
Dùng split() để tách dữ liệu, rồi ép kiểu nếu cần.
ví dụ:  a, b = map(int, input("Nhập hai số cách nhau bởi dấu cách: ").split())
        print("Tổng =", a + b)

4. Nhập danh sách nhiều phần tử
Dùng list() kết hợp với map().

numbers = list(map(int, input("Nhập các số: ").split()))
print("Danh sách:", numbers)

'''