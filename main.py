# import subprocess
# import sys

# #install tkcalendar whihc is needed for the ToDo Module
# subprocess.check_call([sys.executable, "-m", "pip", "install", "tkcalendar"])


import tkinter as tk
from MyClasses.Gui import Gui
from MyClasses.ToDo import ToDo

root = tk.Tk()
root.title("My App")
root.geometry("624x936")  #480x720 576x864 624x936 672x1008 720x1280
root.resizable(False, False)
ToDo.initialiseToDoList()
my_app_instance = Gui(root)
root.mainloop()