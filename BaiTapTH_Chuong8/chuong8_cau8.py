from tkinter import *

def chuyen_doi():
    try:
        f = float(entry_f.get())
        c = (f - 32) * 5 / 9
        lbl_ketqua.config(text=f"{c:.2f} °C")
    except:
        lbl_ketqua.config(text="Giá trị không hợp lệ!")

root = Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("300x160")
root.config(bg="lightyellow")

# Label và Entry nhập độ F
Label(root, text="Nhập độ F:", bg="lightyellow", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky=W)
entry_f = Entry(root, fg="red", font=("Arial", 11))
entry_f.grid(row=0, column=1, padx=10, pady=10)

# Nút chuyển đổi (tạo cảm giác bo tròn)
btn_chuyen = Button(
    root, 
    text="Chuyển", 
    bg="blue", 
    fg="white", 
    font=("Arial", 11, "bold"),
    relief="groove",           # tạo viền mềm
    borderwidth=5,             # làm dày viền
    highlightthickness=0,      # bỏ viền sáng
)
btn_chuyen.grid(row=1, column=0, columnspan=2, pady=10)
btn_chuyen.config(command=chuyen_doi)

# Label kết quả
Label(root, text="Độ C:", bg="lightyellow", font=("Arial", 11)).grid(row=2, column=0, padx=10, sticky=W)
lbl_ketqua = Label(root, text="", bg="lightyellow", fg="green", font=("Arial", 11, "bold"))
lbl_ketqua.grid(row=2, column=1, padx=10)

root.mainloop()