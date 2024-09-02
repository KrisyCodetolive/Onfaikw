import tkinter as tk
from tkinter import ttk
import customtkinter as Ct


dicoText={
    
    "te":"todolist",
    "tf":"liste",
    "ne":"Name",
    "nf":"Nom"
}



def event_Placeholder(event):
    
    holder.config(background="white")
    holder.place(x=97,y=47)
    
def event_todolist(event):
    
    valider=tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/Entrer.png/")
    Valider=ttk.Label(root,image=valider,background="white")
    Valider.place(x=75,y=110)

def event_quit(event):
    
    var=entry.get()
    print(var)
    root.quit()
    
    
def todolist(var_T,var_N):
    
    global holder
    global root
    global entry
    
    root = tk.Tk()
    root.configure(bg="#fff")
    root.title("Onfaikw.")
    root.geometry("355x155")
    
    
    
    
    #Title
    labelTitle=ttk.Label(root,text=var_T,background="white",font=("inder",25))
    labelTitle.pack()
    
    #widget_Name
    labelName=ttk.Label(root,text=var_N,font=("inder",20),background="white")
    labelName.place(x=20,y=65)
    
    #widget_entry
    entry=Ct.CTkEntry(root,border_width=0,corner_radius=5,width=200,fg_color="#D9D9D9",text_color="black",font=("inder",16))
    entry.place(x=90,y=70)
    
    entry.bind("<Button-1>",event_todolist)
    entry.bind("<Return>",event_quit)
    
    #placeholder
    holder=ttk.Label(root,text="Entrez le nom de la Todo",background="#D9D9D9",font=("inder",10))
    holder.place(x=97,y=73)
    #47
    
    holder.bind("<Button-1>",event_Placeholder)
    
    
    root.mainloop()





# todolist(dicoText["tf"],dicoText["nf"])