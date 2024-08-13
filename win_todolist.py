import tkinter as tk
from tkinter import ttk
import customtkinter as Ct


dicoText={
    
    "te":"todolist",
    "tf":"liste",
    "ne":"Name",
    "nf":"Nom"
}



def event_todolist(event):

    var=entry.get()
    print(var)
    entry.delete(0,tk.END)
    
    
def todolist(var_T,var_N):
    
    
    root = tk.Tk()
    root.configure(bg="#fff")
    root.title("Onfaikw.")
    root.geometry("340x130")
    
    global entry

    # image = tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/todolist(4).png")

    
    #Title
    labelTitle=ttk.Label(root,text=var_T,background="white",font=("inder",25))
    labelTitle.pack()
    
    #widget_Name
    labelName=ttk.Label(root,text=var_N,font=("inder",20),background="white")
    labelName.place(x=20,y=50)
    
    #widget_entry
    entry=Ct.CTkEntry(root,border_width=0,corner_radius=5,width=200,fg_color="#D9D9D9",text_color="black",font=("inder",16))
    entry.place(x=90,y=57)
    entry.bind("<Return>",event_todolist)
    


    root.mainloop()





todolist(dicoText["tf"],dicoText["nf"])