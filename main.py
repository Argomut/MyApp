import tkinter as tk
from MyClasses.Gui import Gui

root = tk.Tk()
root.title("My App")
root.geometry("480x720")  #720x1280
root.resizable(False, False)
# my_app_instance = MyApp(root)
my_app_instance = Gui(root)
root.mainloop()