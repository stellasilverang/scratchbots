import scratchattach as sa
import tkinter as tk
from tkinter import messagebox
import webbrowser

projects = []

# Fetch projects
def load_projects():
    global projects

    username = username_entry.get()

    if username == "":
        messagebox.showerror("Error", "Enter a username")
        return

    listbox.delete(0, tk.END)

    try:
        user = sa.get_user(username)
        projects = user.projects(limit=20)

        for p in projects:
            listbox.insert(tk.END, p.title)

    except Exception as e:
        messagebox.showerror("Error", "User not found or connection issue")

# Open selected project
def open_project():
    selected = listbox.curselection()

    if not selected:
        return

    project = projects[selected[0]]
    url = f"https://scratch.mit.edu/projects/{project.id}/"

    webbrowser.open(url)

# GUI window
root = tk.Tk()
root.title("Scratch Studio Helper")
root.geometry("400x450")

tk.Label(root, text="Scratch Username").pack(pady=5)

username_entry = tk.Entry(root, width=30)
username_entry.pack()

load_btn = tk.Button(root, text="Load Projects", command=load_projects)
load_btn.pack(pady=10)

listbox = tk.Listbox(root, width=45, height=15)
listbox.pack(pady=10)

open_btn = tk.Button(root, text="Open Project", command=open_project)
open_btn.pack(pady=5)

root.mainloop()