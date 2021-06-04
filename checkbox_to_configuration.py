import tkinter as tk
from tkinter import ttk, Checkbutton, Button, BooleanVar
import json


def load_config(filename):
    with open(filename) as f:
        return json.load(f)

        
def write_config(filename):
    config = {'frame1': frame1_var.get(), 'frame2': frame2_var.get(), 'frame3': frame3_var.get()}
    with open(filename, "w") as f:
        json.dump(config, f, indent=4, sort_keys=True)

        
settings = load_config('config.json')

gui = tk.Tk()

frame1_var = BooleanVar(value=settings['frame1'])
checkbox_frame = ttk.Frame(gui)
checkbox_frame.pack()
frame1 = Checkbutton(checkbox_frame, text='frame1', variable=frame1_var)
frame1.pack()

frame2_var = BooleanVar(value=settings['frame2'])
checkbox_frame2 = ttk.Frame(gui)
checkbox_frame2.pack()
frame2 = Checkbutton(checkbox_frame, text='frame2', variable=frame2_var)
frame2.pack()

frame3_var = BooleanVar(value=settings['frame3'])
checkbox_frame3 = ttk.Frame(gui)
checkbox_frame3.pack()
frame3 = Checkbutton(checkbox_frame, text='frame3', variable=frame3_var)
frame3.pack()

button_frame = ttk.Frame(gui)
button_frame.pack()

button1 = Button(button_frame, text='Check', command=lambda: print(frame1_var.get(), frame2_var.get(), frame3_var.get()))
button1.pack()

button2 = Button(button_frame, text='Save', command=lambda: write_config("config.json"))
button2.pack()

gui.mainloop()

