import scratchattach as sa
import webbrowser

USERNAME = "GuDuoNei"

print("Fetching projects...\n")

user = sa.get_user(USERNAME)
projects = user.projects(limit=20)

for i, project in enumerate(projects):
    print(f"{i+1}. {project.title}")

choice = input("\nEnter project number to open: ")

try:
    selected = projects[int(choice)-1]
    url = f"https://scratch.mit.edu/projects/{selected.id}/"
    print("Opening:", url)
    webbrowser.open(url)
except:
    print("Invalid choice.")