import tkinter as tk
from MyClasses.ToDo import ToDo
from MyClasses.ProgressBars import ProgressBars
from tkcalendar import Calendar
import datetime
from tkinter import font
from tkinter import messagebox
from tkinter import ttk

#Gui Class
class Gui(tk.Frame):
    def __init__(self, root):

      #pages
      self.current_page_index = 0
      self.pages = []

      #Holding values that are shared to allow quick adjustments                     --Elden
      #Colours
      self.muskeg_grey = "#46484A"
      self.earlgrey = "#969A96"
      self.light_green = "#90EE90"
      self.pacific_blue = "#309CBA"
      self.powder_blue = "#C2EEF7"
      self.white_smoke = "#F5F5F5"
      self.gainsboro = "#DDDDDD"

      #Fonts
      self.monospace_h1 = (("Consolas", 32, "bold"))
      self.h1 = ("Garamond ", 20)
      self.h2 = ("Arial", 18)
      self.normal_text = ("Times New Roman",16)

      #Icon
      self.todo_icon = tk.PhotoImage(file="icon//todo.png")
      self.todo_icon = self.todo_icon.subsample(10)

      self.trash_icon = tk.PhotoImage(file="icon//trash.png")
      self.trash_icon = self.trash_icon.subsample(10)

      self.pin1_icon = tk.PhotoImage(file="icon//pin1.png")
      self.pin1_icon = self.pin1_icon.subsample(5)

      self.pin2_icon = tk.PhotoImage(file="icon//pin2.png")
      self.pin2_icon = self.pin2_icon.subsample(3)

      self.search_icon = tk.PhotoImage(file="icon//search.png")
      self.search_icon = self.search_icon.subsample(12)

      self.back_icon = tk.PhotoImage(file="icon//back.png")
      self.back_icon = self.back_icon.subsample(12)

      #Initialising parent class                                                     --Elden         
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

      self.btn1 = tk.Button(self.navbar, text="To-Do List", image=self.todo_icon, compound='top', background=self.pacific_blue, foreground="white", bd=1)
      self.btn1.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

      self.btn2 = tk.Button(self.navbar, text="Module 2", image=self.todo_icon, compound='top', background=self.pacific_blue, foreground="white", bd=1)
      self.btn2.grid(row=0, column=1, sticky="ew", padx=0, pady=0)

      self.btn3 = tk.Button(self.navbar, text="Module 3", image=self.todo_icon, compound='top', background=self.pacific_blue, foreground="white", bd=1)
      self.btn3.grid(row=0, column=2, sticky="ew", padx=0, pady=0)

  
    #Creating the main interface of To-Do List module                                --Elden
    def create_to_do_list(self):

      #Frame to position canvas and scrollbar
      self.container = tk.Frame(self.main)
      self.container.pack(side="top", fill="both", expand=True)

      #Using canvas to allow scrolling
      self.canvas = tk.Canvas(self.container,background="red")
      self.canvas.pack(side="left", fill="both", expand=True)

      #Create a scrollbar for the canvas
      self.scrollbar = tk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
      self.scrollbar.pack(side="right", fill="y")

      #Configure canvas to respond to the scrollbar
      self.canvas.configure(yscrollcommand=self.scrollbar.set)

      #Frame to store main content
      self.content = tk.Frame(self.canvas, background=self.white_smoke)

      # Create a window to store the frame
      self.content_id = self.canvas.create_window((0, 0), window=self.content, anchor="nw")

      self.search_frame = tk.Frame(self.content, background=self.white_smoke)
      self.search_frame.pack(side="top", fill="x", expand=True, padx=10, pady=10)

      self.searchbar = tk.Entry(self.search_frame, font=self.normal_text)
      self.searchbar.pack(side="left", fill="x", expand="true")

      self.search_btn = tk.Button(self.search_frame, text="Search", image=self.search_icon, compound="left", command=lambda: self.clear(self.content))
      self.search_btn.pack(side="left", padx=20)

      #Main content
      self.refresh_frame = tk.Frame(self.content, background=self.white_smoke)
      self.refresh_frame.pack(fill="x", expand="true")

      toDoList = []
      for x in range(10):
        toDo = ToDo("Title {}".format(x), x*10, x, "Description {}".format(x))
        print(toDo.toString())
        toDoList.append(toDo)

        self.note_frame = tk.Frame(self.refresh_frame, background=self.powder_blue)
        self.note_frame.pack(fill="x", expand="true", padx=10, pady=10)
        self.note_frame.bind("<Button-1>", self.test4)

        self.progress = ProgressBars(self.note_frame, "left", 75, 10, self.powder_blue, "black", "green", self.test4)
        self.progress.setProgress(toDo.getProgress())

        self.mid_frame = tk.Frame(self.note_frame, background=self.powder_blue)
        self.mid_frame.pack(side="left", fill="both", expand="true")

        self.title = tk.Label(self.mid_frame, text=toDo.getTitle(), background="lightblue", font=self.h1, anchor="w")
        self.title.pack(fill="x", padx=10, pady="10")

        self.deadline = tk.Label(self.mid_frame, text=toDo.getDeadline(), background=self.light_green, font=self.normal_text)
        self.deadline.pack(fill="x", padx=10, pady="10")

        self.trash = tk.Label(self.note_frame, image=self.trash_icon, background=self.powder_blue)
        self.trash.pack(side="right")
        if (x == 9):
          toDo.TogglePin()
        if (toDo.getPin()):
          self.pin = tk.Label(self.note_frame, image=self.pin2_icon, background=self.powder_blue)
        else:
          self.pin = tk.Label(self.note_frame, image=self.pin1_icon, background=self.powder_blue)
        self.pin.pack(side="right")


      #add some invisible widget to add padding for new note button


        # progress = ttk.Progressbar(frame, variable=10, maximum=100)
        # label = tk.Label(self.content, text="test", font=("Arial", 18), background="white")
        # label.__dict__['id'] = x 
        # label.pack(padx=50, pady=50)
        # print(label.__dict__['id'])

      #Adjusting the size of the self.content frame to fill the canvas
      self.canvas.bind("<Configure>", self.on_canvas_resize)

      self.content.update_idletasks()

      # Update the scroll region of the canvas to match the content size
      self.canvas.config(scrollregion=self.canvas.bbox("all"))

      #Bind mouse scroll to canvas
      self.canvas.bind_all("<MouseWheel>", lambda event, canvas=self.canvas: on_windows_mouse_wheel(event, canvas))
      self.canvas.bind_all("<Button-4>", lambda event, canvas=self.canvas: on_linux_mouse_wheel(event, canvas))
      self.canvas.bind_all("<Button-5>", lambda event, canvas=self.canvas: on_linux_mouse_wheel(event, canvas))


    def on_progressbar_click(self, event):
      print("Progress bar clicked!")

    def test4(self):
      print("test")
      
    def clear(self, parent):
      for widget in parent.winfo_children():
        widget.destroy()
      self.create_note()

    def create_note(self):
      self.note_background_frame = tk.Frame(self.content, background=self.powder_blue)
      self.note_background_frame.pack(fill="both", expand=True, padx=10, pady=10)

      self.back_btn = tk.Button(self.note_background_frame, background=self.powder_blue, image=self.back_icon ,command=self.clear, highlightthickness=0, border=0)
      self.back_btn.pack(side="top", padx=10, pady=10, anchor="w")

      self.note_header = tk.Frame(self.note_background_frame, background=self.powder_blue)
      self.note_header.pack(side="top", fill="x", expand="true", padx=10)

      self.note_progress_frame = tk.Frame(self.note_header, background=self.powder_blue)
      self.note_progress_frame.pack(side="left")

      self.note_progress = ProgressBars(self.note_progress_frame, "top", 150, 20, self.powder_blue, "black", "green", self.set_progress_popup)
      self.note_progress.setProgress(10)

      # Need to decide to use button or not
      self.note_progress_btn = tk.Button(self.note_progress_frame, text="Update Progress", background="#90EE90", anchor="center", command=self.set_progress_popup, font=self.normal_text)
      self.note_progress_btn.pack(pady=10, side="top")

      self.note_mid_frame = tk.Frame(self.note_header, background=self.powder_blue)
      self.note_mid_frame.pack(side="left", fill="both", expand="true")

      self.note_title = tk.Text(self.note_mid_frame, height=1, background=self.powder_blue, font=self.monospace_h1)
      self.note_title.pack(fill="x", padx=10, pady="10")
      
      self.note_title.bind("<KeyPress>", lambda event: self.adjust_lines(event, self.note_title))
      self.note_title.bind("<Return>", lambda event: self.unfocus_field(event))
      self.note_title.insert("1.0", "Test")
      self.set_lines(self.note_title)

      self.note_deadline = tk.Button(self.note_mid_frame, text="Deadline: {}".format("toDo.getDeadline()"), background=self.light_green, font=self.h2, command=self.datepicker_popup)
      self.note_deadline.pack(padx=10, pady="10", side="bottom")

      self.note_description_label = tk.Label(self.note_background_frame, background=self.powder_blue, font=self.h2, text="Description: ", anchor="w")
      self.note_description_label.pack(padx=10, fill="x", expand=True)

      self.note_description = tk.Text(self.note_background_frame, background=self.powder_blue, height=50, font=self.normal_text)
      self.note_description.pack(pady=10, padx=10, side="bottom", expand=True, fill="both")
      self.note_description.bind("<Return>", self.unfocus_field_v2)
    
    def test2(self):
      self.test_frame = tk.Frame(self.refresh_frame, background="red")
      self.test_frame.pack(fill="both", expand="true")
      # toDoList = []
      # for x in range(10):
      #   toDo = ToDo(x, "Title 1{}".format(x), x*5, x, "Description 1{}".format(x))
      #   toDoList.append(toDo)

      #   self.note_frame = tk.Frame(self.refresh_frame, background=self.powder_blue)
      #   self.note_frame.pack(fill="x", expand="true", padx=10, pady=10)

      #   self.progress = ProgressBars(self.note_frame, "left", 75, 10, self.powder_blue, "black", "green")
      #   self.progress.setProgress(toDo.getProgress())

      #   self.mid_frame = tk.Frame(self.note_frame, background=self.powder_blue)
      #   self.mid_frame.pack(side="left", fill="both", expand="true")

      #   self.title = tk.Label(self.mid_frame, text=toDo.getTitle(), background="lightblue", font=self.h2, anchor="w")
      #   self.title.pack(fill="x", padx=10, pady="10")

      #   self.deadline = tk.Label(self.mid_frame, text=toDo.getDeadline(), background=self.light_green, font=self.normal_text)
      #   self.deadline.pack(fill="x", padx=10, pady="10")

      #   self.trash = tk.Label(self.note_frame, image=self.trash_icon, background=self.powder_blue)
      #   self.trash.pack(side="right")
      #   if (x == 2 or x == 5):
      #     toDo.setPin()
      #   if (toDo.getPin()):
      #     self.pin = tk.Label(self.note_frame, image=self.pin2_icon, background=self.powder_blue)
      #   else:
      #     self.pin = tk.Label(self.note_frame, image=self.pin1_icon, background=self.powder_blue)
      #   self.pin.pack(side="right")

    def set_progress_popup(self):
      popup = tk.Toplevel()
      popup.title("Set Progress")
      
      progress_label = tk.Label(popup, text="Enter Your Progress:", anchor="w", font=self.h1)
      progress_label.pack(padx=10, pady=10, expand=True, fill="x")

      progress_entry = tk.Entry(popup, font=self.h1)
      progress_entry.pack(padx=10)
      
      progress_submit = tk.Button(popup, text="Update Progress", font=self.h1, command=lambda:self.set_progress(progress_entry, popup))
      progress_submit.pack(padx=10, pady=10)
    
    def set_progress(self, progress_entry, popup):
      self.note_progress.setProgress(int(progress_entry.get()))
      popup.destroy()

    def adjust_lines(self, event, widget):
      self.set_lines(widget)

    def set_lines(self, widget):
      width = 15
      min = 1
      char_count = len(widget.get("1.0", "end-1c"))
      roof_division = -(char_count//-width)           #reversing floor division to do roof division
      new_height = max(1, roof_division)              
      widget.config(height = new_height) 
      
      #Used for testing
      #print(char_count)

    def unfocus_field(self, event):
      self.master.focus_set()
      return "break"
    
    def unfocus_field_v2(self, event):
      # print(f"Event state: {event.state}, Key: {event.keysym}")
      if event.state == 8:
        return self.unfocus_field(event)
      # elif event.state == 131080:
      #   pass
      
    def datepicker_popup(self):
      popup = tk.Toplevel(background=self.white_smoke)
      popup.title("Select deadline")
      cal = Calendar(popup, selectmode='day', date_pattern='dd-mm-yyyy', mindate=datetime.date.today(), showweeknumbers=False, firstweekday='sunday', font=self.h2, headersbackground = self.powder_blue, selectbackground=self.powder_blue, selectforeground="black" , background = self.pacific_blue, disableddaybackground=self.earlgrey, disableddayforeground=self.muskeg_grey, weekendbackground="white", weekendforeground="black", othermonthbackground=self.gainsboro, othermonthforeground="black", othermonthwebackground=self.gainsboro, othermonthweforeground="black", )
      cal.pack(pady=20, padx=20)

      deadline_btn = tk.Button(popup, text="Select", font=self.h2, background=self.pacific_blue, foreground="white", command=lambda:self.set_date(cal, popup))
      deadline_btn.pack(pady=10)

    def set_date(self, calendar, popup):
      deadline = calendar.get_date()
      popup.destroy()
      self.note_deadline.config(text="Deadline: {}".format(deadline))

      # Used for testing
      # print("Deadline : {}".format(deadline))

    def on_canvas_resize(self, event):
        # Update the size of content frame based on the canvas size
        width = event.width
        
        # Resize the content window to match the canvas size
        self.canvas.itemconfig(self.content_id, width=width)

  
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



#Detect mouse wheel scroll                                                           --Elden
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

