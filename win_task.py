import tkinter as tk
from tkinter import ttk
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
    
    
    root = tk.Tk()
    root.configure(bg="#fff")
    root.title("Onfaikw.")
    root.geometry("320x500")
    
    
    Title=ttk.Label(root,text=var_T,background="#fff",font=("inder",25))
    Title.pack()
    
    #widget_Name
    labelName=ttk.Label(root,text=var_N,font=("inder",20),background="white")
    labelName.place(x=20,y=80)
    EntryN=Ct.CTkEntry(root,border_width=0,corner_radius=5,width=200,fg_color="#D9D9D9",text_color="black",font=("inder",18))
    EntryN.place(x=100,y=85)
    
    
    #widget_Describle
    labelDescrible=ttk.Label(root,text=var_D,font=("inder",20),background="white")
    labelDescrible.place(x=20,y=150)
    EntryD=Ct.CTkTextbox(root,corner_radius=5,width=270,height=100,fg_color="#D9D9D9",text_color="black",font=("inder",18))
    EntryD.place(x=20,y=190)
    
    
    #widget_Priority
    
    
    
    
    
    root.mainloop()


task(dicoText["tf"],dicoText["nf"],dicoText["df"])