import pyautogui
import tkinter as tk
import keyboard

def quit_program():
    root.destroy()

root = tk.Tk()
root.attributes("-topmost", True)
root.resizable(False, False)
a = 3

color_label = tk.Label(root, text="Цвет")
color_label.pack()

def update_color():
    x, y = pyautogui.position()
    color = pyautogui.screenshot().getpixel((x, y))
    color_label.config(text=f"Цвет: {color}")
    root.geometry(f"+{x+2}+{y+2}")
    root.after(50, update_color)

update_color()

keyboard.add_hotkey('ctrl+alt+m', lambda: quit_program())

root.mainloop()
