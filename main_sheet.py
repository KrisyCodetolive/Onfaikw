import tkinter as tk
import sheet_widget as sh
from tkinter import ttk
import customtkinter as Ct



def Main():
    
    root = tk.Tk()
    root.configure(bg="#fff")
    root.title("Onfaikw.")
    root.geometry("450x700")
    
    todo=sh.Menu(root)
   
   
   
    root.mainloop()
    
    
    


Main()