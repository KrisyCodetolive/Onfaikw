import tkinter as tk
from tkinter import ttk
import customtkinter as Ct



        
class Color(Ct.CTk):
    
    def __init__(self,bg,coor,Root):
        super().__init__()
        
        

        self.bg=bg
        self.coor=coor
        
        self.taille=(60,40) 
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
        
        self.color1_Select()
        
        
        # self.color1.config(border_color=self.Select)
        # self.color2.config(border_color=self.unSelect[1])
        # self.color3.config(border_color=self.unSelect[2])
        # self.Select=self.Select
        # self.bg[1]=self.unSelect[1]
        # self.bg[2]=self.unSelect[2]
        # self.color1.update_idletasks()
        # self.color2.update_idletasks()
        # self.color3.update_idletasks()
            

    def Even2(self,event):
        
        self.color2_Select()
        # self.color1.config(border_color=self.unSelect[0])
        # self.color2.config(border_color=self.Select)
        # self.color3.config(border_color=self.unSelect[2])
        # self.bg[1]=self.Select
        # self.Select=self.unSelect[0]
        # self.bg[2]=self.unSelect[2]
        # self.color1.update_idletasks()
        # self.color2.update_idletasks()
        # self.color3.update_idletasks()
            
    def Even3(self,event):
        
        self.color3_Select()
        # self.color1.config(border_color=self.unSelect[0])
        # self.color2.config(border_color=self.unSelect[1])
        # self.color3.config(border_color=self.Select)
        # self.bg[2]=self.Select
        # self.bg[1]=self.unSelect[1]
        # self.Select=self.unSelect[0]
        # self.color1.update_idletasks()
        # self.color2.update_idletasks()
        # self.color3.update_idletasks()         
           
            
        
        
        



    def color1_Select(self):
        
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
        
        
    def color2_Select(self):
        
        self.color1=Ct.CTkFrame(
                        self.Frame,
                        width=self.taille[0],
                        height=self.taille[1],
                        fg_color=self.bg[0],
                        border_width=2.7,
                        border_color=self.unSelect[0],
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
                        border_color=self.Select,
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
        
        
    def color3_Select(self):
        
        self.color1=Ct.CTkFrame(
                        self.Frame,
                        width=self.taille[0],
                        height=self.taille[1],
                        fg_color=self.bg[0],
                        border_width=2.7,
                        border_color=self.unSelect[0],
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
                        border_color=self.Select,
                        corner_radius=30
                        )
        self.color3.grid(row=0,column=2,padx=4,pady=4)
        self.color3.bind("<Button-1>", self.Even3)   