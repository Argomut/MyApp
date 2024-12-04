import tkinter as tk
from tkinter import font
from tkinter import messagebox

class MyApp(tk.Frame):
    def __init__(self, root):
      #pages
      self.current_page_index = 0
      self.pages = []

      #colours

      #fonts

      #icon
      self.icon = tk.PhotoImage(file="list.png")
      self.icon = self.icon.subsample(10)

      super().__init__(root, background='#EEEEEE')
      self.main = self
      self.main.pack(fill="both", expand=1)
      # self.main.columnconfigure(0, weight=1)
      # self.main.rowconfigure(0, weight=0)
      # self.main.rowconfigure(1, weight=1)
      # self.main.rowconfigure(2, weight=0)      

      #self.load_main_widget()
      self.main.create_widgets()

    def create_widgets(self):
      self.create_header()
      #self.cont()
      #self.nav()


  
    def create_header(self):
      self.header = tk.Frame(self.main, background='#754326')
      self.pack(side="top")
      # self.header.grid(row=0, column=0, sticky="ew")

      self.label = tk.Label(self.header, text="Hello World", background="#123456", fg="#768596", anchor="w")
      self.label.pack(padx=10,pady=10, fill="x")

    def nav(self):
      self.navbar = tk.Frame(self.main, background='#754326')
      self.navbar.pack(side="bottom", fill="x")
      self.button = tk.Button(self.navbar, text="Click Me", image=self.icon, compound='left')
      self.button.pack(padx=10,pady=10)

    def cont(self):
      self.container = tk.Frame(self.main, background='#EEEEEE')
      self.container.pack(side="top", fill="both", expand=1)

      self.canvas = tk.Canvas(self.container)
      self.canvas.pack(side="left", fill="both", expand=1)
      
      self.scrollbar = tk.Scrollbar(self.container)
      self.scrollbar.pack(side="right", fill="y")
      self.canvas.config(yscrollcommand=self.scrollbar.set)

      self.container2 = tk.Frame(self.canvas)

      self.canvas.create_window((0,0), window=self.container2, anchor="nw")

      for x in range (10):
        label = tk.Label(self.container2, text="test", font=("Arial", 18))
        label.__dict__['id'] = x 
        label.pack(padx=50, pady=50)
        print(label.__dict__['id'])
        
      self.container2.update_idletasks()
      self.canvas.config(scrollregion=self.canvas.bbox("all"))

      
    def create_navbar(self):
      self.navbar = tk.Frame(self.main, background='#333333')
      self.navbar.grid(row=2, column=0, sticky="ew")

      self.label = tk.Label(self.navbar, text="Hello World", background="#123456", fg="#768596")
      self.label.pack(padx=10,pady=10)

      self.button = tk.Button(self.navbar, text="Click Me", image=self.icon, compound='left')
      self.button.pack(padx=10,pady=10)


  
    def create_to_do_list(self):
      self.content = tk.Frame(self.main, background='#454545')
      self.content.grid(row=1, column=0, sticky="nsew")

      for x in range (10):
        label = tk.Label(self.content, text="test", font=("Arial", 18))
        label.__dict__['id'] = x 
        label.pack(padx=50, pady=50)
        print(label.__dict__['id'])
      



  
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
root.geometry("480x720") #720x1280
root.resizable(False, False)
my_app_instance = MyApp(root)
root.mainloop()