import tkinter as tk

class MyApp(tk.Frame):
  def __init__(self, root):
    #pages
    self.current_page_index = 0
    self.pages = []

    #colours

    #fonts

    super().__init__(root, background='#000000')
    self.main = self
    self.main.pack(fill="both", expand=1)
    self.main.columnconfigure(0, weight=1)
    self.main.rowconfigure(0, weight=1)

    self.main.create_widgets()

  def create_widgets(self):
    self.label = tk.Label(self, text="Hello World")
    self.label.pack()

    self.button = tk.Button(self, text="Click Me", command=self.on_button_click)
    self.button.pack()

  def on_button_click(self):
    self.label.config(text="Button Clicked!")

  root = tk.Tk()
  root.title("My App")
  root.geometry("1080x1920") #720x1280
  root.resizable(False, False)
  my_app = MyApp(root)