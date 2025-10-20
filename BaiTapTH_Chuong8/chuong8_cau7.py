from tkinter import *

# Danh sách 10 Thiên Can và 12 Địa Chi
CAN = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
CHI = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

# Hàm chuyển đổi năm
def chuyen_doi():
    try:
        nam_duong = int(entry_nam.get())
        can = CAN[nam_duong % 10]
        chi = CHI[nam_duong % 12]
        lbl_am.config(text=f"{can} {chi}")
    except:
        lbl_am.config(text="Năm không hợp lệ!")

# Giao diện chính
root = Tk()
root.title("Chuyển Năm Dương Lịch Sang Âm Lịch")
root.geometry("350x180")
root.config(bg="yellow")

# Nhãn và ô nhập
Label(root, text="Nhập năm dương:", bg="yellow", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky=W)
entry_nam = Entry(root, fg="red", font=("Arial", 11))
entry_nam.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Năm âm:", bg="yellow", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky=W)
lbl_am = Label(root, text="", bg="yellow", fg="black", font=("Arial", 11, "bold"))
lbl_am.grid(row=1, column=1, padx=10, pady=10)

# Nút chuyển
btn = Button(root, text="Chuyển", bg="blue", fg="white", font=("Arial", 11, "bold"), command=chuyen_doi)
btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
