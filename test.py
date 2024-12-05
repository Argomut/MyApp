# import tkinter as tk
# from tkinter import font
# from tkinter import messagebox

# # Function to handle mouse scroll event
# def on_mouse_wheel(event, canvas):
#     # For Windows and macOS
#     if event.delta > 0:
#         canvas.yview_scroll(-1, "units")  # Scroll up
#     else:
#         canvas.yview_scroll(1, "units")   # Scroll down

# # For Linux, the mouse scroll events are Button-4 (scroll up) and Button-5 (scroll down)
# def on_linux_mouse_wheel(event, canvas):
#     if event.num == 4:
#         canvas.yview_scroll(-1, "units")  # Scroll up
#     elif event.num == 5:
#         canvas.yview_scroll(1, "units")   # Scroll down

# # Create the main window
# root = tk.Tk()
# root.title("Scrollable Page with Header and Navbar")
# root.geometry("400x500")  # Increase height to fit header and navbar

# # Header: Place the header at the top
# header = tk.Label(root, text="Header", bg="lightblue", font=("Helvetica", 16))
# header.pack(fill="x")

# # Create a Frame to hold both the canvas and the scrollbar
# frame = tk.Frame(root)
# frame.pack(side="top", fill="both", expand=True)

# # Create the Canvas widget for the scrollable area
# canvas = tk.Canvas(frame)
# canvas.pack(side="left", fill="both", expand=True)

# # Create a Scrollbar widget linked to the Canvas
# scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")

# # Configure the Canvas to respond to the scrollbar
# canvas.configure(yscrollcommand=scrollbar.set)

# # Create a Frame inside the Canvas to hold all the widgets
# scrollable_frame = tk.Frame(canvas)

# # Create a window on the Canvas to place the scrollable_frame
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# # Add widgets (labels, buttons, etc.) to the scrollable_frame
# for i in range(30):
#     label = tk.Label(scrollable_frame, text=f"Label {i+1}")
#     label.pack()

# # Update the scrollable region to match the size of the content
# scrollable_frame.update_idletasks()
# canvas.config(scrollregion=canvas.bbox("all"))

# # For Windows/macOS, bind the mouse wheel to the canvas widget
# canvas.bind_all("<MouseWheel>", lambda event, canvas=canvas: on_mouse_wheel(event, canvas))

# # For Linux, bind the mouse scroll buttons to the canvas widget
# canvas.bind_all("<Button-4>", lambda event, canvas=canvas: on_linux_mouse_wheel(event, canvas))
# canvas.bind_all("<Button-5>", lambda event, canvas=canvas: on_linux_mouse_wheel(event, canvas))

# # Navbar: Place the navbar at the bottom
# navbar = tk.Frame(root, bg="lightgray", height=50)
# navbar.pack(side="bottom", fill="x")

# # Add some buttons to the navbar
# btn1 = tk.Button(navbar, text="Home")
# btn1.pack(side="left", padx=10)
# btn2 = tk.Button(navbar, text="About")
# btn2.pack(side="left", padx=10)
# btn3 = tk.Button(navbar, text="Contact")
# btn3.pack(side="left", padx=10)

# # Start the Tkinter main loop
# root.mainloop()

# class MyApp(tk.Frame):
#   def __init__(self, root):
#     #pages
#     self.current_page_index = 0
#     self.pages = []

#     #colours

#     #fonts

#     #icon
#     self.icon = tk.PhotoImage(file="list.png")
#     self.icon = self.icon.subsample(10)

#     super().__init__(root, background='#EEEEEE')
#     self.main = self
#     self.main.pack(fill="both", expand=1)
#     self.main.columnconfigure(0, weight=1)
#     self.main.rowconfigure(0, weight=0)
#     self.main.rowconfigure(1, weight=1)
#     self.main.rowconfigure(2, weight=0)      

#     #self.load_main_widget()
#     self.main.create_widgets()

#   def create_widgets(self):
#     self.create_header()
#     self.create_to_do_list()
#     self.create_navbar()



#   def create_header(self):
#     self.header = tk.Frame(self.main, background='#754326')
#     self.header.grid(row=0, column=0, sticky="ew")

