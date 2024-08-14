import tkinter as tk
from tkinter import ttk
import customtkinter as Ct


class Color(Ct.CTk):
    
    def __init__(self,bg,coor,Root):
        super().__init__()
        
        self.bg=bg
        self.coor=coor
        
        
        
        self.Frame=Ct.CTkFrame(Root,width=200,
                              height=50,
                              fg_color="#fff",
                              border_width=0,
                              border_color="white"
                              )
        
        self.Frame.place(x=self.coor[0],
                         y=self.coor[1])
        
        self.Frame.columnconfigure((0,1,2),weight=1)
        self.Frame.rowconfigure(0,weight=1)
        
        self.color1=Ct.CTkFrame(
                        self.Frame,
                        width=60,
                        height=40,
                        fg_color=self.bg[0],
                        border_width=3,
                        border_color="#3357FF",
                        corner_radius=30
                        )
        self.color1.grid(row=0,column=0,padx=4,pady=4)
        
        
        self.color2=Ct.CTkFrame(
                        self.Frame,
                        width=60,
                        height=40,
                        fg_color=self.bg[1],
                        border_width=3,
                        border_color=self.bg[1],
                        corner_radius=30
                        )
        self.color2.grid(row=0,column=1,padx=4,pady=4)
        
        
        self.color3=Ct.CTkFrame(
                        self.Frame,
                        width=60,
                        height=40,
                        fg_color=self.bg[2],
                        border_width=3,
                        border_color=self.bg[2],
                        corner_radius=30
                        )
        self.color3.grid(row=0,column=2,padx=4,pady=4)
        
        
        
# root = tk.Tk()

# root.configure(bg="#fff")
# root.title("Onfaikw.")
# # root.geometry("450x700")
# root.geometry("340x130")

# color=Color(root)


# root.mainloop()


    