'''
a=101
while a < 100:
    print('*', end ='')
print()

Phân tích:
Biến a khởi tạo = 0.
Trong vòng lặp while a < 100: → điều kiện đúng (0 < 100).
Nhưng trong thân vòng lặp không hề có câu lệnh a = a + 1 để tăng giá trị của a.

Kết quả:
a luôn bằng 0 → điều kiện a < 100 luôn đúng → vòng lặp chạy vô hạn.
Nghĩa là chương trình sẽ in ra vô hạn dấu * liên tiếp, không dừng.

'''
print("Kết luận: Số dấu * in ra là vô hạn (không đếm được).")