#     self.label = tk.Label(self.header, text="Hello World", background="#123456", fg="#768596", anchor="w")
#     self.label.pack(padx=10,pady=10, fill="x")



#   def create_navbar(self):
#     self.navbar = tk.Frame(self.main, background='#333333')
#     self.navbar.grid(row=2, column=0, sticky="ew")

#     self.label = tk.Label(self.navbar, text="Hello World", background="#123456", fg="#768596")
#     self.label.pack(padx=10,pady=10)

#     self.button = tk.Button(self.navbar, text="Click Me", image=self.icon, compound='left')
#     self.button.pack(padx=10,pady=10)



#   def create_to_do_list(self):
#     self.canvas = tk.Canvas(self.main, background='#EEEEEE')
#     self.canvas.pack(side="left", fill="both", expand=True)
#     self.canvas.grid(row=1, column=0, sticky="nsew")
#     # Create a Scrollbar widget linked to the Canvas
#     self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
#     self.scrollbar.pack(side="right", fill="y")

#     self.canvas.configure(yscrollcommand=self.scrollbar.set)
#     self.content = tk.Frame(self.main, background='#454545')

#     self.canvas.create_window((0, 0), window=self.content, anchor="nw")

#     for x in range (10):
#       label = tk.Label(self.content, text="test", font=("Arial", 18))
#       label.__dict__['id'] = x 
#       label.pack(padx=50, pady=50)
#       print(label.__dict__['id'])

#     self.content.update_idletasks()
#     self.canvas.config(scrollregion=self.canvas.bbox("all"))




#   def on_button_click(self):
#     self.label.config(text="Button Clicked!")

#   def load_main_widget(self):
#     pass

#   def clear_frame(self, frame):
#     pass

#   def create_page_container(self):
#     pass

#   def create_pager(self):
#     pass

#     def change_page(button):
#       pass

#   def page1(self):
#     pass

#   def page2(self):
#     pass

#   def page3(self):
#     pass

#   def page4(self):
#     pass

# root = tk.Tk()
# root.title("My App")
# root.geometry("480x720") #720x1280
# root.resizable(False, False)
# my_app_instance = MyApp(root)
# root.mainloop()



# class MyApp(tk.Frame):
#     def __init__(self, root):
#       self.current_page_index = 0
#       self.pages = [self.page1, self.page2, self.page3, self.page4]
      
#       self.colour1 = '#222448'
#       self.colour2 = '#54527E'
#       self.colour3 = 'WHITE'

#       super().__init__(root, bg=self.colour1)

#       self.main_frame = self
#       self.main_frame.pack(fill='both', expand=1)
#       self.main_frame.columnconfigure(0, weight=1)
#       self.main_frame.rowconfigure(0, weight=1)

#       self.load_main_widget()

#     def load_main_widget(self):
#       self.create_page_container()
#       self.create_pager()
#       self.pages[self.current_page_index]()

#     def clear_frame(self, frame):
#       for child in frame.winfo_children():
#         child.destroy()

#     def create_page_container(self):
#       self.page_container = tk.Frame(self.main_frame, bg=self.colour1)
#       self.page_container.columnconfigure(0, weight=1)
#       self.page_container.rowconfigure(0, weight=0)
#       self.page_container.rowconfigure(0, weight=1)

#       self.page_container.grid(row=0, column=0, sticky='nsew')
    
#     def create_pager(self):
#       self.pager = tk.Frame(self.main_frame, bg=self.colour1, height=125, width=400)
#       self.pager.columnconfigure(1, weight=1)
#       self.pager.rowconfigure(0, weight=1)
#       self.pager.grid(row=1, column=0, sticky='ns')
#       self.pager.grid_propagate(False)

#       def change_page(button):
#         self.clear_frame(self.page_container)
#         match button:
#           case 'Previous':
#             self.current_page_index -= 1
#             self.pages[self.current_page_index]()
#           case 'Next':
#             self.current_page_index += 1
#             self.pages[self.current_page_index]()
            
