import tkinter as tk
import widget as C 
# import test as t 
from tkinter import ttk
import customtkinter as Ct



def Main():
    
    root = tk.Tk()
    root.configure(bg="#fff")
    root.title("Onfaikw.")
    root.geometry("450x700")
    
    # color=C.Color(("#FBE5CB","#F28181","#949393"),(50,50),root)
    # print(color.get_Color())
    color=C.Option(root,(10,10))
    # color=t.Color(("#FBE5CB","#F28181","#949393"),(50,50),root)
    root.mainloop()
    
    
    


Main()