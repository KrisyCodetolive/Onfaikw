import tkinter as tk
from tkinter import ttk
import customtkinter as Ct
import time 


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
        
    def view(self):
        self.color1.grid_forget()
        self.color2.grid_forget()
        self.color3.grid_forget()
        
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

class Option(Color):
    def __init__(self,Root,coor) :
        
        
        self.coor=coor
        self.root=Root
        self.Bool=True
        
        self.Frame=Ct.CTkFrame(Root,
                              width=150,
                              height=40,
                              fg_color="#fff",
                              border_width=3,
                              corner_radius=20,
                              border_color="black"
                              )
        self.Frame.place(x=self.coor[0],y=self.coor[1])
        self.Frame.bind("<Button-1>",self.click_Back)
        self.Frame.bind("<ButtonRelease-1>",self.click)
        
        self.label=Ct.CTkLabel(self.Frame,text="Priorité", 
                               text_color="black",                    
                               fg_color="white",                                
                               font=("inder",25))
        self.label.place(x=20,y=5)
        self.label.bind("<Button-1>",self.click_Back)
        self.label.bind("<ButtonRelease-1>",self.click)
        
        self.img=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/Arrow 5(3).png")
        self.imgLabel=tk.Label(self.Frame,image=self.img,
                               background="white")  
        self.imgLabel.place(x=115,y=10)
        
        #Fenetre d'option
        
        
        self.FrameOption=Ct.CTkFrame(Root,
                              width=15,
                              height=5,
                              fg_color="#515151",
                              border_width=0,
                              corner_radius=15,
                              border_color="black"
                              )
        # self.FrameOption.place(x=25,y=55)
        
        self.FrameOption.columnconfigure(0,weight=1)
        self.FrameOption.rowconfigure(0,weight=1)
        self.FrameOption.rowconfigure((1,2,3),weight=1) 
        self.FrameOption.rowconfigure(4,weight=1)       
        
        self.H=Ct.CTkLabel(self.FrameOption,
                           text="",
                           fg_color="#515151",
                           height=2
                               )
        self.H1=Ct.CTkLabel(self.FrameOption,
                           text="",
                           fg_color="#515151",
                           height=2
                               )
        
        self.Haute=Ct.CTkLabel(self.FrameOption,
                               text="Haute",
                               text_color="#D6D6D6",
                               fg_color="#515151",
                               font=("inder",15),
                               #corner_radius=5,
                               anchor="w",
                               width=180,
                               height=10,
                               padx=10
                               )
        self.Haute.bind("<Enter>",lambda p: self.Haute.configure(fg_color="#3F80CD"))
        self.Haute.bind("<Leave>",lambda p: self.Haute.configure(fg_color="#515151"))
        self.Haute.bind("<Button-1>",self.SelectH)
        self.Moyen=Ct.CTkLabel(self.FrameOption,
                               text="Moyen",
                               text_color="#D6D6D6",
                               fg_color="#515151",
                               font=("inder",15),
                               anchor="w",
                               width=180,
                               height=10,
                               padx=10
                               )
        self.Moyen.bind("<Enter>",lambda p: self.Moyen.configure(fg_color="#3F80CD"))
        self.Moyen.bind("<Leave>",lambda p: self.Moyen.configure(fg_color="#515151"))
        self.Moyen.bind("<Button-1>",self.SelectM)
        self.Basse=Ct.CTkLabel(self.FrameOption,
                               text="Basse",
                               text_color="#D6D6D6",
                               fg_color="#515151",
                               font=("inder",15),
                               anchor="w",
                               width=180,
                               height=10,
                               padx=10
                               )                  
        self.Basse.bind("<Enter>",lambda p: self.Basse.configure(fg_color="#3F80CD"))
        self.Basse.bind("<Leave>",lambda p: self.Basse.configure(fg_color="#515151"))
        self.Basse.bind("<Button-1>",self.SelectB)
                              
    
    #fonction callback
    
        
    def click_Back(self,event):
        
        self.imgLabel.place(x=115,y=15)
        if self.Bool:
           
           self.visible()   
        else:
            self.pasvisible()
            
    def click(self,event):
        
        self.imgLabel.place(x=115,y=10)
        self.root.update()
        time.sleep(0.4)
    
    def SelectH(self,event):
        self.label.configure(text="Haute")
        self.pasvisible()
    def SelectM(self,event):
        self.label.configure(text="Moyen")
        self.pasvisible()
    def SelectB(self,event):
        self.label.configure(text="Basse")
        self.pasvisible()
    
    #methode 
    
    def visible(self):
        
        self.H.grid(row=0,column=0)
        self.H1.grid(row=4,column=0)
        self.Haute.grid(row=1,pady=5,column=0)
        self.Moyen.grid(row=2,pady=5,column=0)
        self.Basse.grid(row=3,pady=5,column=0)
        self.FrameOption.place(x=self.coor[0]+70,y=self.coor[1]+35)
        self.Bool=False

    def pasvisible(self):
        
        self.H.grid_forget()
        self.H1.grid_forget()
        self.Haute.grid_forget()
        self.Moyen.grid_forget()
        self.Basse.grid_forget()
        self.FrameOption.place_forget()
        self.Bool=True
        

# widget Option
    