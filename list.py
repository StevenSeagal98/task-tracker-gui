import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
#pip install Pillow to use this package - Used for images (May need to update pip to work correctly)
from PIL import Image, ImageTk

#Create main window with root variable
root = tkinter.Tk()
#set geometry, title, and label for window
root.geometry('500x500')
root.title('Task Tracker')
main_label = Label(root, text = 'Welcome To Task Tracker').pack(pady = 10)

#Set Image for main window
#Load the image
image = Image.open('images/checklist.png')

#Resize the image in the given (width, height)
img = image.resize((100, 100))

#Convert the image in TkImage
my_img = ImageTk.PhotoImage(img)

#Display the image with label
label = Label(root, image = my_img)
label.pack()

#Dict to store tasks - Store name of the task and respective subtasks. Also "completed" will track whether a task has been finished or not
tasks_dict = {'task_name': [], 'sub_tasks': [], 'completed': []}

#Button Functions
#Add task
def add_task():
    task = entry_task.get()

    #validate input - warn user if task is empty
    if task != '':
        #Create new Task object from input
        tasks_dict['task_name'].append(task)
        tasks_dict['sub_tasks'].append('Learn TKINTER')
        tasks_dict['sub_tasks'].append(False)
        #print (tasks_dict)
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    #Warning message if input field is empty when submitting task
    else:
        tkinter.messagebox.showwarning(title = 'Warning', message = 'Enter a task.')

def delete_task():
    listbox_tasks.delete(ANCHOR)

#Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

#Create main listbox
listbox_tasks = tkinter.Listbox(root, height = 10, width = 50, selectmode = SINGLE)
listbox_tasks.pack()

#Variable to store user input as tasks in listbox
entry_task = tkinter.Entry(root, width = 50)
entry_task.pack()

#Create new window for selected task
def task_window():
    #loop through values given by curselection and use appropriate value to populate variable current_task
    for i in listbox_tasks.curselection():
        #Create current task variable from selected task on main window
        current_task = listbox_tasks.get(i)

        #Create Window, set title, set geometry
        newWindow = Toplevel(root)
        newWindow.title(current_task)
        newWindow.geometry('600x600')

        #Set label to selected task value
        task_label = Label(newWindow, text= listbox_tasks.get(i)).pack(pady = 10)

        #Image for new window
        #Load the image
        new_window_img = Image.open('images/task_tracker_home.jpg')

        #Resize the image in the given (width, height)
        new_window_img_resize = new_window_img.resize((100, 100))

        #Convert the image in TkImage
        new_window_image = ImageTk.PhotoImage(new_window_img_resize)

        #Display the image with label
        label = Label(newWindow, image = new_window_image)
        label.pack()

        #CRUD operations for new window
        #Add subtask
        def add_subtask():
            sub_task = subtask_entry.get()

            #validate input - warn user if task is empty
            if sub_task != '':
            #Add subtask as value to corresponding key value pair
                tasks_dict.update({current_task: [sub_task]})
                
                #Add subtask to subtask list
                listbox_subtasks.insert(tkinter.END, sub_task)
                subtask_entry.delete(0, tkinter.END)

                #Warning message if input field is empty when submitting subtask
            else:
                tkinter.messagebox.showwarning(title = 'Warning', message = 'Enter a subtask.')
        
        def delete_subtask():
            listbox_subtasks.delete(ANCHOR)

        #Create subtask list box
        listbox_subtasks = tkinter.Listbox(newWindow, height = 10, width = 50, selectmode = SINGLE).pack(pady = 10)

        #Create subtask entry box
        subtask_entry = Entry(newWindow)
        subtask_entry.pack()

        #Delete Subtask
        button_delete_subtask = tkinter.Button(newWindow, text = 'Delete Subtask', width = 48, command = delete_subtask)
        button_delete_subtask.pack(pady = 10)

        # Buttons in individual task window
        button_add_task = tkinter.Button(newWindow, text = 'Add SubTask', width = 48, command = add_subtask)
        button_add_task.pack(pady = 10)

        #Exit Button for new window
        button_exit_sub = tkinter.Button(newWindow, text = 'Exit', width = '48', bg = 'red', fg = 'white', command = root.destroy)
        button_exit_sub.pack(pady = 10)

#Create Buttons
#Create add task button
button_add_task = tkinter.Button(root, text = 'Add task', width = 48, bg = 'blue', fg = 'white', command = add_task)
button_add_task.pack()

#print Button
button_new_window = tkinter.Button(root, text = 'Add Sub Tasks', width = 48, bg = 'yellow', command = task_window)
button_new_window.pack()

#Delete Button
button_delete_task = tkinter.Button(root, text = 'Delete Task', width = 48, bg = 'purple', fg = 'white', command = delete_task)
button_delete_task.pack()

#Exit Button
button_exit = tkinter.Button(root, text = 'Exit', width = '48', bg = 'red', command = root.destroy)
button_exit.pack()

#Run main loop
root.mainloop()
