from tkinter import *

root = Tk()
root.title("frame 2")

styles = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

for bw in range(5):  # borderwidth từ 0 đến 4
    Label(root, text=f"borderwidth = {bw}").grid(row=bw, column=0, padx=5, pady=5)
    for i, style in enumerate(styles):
        Button(root, text=style, relief=style, borderwidth=bw, width=8).grid(row=bw, column=i+1, padx=5, pady=5)

root.mainloop()