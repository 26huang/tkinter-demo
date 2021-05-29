import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Cambria", 12)

class MainGui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
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
