import tkinter as tk
from tkinter import ttk
import code_source.win_widget as C 
import customtkinter as Ct


dicoText={
    "te" :"task",
    "tf" :"tâche",
    "ne" :"Name",
    "nf" :"Nom",
    "de" :"Describle",
    "df" :"Description",
    "pe" :"Priority",
    "pf" :"Priorité",
    "ce" :"Color",
    "cf" :"Couleur",
    "Def":"Date"
}


def task(var_T,var_N,var_D):
    
    def event_task(event):
        
        entry=EntryN.cget()
        entry.delete(0,tk.END)
        TextboxD=EntryN.cget()
        TextboxD.delete(0,tk.END)
        
        pass
    #initialisation de la fenetre
    root = tk.Tk()
    root.configure(bg="#ffffff")
    root.title("Onfaikw.")
    root.geometry("320x500")
    #initialisation de la fenetre
    
    
    #widget_Title
    Title=ttk.Label(root,text=var_T,background="#fff",font=("inder",20))
    Title.pack()
    
    
    #widget_Name
    labelName=ttk.Label(root,text=var_N,font=("inder",20),background="white")
    labelName.place(x=20,y=80)
    EntryN=Ct.CTkEntry(
           root,
           border_width=0,
           corner_radius=20,
           width=200,
           fg_color="#D9D9D9",
           text_color="black",
           font=("inder",18)
                       
                       )
    EntryN.place(x=100,y=85)
    
    
    #widget_Describle
    labelDescrible=ttk.Label(root,text=var_D,font=("inder",20),background="white")
    labelDescrible.place(x=15,y=130)
    TextboxD=Ct.CTkTextbox(
             root,
             corner_radius=5,
             width=270,
             height=100,
             fg_color="#D9D9D9",
             text_color="black",
             font=("inder",18)
        
        )
    TextboxD.place(x=16,y=170)
    
    
    #Color
    Colors=C.Color(("#FBE5CB","#F28181","#949393"),(18,350),root)
    
    
    #Option Priorité
    Option=C.Option(root,(18,297))
    
    
    root.bind("<Return>",event_task)
    
    
    root.mainloop()


task(
    dicoText["tf"],
    dicoText["nf"],
    dicoText["df"]
    
    
    )