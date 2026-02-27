import scratchattach as sa
import tkinter as tk
from tkinter import messagebox
import webbrowser
import matplotlib.pyplot as plt
from threading import Thread
import time

projects = []
history = {}

# ------------------------
# Popularity Score
# ------------------------
def popularity(p):
    return (p.views * 0.5 +
            p.loves * 2 +
            p.favorites * 3)

# ------------------------
# Load Projects
# ------------------------
def load_projects():
    global projects

    username = username_entry.get()

    if username == "":
        messagebox.showerror("Error","Enter username")
        return

    listbox.delete(0, tk.END)

    try:
        user = sa.get_user(username)
        projects = user.projects(limit=30)

        for p in projects:
            score = int(popularity(p))
            listbox.insert(
                tk.END,
                f"{p.title}  | Score: {score}"
            )

    except:
        messagebox.showerror("Error","User not found")

# ------------------------
# Show Stats
# ------------------------
def show_stats(event=None):
    sel = listbox.curselection()
    if not sel:
        return

    p = projects[sel[0]]

    stats_label.config(
        text=f"""
Views: {p.views}
Loves: {p.loves}
Favorites: {p.favorites}
Popularity Score: {int(popularity(p))}
"""
    )

# ------------------------
# Open Project
# ------------------------
def open_project():
    sel = listbox.curselection()
    if not sel:
        return

    webbrowser.open(
        f"https://scratch.mit.edu/projects/{projects[sel[0]].id}/"
    )

# ------------------------
# Studio Finder
# ------------------------
def studio_search():
    sel = listbox.curselection()
    if not sel:
        return

    title = projects[sel[0]].title
    webbrowser.open(
        f"https://scratch.mit.edu/search/studios?q={title}"
    )

# ------------------------
# Track Growth
# ------------------------
def track_growth():
    while True:
        for p in projects:
            history.setdefault(p.title, [])
            history[p.title].append(p.views)
        time.sleep(60)

# ------------------------
# Show Graph
# ------------------------
def show_graph():
    sel = listbox.curselection()
    if not sel:
        return

    title = projects[sel[0]].title

    if title not in history:
        return

    plt.figure()
    plt.plot(history[title])
    plt.title(title + " View Growth")
    plt.xlabel("Refresh")
    plt.ylabel("Views")
    plt.show()

# ------------------------
# GUI
# ------------------------
root = tk.Tk()
root.title("Scratch Helper ULTRA")
root.geometry("600x700")
root.configure(bg="#121212")

tk.Label(
    root,
    text="Scratch Helper ULTRA",
    fg="white",
    bg="#121212",
    font=("Arial",18,"bold")
).pack(pady=10)

username_entry = tk.Entry(root,width=40)
username_entry.pack()

tk.Button(
    root,
    text="Load Projects",
    command=load_projects
).pack(pady=5)

listbox = tk.Listbox(
    root,
    width=70,
    height=20,
    bg="#1e1e1e",
    fg="white"
)
listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", show_stats)
listbox.bind("<Double-Button-1>",
             lambda e: open_project())

stats_label = tk.Label(
    root,
    text="Stats appear here",
    fg="white",
    bg="#121212"
)
stats_label.pack()

tk.Button(root,text="Open Project",
          command=open_project).pack(pady=3)

tk.Button(root,text="Find Studios",
          command=studio_search).pack(pady=3)

tk.Button(root,text="Show Growth Graph",
          command=show_graph).pack(pady=3)

Thread(target=track_growth,
       daemon=True).start()

root.mainloop()