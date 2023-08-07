import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Pull count")
window.geometry("500x200")


count = 0

def add():
    global count
    count += 1
    count_label.config(text=f"Count: {count}")

    if count % 15 == 0:
        messagebox.showinfo("Popup", "Euryxx lache la manette !")

def on_key_press(event):
    if event.char.lower() == "+":
        add()

add_button = tk.Button(window, text="Add or press '+'", command=add)
add_button.pack()

count_label = tk.Label(window, text=f"Count: {count}", font=("Helvetica", 24))
count_label.pack()

window.bind("<KeyPress>", on_key_press)

window.mainloop()