#         if self.current_page_index == 0:
#           prev_button.config(state=tk.DISABLED)
#           next_button.config(state=tk.ACTIVE)
#         elif self.current_page_index == len(self.pages) - 1:
#           next_button.config(state=tk.DISABLED)
#           prev_button.config(state=tk.ACTIVE)
#         else:
#           next_button.config(state=tk.ACTIVE)
#           prev_button.config(state=tk.ACTIVE)
#         self.page_number['text'] = f'{self.current_page_index + 1} / {len(self.pages)}'
        
#       prev_button = tk.Button(self.pager, background=self.colour2, foreground=self.colour3, activebackground=self.colour2, activeforeground=self.colour3, disabledforeground='#3B3A56', highlightthickness=0, width=7, relief=tk.FLAT, text='Previous', font=('Helvetica', 12, 'bold'), state=tk.DISABLED, command=lambda button='Previous': change_page(button))
#       prev_button.grid(row=0, column=0)

#       self.page_number = tk.Label(self.pager, background=self.colour1, foreground=self.colour3, font=('Arial', 18), text=f'{self.current_page_index+1} / {len(self.pages)}')
#       self.page_number.grid(row=0, column=1)

#       next_button = tk.Button(self.pager, background=self.colour2, foreground=self.colour3, activebackground=self.colour2, activeforeground=self.colour3, disabledforeground='#3B3A56', highlightthickness=0, width=7, relief=tk.FLAT, text='Next', font=('Helvetica', 12, 'bold'), command=lambda button='Next': change_page(button))
#       next_button.grid(row=0, column=2)

#     def page1(self):
#       title=tk.Label(self.page_container, background=self.colour1, foreground=self.colour3, height=2, font=('Arial', 26, 'bold'), text='Page 1')
#       title.grid(column=0, row=0)

#       text = ('asdasasda sdas  dsaf asd asd asdsa edasdasdas sad asd as asdasasda sdas  dsaf asd asd asdsa edasdasdas sad asd asasdasasda sdas  dsaf asd asd asdsa edasdasdas sad asd asasdasasda sdas  dsaf asd asd asdsa edasdasdas sad asd asasdasasda sdas  dsaf asd asd asdsa edasdasdas sad asd asasdasasda sdas  dsaf asd asd asdsa edasdasdas sad asd as')

#       content = tk.Label(self.page_container, background=self.colour2, foreground=self.colour3, justify=tk.LEFT, anchor=tk.N,pady=20, font=('Arial', 16),text=text,wraplength=600)

#       content.grid(column=0, row=1, sticky=tk.NSEW)

#     def page2(self):
#       title=tk.Label(self.page_container, background=self.colour1, foreground=self.colour3, height=2, font=('Arial', 26, 'bold'), text='Page 2')
#       title.grid(column=0, row=0)

#       text = ('123213 12312 34325234314123213123 w 2e 1 2321321331 ')

#       content = tk.Label(self.page_container, background=self.colour2, foreground=self.colour3, justify=tk.LEFT, anchor=tk.N,pady=20, font=('Arial', 16),text=text,wraplength=600)

#       content.grid(column=0, row=1, sticky=tk.NSEW)

#     def page3(self):
#       title=tk.Label(self.page_container, background=self.colour1, foreground=self.colour3, height=2, font=('Arial', 26, 'bold'), text='Page 3')
#       title.grid(column=0, row=0)

#       text = ('zzzzzzzzzzzzzzzzzzzzzzzzzz szzzzzzzzzzzzzzzzzzzzzz zzzzzzzzzzzzzzzzzzzs')

#       content = tk.Label(self.page_container, background=self.colour2, foreground=self.colour3, justify=tk.LEFT, anchor=tk.N,pady=20, font=('Arial', 16),text=text,wraplength=600)

#       content.grid(column=0, row=1, sticky=tk.NSEW)

#     def page4(self):
#       title=tk.Label(self.page_container, background=self.colour1, foreground=self.colour3, height=2, font=('Arial', 26, 'bold'), text='Page 4')
#       title.grid(column=0, row=0)

#       text = ('000000000000000 000000000000000000000000000 00000000000000000000000 000000000')

