import tkinter as tk
from tkinter import messagebox
import time
import winsound

working = True

def chronometer(s):
    global working

    root = tk.Tk()
    root.title("Pomodoro Timer")
    label = tk.Label(root, text=f"Remaining time: {s} seconds.")
    label.pack()

    for i in range (s, 0, -1):
        label.config(text=f"Remaining time: {i} seconds.")
        root.update()
        time.sleep(1)

    play_bell_sound()

    label.config(text=f"Time has ended.")

    data = {"¡Pomodoro Timer!", "Stop working."} if working else {"¡Pomodoro Timer!", "Go to work!"}
    messagebox.showinfo(*data)

    working = not working

    root.withdraw()

def play_bell_sound():
    winsound.Beep(1000, 1000)

while(True):
    desired_time = 15 * 60 if working else 5 * 60
    chronometer(desired_time)