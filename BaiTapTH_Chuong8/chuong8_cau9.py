from tkinter import *
from tkinter import messagebox

def tinh_bmi():
    try:
        chieu_cao = float(entry_cao.get())
        can_nang = float(entry_can.get())
        bmi = can_nang / (chieu_cao ** 2)
        entry_bmi.delete(0, END)
        entry_bmi.insert(0, f"{bmi:.2f}")

        # Phân loại BMI
        if bmi < 18.5:
            tinh_trang = "Gầy"
            nguy_co = "Thấp"
        elif bmi < 24.9:
            tinh_trang = "Bình thường"
            nguy_co = "Trung bình"
        elif bmi < 29.9:
            tinh_trang = "Hơi béo"
            nguy_co = "Hơi cao"
        else:
            tinh_trang = "Béo phì"
            nguy_co = "Rất cao"

        entry_tinhtrang.delete(0, END)
        entry_tinhtrang.insert(0, tinh_trang)

        entry_nguyco.delete(0, END)
        entry_nguyco.insert(0, nguy_co)

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số!")

def thoat():
    root.destroy()

# Giao diện chính
root = Tk()
root.title("Phần mềm tính BMI")
root.geometry("360x350")
root.config(bg="yellow")

# --- Các nhãn và ô nhập ---
Label(root, text="Nhập chiều cao:", bg="yellow", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky=W)
entry_cao = Entry(root, fg="red", font=("Arial", 11))
entry_cao.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Nhập cân nặng:", bg="yellow", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky=W)
entry_can = Entry(root, fg="red", font=("Arial", 11))
entry_can.grid(row=1, column=1, padx=10, pady=10)

# Nút tính BMI
btn_tinh = Button(root, text="Tính BMI", bg="blue", fg="white", font=("Arial", 11, "bold"),
                  padx=15, pady=5, relief="groove", borderwidth=6, command=tinh_bmi)
btn_tinh.grid(row=2, column=0, columnspan=2, pady=10)

# Kết quả
Label(root, text="BMI của bạn:", bg="yellow", font=("Arial", 11)).grid(row=3, column=0, padx=10, pady=5, sticky=W)
entry_bmi = Entry(root, font=("Arial", 11))
entry_bmi.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Tình trạng của bạn:", bg="yellow", font=("Arial", 11)).grid(row=4, column=0, padx=10, pady=5, sticky=W)
entry_tinhtrang = Entry(root, font=("Arial", 11))
entry_tinhtrang.grid(row=4, column=1, padx=10, pady=5)

Label(root, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("Arial", 11)).grid(row=5, column=0, padx=10, pady=5, sticky=W)
entry_nguyco = Entry(root, font=("Arial", 11))
entry_nguyco.grid(row=5, column=1, padx=10, pady=5)

# Nút thoát
btn_thoat = Button(root, text="Thoát", bg="steelblue", fg="white", font=("Arial", 11, "bold"),
                   padx=15, pady=5, relief="groove", borderwidth=6, command=thoat)
btn_thoat.grid(row=6, column=0, columnspan=2, pady=15)

root.mainloop()