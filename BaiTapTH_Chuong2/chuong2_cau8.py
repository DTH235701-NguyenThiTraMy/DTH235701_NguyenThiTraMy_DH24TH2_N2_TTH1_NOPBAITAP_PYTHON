#Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python. 

'''
1. Các loại lỗi khi lập trình Python
    a) Lỗi cú pháp (Syntax Error)
        - Do viết sai quy tắc ngôn ngữ.
        - Python báo lỗi ngay khi chạy.
    print("Hello"   # thiếu dấu đóng ngoặc
    ==>Báo lỗi: SyntaxError: unexpected EOF while parsing

    b) Lỗi runtime (Runtime Error / Exception)
        - Code chạy được nhưng gặp lỗi trong quá trình thực thi.
        Ví dụ: chia cho 0, nhập sai kiểu dữ liệu…
        x = 10 / 0
    ==>Báo lỗi: ZeroDivisionError: division by zero

    c) Lỗi logic (Logic Error)
        - Code chạy bình thường không báo lỗi, nhưng kết quả sai so với mong muốn.
        ví dụ: Muốn tính diện tích hình chữ nhật nhưng nhầm công thức
                    dai, rong = 5, 3
                    s = dai + rong   # sai, lẽ ra phải là dai * rong
                    print(s)         # Kết quả 8, nhưng đúng phải là 15

'''