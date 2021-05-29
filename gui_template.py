import tkinter as tk
from tkinter import ttk, Menu, messagebox
import time
import threading

LARGE_FONT = ("Cambria", 12)

class MainGui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.DELAY_VALUE = 3
        
        self.wm_title("Gui Demo")
        
        menu = Menu(self) 
        item_one = Menu(menu) 
        item_one.add_command(label='New', command=lambda: self.clicked()) 
        item_one.add_command(label='Save', command=lambda: threading.Thread(target=self.clicked, args=(self.DELAY_VALUE,)).start())

        item_one.add_command(label='Save As', command=lambda: self.clicked())
        item_one.add_command(label='exit', command=lambda: self.clicked()) 
        menu.add_cascade(label='File', menu=item_one) 
        
        item_two = Menu(menu)
        item_two.add_command(label='Help', command=lambda: self.clicked())
        item_two.add_command(label='About Me', command=lambda: self.clicked())
        menu.add_cascade(label='Help', menu=item_two)
        self.config(menu=menu)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def clicked(self, sec=0):
        time.sleep(sec)
        messagebox.showinfo(title='Information', message='Clicked!')
        
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="tk Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        label = ttk.Label(self, text="ttk Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="ttk Visit Page One", command=lambda: controller.show_frame(PageOne))
        button.pack()
        
        button = tk.Button(self, text="tk Visit Page Two", command=lambda: controller.show_frame(PageTwo))
        button.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="Visit Home Page", command=lambda: controller.show_frame(StartPage))
        button.pack()
        
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="Visit Home Page", command=lambda: controller.show_frame(StartPage))
        button.pack()
        
app = MainGui()
app.mainloop()
