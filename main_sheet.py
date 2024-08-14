import tkinter as tk
import widget as C 
from tkinter import ttk
import customtkinter as Ct



def Main():
    
    root = tk.Tk()
    root.configure(bg="#fff")
    root.title("Onfaikw.")
    root.geometry("450x700")
    
    color=C.Color(("#FF5733","#33FF57","#3357FF"),(50,50),root)
    root.mainloop()
    
    
    


Main()