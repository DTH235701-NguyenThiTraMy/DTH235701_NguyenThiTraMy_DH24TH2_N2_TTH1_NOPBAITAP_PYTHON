'''
🧩 Một số hàm quan trọng trong xử lý chuỗi của Python

🟢 1. Hàm loại bỏ khoảng trắng
Hàm	                Chức năng	                            Ví dụ
strip()	    Xóa khoảng trắng ở đầu và cuối chuỗi	" Hello ".strip() → "Hello"
lstrip()	Xóa khoảng trắng ở bên trái	            " Hello".lstrip() → "Hello"
rstrip()	Xóa khoảng trắng ở bên phải	            "Hello ".rstrip() → "Hello"


🟢 2. Hàm tách và nối chuỗi
Hàm	                        Chức năng	                                 Ví dụ
replace(old, new)	Thay thế đoạn chuỗi con	                "xin chao".replace("chao", "chào") → "xin chào"
split(sep)	        Tách chuỗi thành list các từ	        "a,b,c".split(",") → ['a', 'b', 'c']
join(list)	        Ghép list các chuỗi thành 1 chuỗi	    " ".join(['xin', 'chào']) → "xin chào"

🟢 3. Hàm thay đổi kiểu chữ
Hàm	                    Chức năng	                            Ví dụ
lower()	        Chuyển về chữ thường	                "Hello".lower() → "hello"
upper()	        Chuyển về chữ hoa	                    "Hello".upper() → "HELLO"
title()	        Viết hoa chữ cái đầu mỗi từ	            "xin chao ban".title() → "Xin Chao Ban"
capitalize()	Viết hoa chữ cái đầu tiên của chuỗi	    "xin chao".capitalize() → "Xin chao"

🟢 4. Hàm kiểm tra nội dung chuỗi
    isalpha, isdigit, isalnum, startswith, endswith
🟢 5. Hàm tìm kiếm
    find, rfind, index, rindex, count
'''