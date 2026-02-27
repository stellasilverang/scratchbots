import scratchattach as sa
import tkinter as tk
from tkinter import messagebox
import webbrowser

projects = []

# ------------------------
# Load Projects
# ------------------------
def load_projects():
    global projects

    username = username_entry.get()

    if username == "":
        messagebox.showerror("Error", "Enter username")
        return

    listbox.delete(0, tk.END)
    stats_label.config(text="Loading...")

    try:
        user = sa.get_user(username)
        projects = user.projects(limit=30)

        for p in projects:
            listbox.insert(tk.END, p.title)

        stats_label.config(
            text=f"Loaded {len(projects)} projects"
        )

    except:
        messagebox.showerror("Error", "User not found")

# ------------------------
# Show Stats
# ------------------------
def show_stats(event=None):
    selected = listbox.curselection()

    if not selected:
        return

    p = projects[selected[0]]

    stats = (
        f"Views: {p.views}\n"
        f"Loves: {p.loves}\n"
        f"Favorites: {p.favorites}"
    )

    stats_label.config(text=stats)

# ------------------------
# Open Project
# ------------------------
def open_project():
    selected = listbox.curselection()

    if not selected:
        return

    p = projects[selected[0]]
    webbrowser.open(
        f"https://scratch.mit.edu/projects/{p.id}/"
    )

# ------------------------
# Studio Finder (manual helper)
# ------------------------
def open_studio_search():
    selected = listbox.curselection()

    if not selected:
        return

    title = projects[selected[0]].title
    search_url = f"https://scratch.mit.edu/search/studios?q={title}"

    webbrowser.open(search_url)

# ------------------------
# GUI
# ------------------------
root = tk.Tk()
root.title("Scratch Helper PRO")
root.geometry("500x600")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="Scratch Helper PRO",
    font=("Arial",16,"bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=10)

username_entry = tk.Entry(root, width=35)
username_entry.pack(pady=5)

load_btn = tk.Button(
    root,
    text="Load Projects",
    command=load_projects
)
load_btn.pack(pady=5)

listbox = tk.Listbox(
    root,
    width=55,
    height=18,
    bg="#2b2b2b",
    fg="white"
)
listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", show_stats)
listbox.bind("<Double-Button-1>", lambda e: open_project())

stats_label = tk.Label(
    root,
    text="Project stats appear here",
    fg="white",
    bg="#1e1e1e"
)
stats_label.pack(pady=10)

open_btn = tk.Button(
    root,
    text="Open Project",
    command=open_project
)
open_btn.pack(pady=5)

studio_btn = tk.Button(
    root,
    text="Find Related Studios",
    command=open_studio_search
)
studio_btn.pack(pady=5)

root.mainloop()