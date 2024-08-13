import tkinter as tk
from tkinter import ttk
import customtkinter as Ct

root = tk.Tk()

root.configure(bg="#fff")
root.title("Onfaikw.")
# root.geometry("450x700")
root.geometry("340x130")



def todolist(event):

    var=entry.get()
    print(var)
    entry.delete(0,tk.END)
    
    
image = tk.PhotoImage(file="/home/krisy/Bureau/Projet_/Logiciel_/Onfaikw./code_source/resset/todolist(4).png")

entry=Ct.CTkEntry(root,border_width=0,corner_radius=10,width=200,fg_color="#D9D9D9",text_color="black",font=("inder",20))
entry.place(x=110,y=55)
entry.bind("<Return>",todolist)
labelText=ttk.Label(root,text="Name",font=("inder",20),background="white")
labelText.place(x=20,y=50)
labelImage=ttk.Label(root,image=image,background="white")
labelImage.pack()


root.mainloop()