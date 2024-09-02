import tkinter as tk
import sheet_widget as sh
from tkinter import ttk
import customtkinter as Ct


def switch(event):
    pass

def Main():
    
    Root = tk.Tk()
    Root.configure(bg="#fff")
    Root.title("Onfaikw.")
    Root.geometry("440x710")
    Logo=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/Logo_A.png")
    Barre=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/barre.png")
    Selection=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/selection.png")
    
    
    
    labelLogo=tk.Label(Root,image=Logo,background="white")
    labelLogo.place(relx=0.5,y=70,anchor="center")
    
    labelbarre=tk.Label(Root,image=Barre,background="white")
    labelbarre.place(relx=0.5,y=210,anchor="center")
    
    labelselection=tk.Label(Root,image=Selection,background="white")
    labelselection.place(relx=0.253,y=210,anchor="center")
    
    Frame=Ct.CTkFrame(
                       Root,
                       width=250,
                       height=50,
                       border_width=3,
                       border_color="white",
                       fg_color="white",
                       corner_radius=5
                       )
    Frame.place(relx=0.5,y=185,anchor="center")
    
    
    
    todolist=ttk.Label(Frame,text="todolist",background="white",font=("inder",16))
    todolist.grid(row=0,column=0,padx=20,pady=5)
    tache=ttk.Label(Frame,text="tâche",background="white",font=("inder",16))
    tache.grid(row=0,column=1,padx=20,pady=5)
    historie=ttk.Label(Frame,text="historie",background="white",font=("inder",16))
    historie.grid(row=0,column=2,padx=20,pady=5)
    
    
    todo=sh.Menu(Root)
   
   
   
    Root.mainloop()
    
    
    


Main()