import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

def display_contacts():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    if not listbox_contacts.size():
        messagebox.showinfo("Search", "No contacts found.")

def update_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contacts[index] = {
            "name": entry_name.get(),
            "phone": entry_phone.get(),
            "email": entry_email.get(),
            "address": entry_address.get()
        }
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "No contact selected.")

def delete_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        display_contacts()
    else:
        messagebox.showerror("Error", "No contact selected.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def on_select(event):
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact['name'])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact['phone'])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact['email'])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact['address'])

# Main application window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("330x500")

# Input fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, padx=10, pady=5)

# Buttons
btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.grid(row=4, column=0, padx=10, pady=10)

btn_update = tk.Button(root, text="Update Contact", command=update_contact)
btn_update.grid(row=4, column=1, padx=10, pady=10)

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=5, column=0, padx=10, pady=10)

btn_clear = tk.Button(root, text="Clear Fields", command=clear_entries)
btn_clear.grid(row=5, column=1, padx=10, pady=10)

# Search bar
tk.Label(root, text="Search:").grid(row=6, column=0, padx=10, pady=5)
entry_search = tk.Entry(root)
entry_search.grid(row=6, column=1, padx=10, pady=5)

btn_search = tk.Button(root, text="Search", command=search_contact)
btn_search.grid(row=6, column=2, padx=10, pady=5)

# Contact list
listbox_contacts = tk.Listbox(root, width=50, height=15)
listbox_contacts.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
listbox_contacts.bind("<<ListboxSelect>>", on_select)

# Run the application
root.mainloop()
