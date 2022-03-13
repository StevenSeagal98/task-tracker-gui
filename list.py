import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *

#Create Main Window
root = tkinter.Tk()
root.geometry('500x500')
root.title('Task Tracker')

#Dict to store tasks - Store name of the task and respective subtasks
tasks_dict = {'task_name': [], 'sub_tasks': []}

#CRUD Functions
#Add task
def add_task():
    task = entry_task.get()

    #validate input - warn user if task is empty
    if task != '':
        #Create new Task object from input
        tasks_dict['task_name'].append(task)
        tasks_dict['sub_tasks'].append('Learn TKINTER')
        #print (tasks_dict)
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    #Warning message if input field is empty when submitting task
    else:
        tkinter.messagebox.showwarning(title = 'Warning', message = 'Enter a task.')

#Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

#Create main listbox
listbox_tasks = tkinter.Listbox(root, height = 10, width = 50, selectmode = SINGLE)
listbox_tasks.pack()

#Create new window for selected task
def printValue():
    #loop through values given by curselection and use appropriate value to populate variables
    for i in listbox_tasks.curselection():
        #Create current task variable
        current_task = listbox_tasks.get(i)
        #print(listbox_tasks.get(i))

        #Create Window
        newWindow = Toplevel(root)
        newWindow.title(current_task)
        newWindow.geometry('400x400')

        #Set label to selected task value
        task_label = Label(newWindow, text= listbox_tasks.get(i)).pack(pady = 10)

        #Create subtask list box
        sub_task_list = tkinter.Listbox(newWindow, height = 10, width = 50, selectmode = SINGLE).pack(pady = 10)

        #Print sub_tasks
        print(tasks_dict.get(current_task))

        # Buttons in individual task window
        button_add_task = tkinter.Button(newWindow, text = 'Add task', width = 48, command = add_task)
        button_add_task.pack()

        

#Create Scrollbar for tasks box
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side = tkinter.RIGHT, fill = tkinter.Y)
scrollbar_tasks.config(command = listbox_tasks.yview)

entry_task = tkinter.Entry(root, width = 50)
entry_task.pack()

#Create Buttons
#Create add task button
button_add_task = tkinter.Button(root, text = 'Add task', width = 48, command = add_task)
button_add_task.pack()

#print Button
button_print = tkinter.Button(root, text = 'Add Sub Tasks', width = 48, command = printValue)
button_print.pack()

#Show Completed Tasks
button_completed_tasks = tkinter.Button(root, text = 'Completed Tasks', width = 48)
button_completed_tasks.pack()
#Edit Button

#Delete Button

#Mark Complete Button

#Run main loop
root.mainloop()