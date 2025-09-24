#giải thích cách chạy các dòng lệnh range
'''
(a) range(5) 
--> Hàm range(5) tạo ra một dãy số nguyên bắt đầu từ 0 đến 4 (không bao gồm 5).
Cụ thể, range(5) tương đương với dãy: 0, 1, 2, 3, 4

(b) range(5, 10)       
--> Hàm range(5, 10) tạo ra một dãy số nguyên bắt đầu từ 5 đến 9 (không bao gồm 10).
Cụ thể, range(5, 10) tương đương với dãy: 5, 6, 7, 8, 9

(c) range(5, 20, 3) 
--> Hàm range(5, 20, 3) tạo ra một dãy số nguyên bắt đầu từ 5 đến 19 (không bao gồm 20),
với bước nhảy là 3.
cụ thể: 5, 8, 11, 14, 17, 20

(d) range(20, 5, -1) 
--> Hàm range(20, 5, -1) tạo ra một dãy số nguyên bắt đầu từ 20 giảm dần đến lớn hơn 5,
với bước nhảy là -1 (giảm 1 mỗi lần lặp).
Cụ thể, dãy này là:
20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6

(e) range(20, 5, -3) 
--> Hàm range(20, 5, -3) tạo ra một dãy số nguyên bắt đầu từ 20 giảm dần đến lớn hơn 5,
với bước nhảy là -3 (giảm 3 mỗi lần lặp).
Cụ thể, dãy này là:
20, 17, 14, 11, 8

(f) range(10, 5) 
--> Hàm range(10, 5) tạo ra một dãy số nguyên bắt đầu từ 10 đến nhỏ hơn 5, với bước nhảy mặc định là 1 (tăng dần).
Vì 10 đã lớn hơn 5 và bước nhảy là dương, nên dãy này không có phần tử nào.
Cụ thể, range(10, 5) là một dãy rỗng: []

(g) range(0) 
--> Hàm range(0) tạo ra một dãy số bắt đầu từ 0 nhưng kết thúc ngay tại 0 (không bao gồm 0), 
nên không có phần tử nào.
Cụ thể, range(0) là một dãy rỗng:[]

(h) range(10, 101, 10) 
-->Hàm range(10, 101, 10) tạo ra một dãy số nguyên bắt đầu từ 10 đến nhỏ hơn 101, 
với bước nhảy là 10.
Cụ thể, dãy này là: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

(i) range(10, -1, -1) 
--> Hàm range(10, -1, -1) tạo ra một dãy số nguyên bắt đầu từ 10, giảm dần, mỗi lần giảm 1, 
và dừng lại khi nhỏ hơn -1 (không bao gồm -1).
Cụ thể, dãy này là: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0

tương tự
(j) range(-3, 4) 
--> -3, -2, -1, 0, 1, 2, 3

(k) range(0, 10, 1)
-->0, 1, 2, 3, 4, 5, 6, 7, 8, 9

'''