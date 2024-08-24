import tkinter as tk
import code_source.win_widget as C 
# import test as t 
from tkinter import ttk
import customtkinter as Ct


root = tk.Tk()
root.configure(bg="#fff")
root.title("Onfaikw.")
root.geometry("450x700")
    
    


FrameOption=Ct.CTkFrame(root,
                        width=100,
                        height=100,
                        fg_color="#515151",
                        border_width=0,
                        corner_radius=20,
                        border_color="black"
                        )
FrameOption.place(x=25,y=55)
        
FrameOption.columnconfigure(0,weight=1)
FrameOption.rowconfigure(0,weight=0)
FrameOption.rowconfigure((1,2,3),weight=1) 
FrameOption.rowconfigure(4,weight=0) 



root.mainloop()