import tkinter as tk
from tkinter import messagebox, simpledialog
import keyboard
import sys
sys.executable = "python"

window = tk.Tk()
window.title("Pull count")
window.geometry("500x300")

count = 0

def add():
    global count
    count += 1
    count_label.config(text=f"Count: {count}")

    if count % 15 == 0:
        messagebox.showinfo("Popup", "Euryxx lache la manette !")

def reset():
    global count
    boss_name = simpledialog.askstring("Pseudo du Boss", "Entrez le pseudo du boss:")
    if boss_name is not None:
        with open("boss_count.txt", "a") as file:
            file.write(f"Pseudo du boss : {boss_name}, Count : {count}\n")
        count = 0
        count_label.config(text=f"Count: {count}")
        last_5_counts_label.config(text="")

        with open("boss_count.txt", "r") as file:
            lines = file.readlines()
            last_5_counts = lines[::-1]
            last_5_counts = last_5_counts[:5]
            last_5_counts_label.config(text="\n".join(last_5_counts))

def on_key_press(e):
    if e.event_type == keyboard.KEY_DOWN and e.name.lower() == "+":
        add()

add_button = tk.Button(window, text="Add or press '+'", command=add)
add_button.pack()

reset_button = tk.Button(window, text="Reset", command=reset)
reset_button.pack()

count_label = tk.Label(window, text=f"Count: {count}", font=("Helvetica", 24))
count_label.pack()

last_5_counts_label = tk.Label(window, text="", font=("Helvetica", 12))
last_5_counts_label.pack(side="bottom")

keyboard.hook(on_key_press)

with open("boss_count.txt", "r") as file:
    lines = file.readlines()
    last_5_counts = lines[::-1]
    last_5_counts = last_5_counts[:5]
    last_5_counts_label.config(text="\n".join(last_5_counts))

window.mainloop()


