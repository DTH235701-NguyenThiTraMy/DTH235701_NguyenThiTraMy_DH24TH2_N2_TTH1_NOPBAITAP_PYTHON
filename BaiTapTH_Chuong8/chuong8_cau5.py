from tkinter import *
from tkinter import messagebox

def doi_mat_khau():
    old_pw = old_password.get()
    new_pw = new_password.get()
    re_pw = re_password.get()

    if old_pw == "" or new_pw == "" or re_pw == "":
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
    elif new_pw != re_pw:
        messagebox.showerror("Lỗi", "Mật khẩu nhập lại không trùng khớp!")
    else:
        messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")

def huy():
    root.destroy()

# Tạo cửa sổ chính
root = Tk()
root.title("Đổi mật khẩu")
root.geometry("300x200")

Label(root, text="Old Password:").grid(row=0, column=0, padx=10, pady=5, sticky=E)
Label(root, text="New Password:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
Label(root, text="Enter New Password Again:").grid(row=2, column=0, padx=10, pady=5, sticky=E)

old_password = Entry(root, show="*", width=25)
new_password = Entry(root, show="*", width=25)
re_password = Entry(root, show="*", width=25)

old_password.grid(row=0, column=1, padx=10, pady=5)
new_password.grid(row=1, column=1, padx=10, pady=5)
re_password.grid(row=2, column=1, padx=10, pady=5)

Button(root, text="OK", width=10, command=doi_mat_khau).grid(row=3, column=0, pady=15)
Button(root, text="Cancel", width=10, command=huy).grid(row=3, column=1)

root.mainloop()