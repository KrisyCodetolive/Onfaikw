import tkinter as tk
import customtkinter as Ct
import time 
import win_todolist as todo


# widget todolist

#widget Todo

class Todo:
    def __init__(self,Root,todo):
        
        self.todo=todo
        self.widthF=390
        self.heightF=63
        self.border=2.5
        self.Select="#22A2E4"
        self.unselect="black"
        self.var=True
        
        self.Frame=Ct.CTkFrame(
                       Root,
                       width=self.widthF,
                       height=self.heightF,
                       border_width=self.border,
                       border_color=self.unselect,
                       fg_color="#fff",
                       corner_radius=0
                       )
        self.Frame.place(relx=0.5,rely=0.1,anchor="center")
        self.Frame.bind("<Button-1>",self.select)
        self.Frame.bind("<Enter>",lambda p: self.Frame.configure(border_color=self.Select))
        self.Frame.bind("<Leave>",self.leave)
        
       
        
        self.Label=Ct.CTkLabel(self.Frame,text=self.todo,font=("Poppins",28,"bold"), 
                               text_color="black",                    
                               fg_color="white",)
        
        self.Label.place(relx=0.5,rely=0.5,anchor="center")
        self.Label.bind("<Button-1>",self.select)
        self.Label.bind("<Enter>",lambda p: self.Frame.configure(border_color=self.Select))
        self.Label.bind("<Leave>",self.leave)
        
        
        
    #fonction callback
    
    def select(self,event):
        
        if self.var :
            self.Frame.configure(border_color=self.Select)
            self.var=False
            
        else:
            self.Frame.configure(border_color=self.unselect)
            self.var=True
            

    def leave(self,event):
        
        if not self.var :
            self.Frame.configure(border_color=self.Select)
        
        else:
            self.Frame.configure(border_color=self.unselect)
            
    #fonction callback
        
#widget Todo
        
        

#widget task

class Task():
    
    def __init__(self,Root,color,todo): 
        
        
        self.var=True
        self.circle_widthF=40
        self.circle_heightF=40
        self.Select="#22A2E4"
        self.unselect=color
        self.widthF=390
        self.border=2.5
        
        self.check=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/check.png")
        self.uncheck=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/uncheck.png")
        
        self.frame=Ct.CTkFrame(
                       Root,
                       width=self.widthF,
                       height=50,
                       border_width=self.border,
                       border_color=color,
                       fg_color=color,
                       corner_radius=7
                       )
        self.frame.place(relx=0.5,rely=0.1,anchor="center")
        self.frame.bind("<Button-1>",self.select)
        self.frame.bind("<Enter>",lambda p: self.frame.configure(border_color=self.Select))
        self.frame.bind("<Leave>",self.leave)
        
        self.label=Ct.CTkLabel(self.frame,text=todo,font=("Poppins",20,"bold"), 
                               text_color="black",                    
                               fg_color=color)
        self.label.place(relx=0.25,rely=0.5,anchor="center")
        
        self.labelcheckBox=Ct.CTkLabel(self.frame,image=self.uncheck,
                                text="",                    
                               fg_color=color)
        self.labelcheckBox.place(relx=0.11,rely=0.5,anchor="center")
        self.labelcheckBox.bind("<Button-1>",self.Check)
        
        
        
        
        #fonction callback
        
        
    def Check(self,event):
        
        if self.var :
            self.label.configure(font=("Poppins",20,"bold","overstrike"))
            self.labelcheckBox.configure(image=self.check)
            self.labelcheckBox.place(relx=0.11,rely=0.7,anchor="center")
            self.var=False
            
        
        else:
            
            self.labelcheckBox.configure(image=self.uncheck)
            self.label.configure(font=("Poppins",20,"bold","bold"))
            self.labelcheckBox.place(relx=0.11,rely=0.5,anchor="center")
            self.var=True
            
    def select(self,event):
        
        if self.var :
            self.frame.configure(border_color=self.Select)
            self.var=False
            
        else:
            self.frame.configure(border_color=self.unselect)
            self.var=True
            
    def leave(self,event):
        
        if not self.var :
            self.frame.configure(border_color=self.Select)
        
        else:
            self.frame.configure(border_color=self.unselect)


#widget task




#widget Menu


class Menu:
    
    def __init__(self,Root):
        
        self.widthF=365
        self.heightF=70
        self.border=2.7
        
        self.add=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/Group 47.png")
        self.modifier=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/modifier.png")
        self.supprimer=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/supprimer(1).png")
        
        
        self.Frame=Ct.CTkFrame(
                       Root,
                       width=self.widthF,
                       height=self.heightF,
                       border_width=self.border,
                       border_color="black",
                       fg_color="#F6F6F6",
                       corner_radius=27
                       )
        
        self.Frame.place(relx=0.5,rely=0.89,anchor="center")
        
        
        
        self.Frame.rowconfigure(0,weight=1)
        
        
        self.Add=Ct.CTkLabel(self.Frame,text="",image=self.add,                    
                               fg_color="#F6F6F6")
        self.Add.bind("<Button-1>",lambda p : todo.todolist(todo.dicoText["tf"],todo.dicoText["nf"]))
        self.Modifier=Ct.CTkLabel(self.Frame,text="",image=self.modifier,                    
                               fg_color="#F6F6F6")
        self.Supprimer=Ct.CTkLabel(self.Frame,text="",image=self.supprimer,                    
                               fg_color="#F6F6F6")
        
        self.Add.grid(row=0,column=0,padx=50,pady=20)
        self.Modifier.grid(row=0,column=1,padx=50,pady=20)
        self.Supprimer.grid(row=0,column=2,padx=50,pady=20)
        

#widget Menu





        
        
        
        
        
        
        
        








# widget todolist