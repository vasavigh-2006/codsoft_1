import tkinter as tk
from tkinter import messagebox
import pickle
root=tk.Tk()
root.geometry("360x360")
root.title("To Do List")

label=tk.Label(root,text="A To Do List-manage your tasks Effectively",font=("Verdana",12))
label.pack()
def addtask():
    task=myentry.get()
    if task!="":
        list_task.insert(tk.END,task)
        myentry.delete(0,tk.END)
    else:
        
        tk.messagebox.showwarning(title="WARNING",message="Please add a task to enter")
def removetask():
    index=list_task.curselection()
    for item in reversed(index):
        list_task.delete(item)

    
def savetasks():
    tasklist=list_task.get(0,list_task.size())
    pickle.dump(tasklist,open("tasks.dat","wb"))
def showtasks():
    try:
        tasklist=pickle.load(open("tasks.dat","rb"))
        for task in tasklist:
            list_task.insert(tk.END,task)
    except:
        messagebox.showwarning("title=File not found!!",message="The file does not exist,please try with a valid file")
def closing():
    m=messagebox.askyesnocancel("Exit", "Do you want to exit from our to do appplication for now?")
    if m is True:
        root.destroy()    
        


frame=tk.Frame(root)
frame.pack(fill=tk.BOTH,expand=True,padx=8,pady=8)
scroll=tk.Scrollbar(frame)
list_task=tk.Listbox(frame,height=8,font=("Arial",12),yscrollcommand=scroll.set,selectmode=tk.EXTENDED)
list_task.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
scroll.pack(side=tk.RIGHT,fill=tk.Y)

scroll.config(command=list_task.yview)

myentry=tk.Entry(root,width=300,font=("Arial",12))
myentry.pack()

button_add=tk.Button(root,text="Add Your Task",font=("Arial",10),width="50",bg="yellow",command=addtask)
button_add.pack()
button_remove=tk.Button(root,text="Remove a Task",font=("Arial",10),width="50",bg="yellow",command=removetask)
button_remove.pack()
button_remove=tk.Button(root,text="Save your Tasks",font=("Arial",10),width="50",bg="yellow",command=savetasks)
button_remove.pack()
button_remove=tk.Button(root,text="Show my tasks",font=("Arial",10),width="50",bg="yellow",command=showtasks)
button_remove.pack()
root.protocol("WM_DELETE_WINDOW", closing)
root.mainloop()
