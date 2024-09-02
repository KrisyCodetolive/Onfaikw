import tkinter as tk
# import code_source.win_widget as C 
# import test as t 
from tkinter import ttk
import customtkinter as Ct



root = tk.Tk()
root.configure(bg="#fff")
root.title("Onfaikw.")
root.geometry("340x130")
    

def imprime():
    print('1')
    root.after(200,imprime)

def event_Placeholder(event):
    imprime()

    
    #Title
labelTitle=ttk.Label(root,text="Liste",background="white",font=("inder",25))
labelTitle.pack()
    
    #widget_Name
labelName=ttk.Label(root,text="Nom",font=("inder",20),background="white")
labelName.place(x=20,y=50)
    
    #widget_entry
entry=Ct.CTkEntry(root,border_width=0,corner_radius=5,width=200,fg_color="#D9D9D9",text_color="black",font=("inder",16))
entry.place(x=90,y=57)
    
    # entry.bind("<Return>",event_todolist)
    
    #placeholder
holder=Ct.CTkLabel(root,text="Nom de la liste",text_color="#5E5E5E",bg_color="#D9D9D9",font=("inder",13))
holder.place(x=97,y=57)
holder.bind("<Button-1>",event_Placeholder)
    # Placeholder="Nom de la liste"
    # entry.insert(0,Placeholder)
    
    


root.mainloop()