#       content = tk.Label(self.page_container, background=self.colour2, foreground=self.colour3, justify=tk.LEFT, anchor=tk.N,pady=20, font=('Arial', 16),text=text,wraplength=600)

#       content.grid(column=0, row=1, sticky=tk.NSEW)
      
# root = tk.Tk()
# root.title('My App')
# root.geometry('700x500')
# root.resizable(False, False)
# my_app_instance = MyApp(root)
# root.mainloop()



# root = tk.Tk()
# root.geometry("500x500")
# root.title("Test")

# for x in range (2):
#   label = tk.Label(root, text="test", font=("Arial", 18))
#   label.__dict__['id'] = x 
#   label.pack(padx=20, pady=20)
#   print(label.__dict__['id'])

# textbox = tk.Text(root, height=3, font=("Arial", 16), wrap="word")
# textbox.pack(padx=10, pady=10)

# entry = tk.Entry(root, font=("Arial", 16))

# button = tk.Button(root, text="Click me!", font=("Arial", 16))
# button.pack(padx=10,pady=10)

# buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=2)

# btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

# btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
# btn4.grid(row=0, column=1, sticky=tk.W+tk.E)

# btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
# btn2.grid(row=1, column=0, sticky=tk.W+tk.E)

# btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

# btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
# btn3.grid(row=2, column=0, sticky=tk.W+tk.E)

# btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18), command=lambda: test())
# btn6.grid(row=2, column=1, sticky=tk.W+tk.E)

# buttonframe.pack(padx=10,pady=10, fill="x")


# btn7 = tk.Button(root, text="7", font=("Arial", 18))
# btn7.place(x=225, y=225, height=50, width=50) #500 - 50 = 450/2 = 225

# tk.Button(root, text="8", font=("Arial", 18))

# def test():
#   print(textbox.get(1.0, "end-1c"))
  
# root.mainloop()



# class MyGui:
#   def __init__(self):
#     self.root = tk.Tk()

#     self.root.geometry("500x500")

#     self.menubar = tk.Menu(self.root)

#     self.filemenu = tk.Menu(self.menubar, tearoff=0)
#     self.filemenu.add_command(label="Close", command=self.on_closing)
#     self.filemenu.add_separator
#     self.filemenu.add_command(label="Close 2", command=exit)

#     self.actionmenu = tk.Menu(self.menubar, tearoff=0)
#     self.actionmenu.add_command(label="test", command=self.show_message)
    
#     self.menubar.add_cascade(label="File", menu=self.filemenu)
#     self.menubar.add_cascade(label="Action", menu=self.actionmenu)

#     self.root.config(menu=self.menubar)

#     self.label = tk.Label(self.root, text="test", font=("Arial", 18))
#     self.label.pack(padx=10, pady=10)

#     self.textbox = tk.Text(self.root, height=3, font=("Arial", 16))
#     self.textbox.bind("<KeyPress>", self.shortcut)
#     self.textbox.pack(padx=10, pady=10)

#     self.check_state = tk.IntVar()
    
#     self.check = tk.Checkbutton(self.root, text="Show Messafe", font=("Arial", 16), variable= self.check_state)
#     self.check.pack(padx=10, pady=10)

#     self.button = tk.Button(self.root, text="Click me!", font=("Arial", 16), command=self.show_message)
#     self.button.pack(padx=10,pady=10)

#     self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 16), command=self.clear)
#     self.clearbtn.pack(padx=10,pady=10)

#     self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
#     self.root.mainloop()

#   def show_message(self):
#     if self.check_state.get() == 0:
#       print(self.textbox.get(1.0, tk.END))
#     else:
#       messagebox.showinfo("Message", self.textbox.get(1.0, tk.END))

#   def shortcut(self, event):
#     # print(event.keysym)
#     # print(event.state)
#     if event.state == 8 and event.keysym == "Return":
#       self.show_message()


#   def on_closing(self):
#     if messagebox.askyesno("Quit", "Do you really want to quit?"):
#       self.root.destroy()

#   def clear(self):
#     self.textbox.delete(1.0, tk.END)
# MyGui()