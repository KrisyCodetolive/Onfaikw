import tkinter as tk
from tkinter import ttk
import customtkinter as Ct


# widget Color
        
class Color:
    
    def __init__(self,bg,coor,Root):
        
        
        self.bg=bg
        self.coor=coor
        
        self.taille=(40,30) 
        self.Select="#1C77BD"
        self.unSelect=(self.bg[0],self.bg[1],self.bg[2])
        
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
                        width=self.taille[0],
                        height=self.taille[1],
                        fg_color=self.bg[0],
                        border_width=2.7,
                        border_color=self.Select,
                        corner_radius=30
                        )
        self.color1.grid(row=0,column=0,padx=4,pady=4)
        self.color1.bind("<Button-1>", self.Even1)
        
        
        self.color2=Ct.CTkFrame(
                        self.Frame,
                        width=self.taille[0],
                        height=self.taille[1],
                        fg_color=self.bg[1],
                        border_width=2.7,
                        border_color=self.unSelect[1],
                        corner_radius=30
                        )
        self.color2.grid(row=0,column=1,padx=4,pady=4)
        self.color2.bind("<Button-1>", self.Even2)
        
        
        self.color3=Ct.CTkFrame(
                        self.Frame,
                        width=self.taille[0],
                        height=self.taille[1],
                        fg_color=self.bg[2],
                        border_width=2.7,
                        border_color=self.unSelect[2],
                        corner_radius=30
                        )
        self.color3.grid(row=0,column=2,padx=4,pady=4)
        self.color3.bind("<Button-1>", self.Even3)
        

    def Even1(self,event):
        
        
        self.color1.configure(border_color=self.Select)
        self.color2.configure(border_color=self.unSelect[1])
        self.color3.configure(border_color=self.unSelect[2])
        # print(self.bg[0])
        
            

    def Even2(self,event):
        
        self.color1.configure(border_color=self.unSelect[0])
        self.color2.configure(border_color=self.Select)
        self.color3.configure(border_color=self.unSelect[2])
        # print(self.bg[1])
        
            
    def Even3(self,event):
        
        self.color1.configure(border_color=self.unSelect[0])
        self.color2.configure(border_color=self.unSelect[1])
        self.color3.configure(border_color=self.Select)
        # print(self.bg[2])
        
    
    def get_Color(self):
        
        if self.color1.cget("border_color")== self.Select:
            return self.bg[0]
        if self.color2.cget("border_color") == self.Select:
            return self.bg[1]
        if self.color3.cget("border_color") == self.Select:
            return self.bg[2]
            
        
# widget Color


# widget Option

class Option:
    def __init__(self,Root,coor) :
        
        self.coor=coor
        
        self.Frame=Ct.CTkFrame(Root,
                              width=150,
                              height=40,
                              fg_color="#fff",
                              border_width=2,
                              corner_radius=20,
                              border_color="black"
                              )
        self.Frame.place(x=self.coor[0],y=self.coor[1])
        
        self.label=Ct.CTkLabel(self.Frame,    bg_color="white",                                font=("inder",25))

# widget Option
    