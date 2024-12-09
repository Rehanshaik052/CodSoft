import tkinter as tk
from tkinter import messagebox

tasks = []

def addt():
    task = task_entry.get()
    if task:
        tasks.append({"description": task, "status": "Pending"})
        utl()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty!")

def utl():
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        task_display = f"[{index + 1}] {task['description']} - {task['status']}"
        task_listbox.insert(tk.END, task_display)

def markdone():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["status"] = "Done"
        utl()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

def delete():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        utl()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="lightblue")


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="enter the Task", command=addt)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

done_button = tk.Button(root, text="mark as completed", command=markdone)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete)
delete_button.pack(pady=5)


root.mainloop()
