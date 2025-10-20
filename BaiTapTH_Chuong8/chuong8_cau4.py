from tkinter import *

def click_button(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Giao diện chính
root = Tk()
root.title("Máy tính bỏ túi")

entry = Entry(root, width=20, font=("Arial", 16), justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Các nút số và phép toán
buttons = [
    ('1',1,0), ('2',1,1), ('3',1,2),
    ('4',2,0), ('5',2,1), ('6',2,2),
    ('7',3,0), ('8',3,1), ('9',3,2),
    ('0',4,1), ('.',4,2), ('-',4,0),
    ('+',5,0), ('*',5,1), ('/',5,2),
    ('=',6,2), ('Clr',6,0)
]

for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'Clr':
        Button(root, text=text, width=5, height=2, command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=5, height=2, command=lambda t=text: click_button(t)).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
