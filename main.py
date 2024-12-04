import tkinter as tk
from tkinter import font
from tkinter import messagebox

#Detect mouse wheel scroll                                                 --Elden
#Windows mouse wheel
def on_windows_mouse_wheel(event, canvas):
  if event.delta > 0:
    canvas.yview_scroll(-1, "units")  # Scroll up
  else:
    canvas.yview_scroll(1, "units")   # Scroll down

#Linux mouse wheel
def on_linux_mouse_wheel(event, canvas):
  if event.num == 4:
    canvas.yview_scroll(-1, "units")
  elif event.num == 5:
    canvas.yview_scroll(1, "units")

#Main
class MyApp(tk.Frame):
    def __init__(self, root):

      #pages
      self.current_page_index = 0
      self.pages = []

      #Holding values that are shared to allow quick adjustments           --Elden
      #Colours
      self.pacific_blue = "#309CBA"
      self.white_smoke = "#F5F5F5"

      #Fonts
      self.h1 = ("Garamond ", 20)

      #Icon
      self.icon = tk.PhotoImage(file="list.png")
      self.icon = self.icon.subsample(10)

      #Initialising parent class                                           --Elden         
      super().__init__(root, background='#EEEEEE')
      self.main = self
      self.main.pack(fill="both", expand=1)    

      #Create main page
      self.main.create_main_page()


    def create_main_page(self):
      self.create_header()
      self.create_to_do_list()
      self.create_navbar()
  

    #Creating the header at the top                                                  --Elden
    def create_header(self):

      #Frame is used to allow padding with background colour
      self.header = tk.Frame(self.main, background=self.pacific_blue)
      self.header.pack(fill="x")

      self.label = tk.Label(self.header, text="Title", background=self.pacific_blue, font=self.h1, fg="white", )
      self.label.pack(side="left", padx=10, pady=10)


    #Creating a navigation bar at the bottom to navigate the 3 modules               --Elden 
    def create_navbar(self):
      self.navbar = tk.Frame(self.main, background=self.pacific_blue)
      self.navbar.pack(side="bottom", fill="x")
      self.navbar.columnconfigure(0, weight=1)
      self.navbar.columnconfigure(1, weight=1)
      self.navbar.columnconfigure(2, weight=1)

      self.btn1 = tk.Button(self.navbar, text="To-Do List", image=self.icon, compound='top', background=self.pacific_blue, foreground="white")
      self.btn1.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

      self.btn2 = tk.Button(self.navbar, text="Module 2", image=self.icon, compound='top', background=self.pacific_blue, foreground="white")
      self.btn2.grid(row=0, column=1, sticky="ew", padx=0, pady=0)

      self.btn3 = tk.Button(self.navbar, text="Module 3", image=self.icon, compound='top', background=self.pacific_blue, foreground="white")
      self.btn3.grid(row=0, column=2, sticky="ew", padx=0, pady=0)

  
    #Creating the main interface of To-Do List module                                --Elden
    def create_to_do_list(self):

      #Frame to position canvas and scrollbar
      self.container = tk.Frame(self.main)
      self.container.pack(side="top", fill="both", expand=True)

      #Using canvas to allow scrolling
      self.canvas = tk.Canvas(self.container,background=self.white_smoke)
      self.canvas.pack(side="left", fill="both", expand=True)

      #Create a scrollbar for the canvas
      self.scrollbar = tk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
      self.scrollbar.pack(side="right", fill="y")

      #Configure canvas to respond to the scrollbar
      self.canvas.configure(yscrollcommand=self.scrollbar.set)

      #Frame to store main content
      self.content = tk.Frame(self.canvas, background=self.white_smoke)

      #Create a window to store the frame
      self.canvas.create_window((0,0), window=self.content, anchor="nw")

      #Main content
      for x in range (10):
        label = tk.Label(self.content, text="test", font=("Arial", 18), background="white")
        label.__dict__['id'] = x 
        label.pack(padx=50, pady=50)
        print(label.__dict__['id'])

      self.content.update_idletasks()
      self.canvas.config(scrollregion=self.canvas.bbox("all"))

      #Bind mouse scroll to canvas
      self.canvas.bind_all("<MouseWheel>", lambda event, canvas=self.canvas: on_windows_mouse_wheel(event, canvas))
      self.canvas.bind_all("<Button-4>", lambda event, canvas=self.canvas: on_linux_mouse_wheel(event, canvas))
      self.canvas.bind_all("<Button-5>", lambda event, canvas=self.canvas: on_linux_mouse_wheel(event, canvas))

  
    def on_button_click(self):
      self.label.config(text="Button Clicked!")

    def load_main_widget(self):
      pass

    def clear_frame(self, frame):
      pass

    def create_page_container(self):
      pass

    def create_pager(self):
      pass

      def change_page(button):
        pass

    def page1(self):
      pass
      
    def page2(self):
      pass

    def page3(self):
      pass

    def page4(self):
      pass

root = tk.Tk()
root.title("My App")
root.geometry("480x720")  #720x1280
root.resizable(False, False)
my_app_instance = MyApp(root)
root.mainloop()
