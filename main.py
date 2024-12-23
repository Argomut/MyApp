import subprocess
import sys

#install tkcalendar whihc is needed for the ToDo Module
subprocess.check_call([sys.executable, "-m", "pip", "install", "tkcalendar"])


import tkinter as tk
from tkcalendar import Calendar
import time
import datetime
import os
import threading
from tkinter import ttk, PhotoImage

#Gui Class
class Gui(tk.Frame):
    
    #Constructor
    def __init__(self, root):
      #Holding values that are shared to allow quick adjustments                     --Elden
      #Colours
      self.muskeg_grey = "#46484A"
      self.earlgrey = "#969A96"
      self.light_green = "#90EE90"
      self.pacific_blue = "#309CBA"
      self.powder_blue = "#C2EEF7"
      self.white_smoke = "#F5F5F5"
      self.gainsboro = "#DDDDDD"
      self.bleu_de_france = "#228BE6"

      #Fonts
      self.monospace_h1 = ("Consolas", 32, "bold")
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

      self.add_icon = tk.PhotoImage(file="icon//add.png")
      self.add_icon = self.add_icon.subsample(7)

      self.clock_icon = tk.PhotoImage(file="icon//clock.png")
      self.clock_icon = self.clock_icon.subsample(8)

      self.calculator_icon = tk.PhotoImage(file="icon//calculator.png")
      self.calculator_icon = self.calculator_icon.subsample(8)

      #Initialising parent class                                                     --Elden         
      super().__init__(root, background='#EEEEEE')
      self.main = self
      self.main.pack(fill="both", expand=1)    

      #Create main page
      self.main.create_main_page()


    def create_main_page(self):
      self.load_to_do_list()
  

    #Creating the header at the top                                                  --Elden
    def create_header(self):

      #Frame is used to allow padding with background colour
      self.header = tk.Frame(self.main, background=self.pacific_blue)
      self.header.pack(fill="x")

      self.header_title = tk.Label(self.header, text="Title", background=self.pacific_blue, font=self.h1, fg="white", )
      self.header_title.pack(side="left", padx=10, pady=10)


    #Creating a navigation bar at the bottom to navigate the 3 modules               --Elden 
    def create_navbar(self):
      self.navbar = tk.Frame(self.main, background=self.pacific_blue)
      self.navbar.pack(side="bottom", fill="x")
      self.navbar.columnconfigure(0, weight=1)
      self.navbar.columnconfigure(1, weight=1)
      self.navbar.columnconfigure(2, weight=1)

      self.btn1 = tk.Button(self.navbar, text="To-Do List", image=self.todo_icon, compound='top', background=self.pacific_blue, foreground="white", bd=1, command=self.load_to_do_list)
      self.btn1.grid(row=0, column=0, sticky="ew", padx=0, pady=0)

      self.btn2 = tk.Button(self.navbar, text="Pomodoro Timer", image=self.clock_icon, compound='top', background=self.pacific_blue, foreground="white", bd=1, command=self.load_pomodoro_timer)
      self.btn2.grid(row=0, column=1, sticky="ew", padx=0, pady=0)

      self.btn3 = tk.Button(self.navbar, text="GPA Calculator", image=self.calculator_icon, compound='top', background=self.pacific_blue, foreground="white", bd=1, command=self.load_gpa_calculator)
      self.btn3.grid(row=0, column=2, sticky="ew", padx=0, pady=0)

    ########## Start of To-Do List Manager Module ##########     
    
    #Clear page before loading To-Do List widgets                                    --Elden
    def load_to_do_list(self):
      self.clear(self.main)
      self.create_header()
      self.create_to_do_frame()
      self.create_navbar()
                      

    #Creating the main interface of To-Do List module                                
    def create_to_do_frame(self):

      self.header_title.config(text="To-Do List Manager")

      #Frame to position canvas and scrollbar
      self.container = tk.Frame(self.main)
      self.container.pack(side="top", fill="both", expand=True)

      #Using canvas to allow scrolling
      self.canvas = tk.Canvas(self.container,background=self.white_smoke)
      self.canvas.pack(side="left", fill="both", expand=True)

      #Create a scrollbar for the canvas
      self.scrollbar = tk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
      self.scrollbar.pack(side="right", fill="y")
      self.canvas.configure(yscrollcommand=self.scrollbar.set)
      

      #Create frame to store main content and adjusting frame to fill canvas
      self.content = tk.Frame(self.canvas, background=self.white_smoke)
      self.content_id = self.canvas.create_window((0, 0), window=self.content, anchor="nw")

      self.create_to_do_content()

      #binding mousescroll 
      self.canvas.bind_all("<MouseWheel>", lambda event, canvas=self.canvas: on_windows_mouse_wheel(event, canvas))
      self.canvas.bind_all("<Button-4>", lambda event, canvas=self.canvas: on_linux_mouse_wheel(event, canvas))
      self.canvas.bind_all("<Button-5>", lambda event, canvas=self.canvas: on_linux_mouse_wheel(event, canvas))

    def create_to_do_content(self):
      self.create_search()
      self.create_to_do_list()

    #Search feature
    def create_search(self):
      self.clear(self.content)  
      self.search_frame = tk.Frame(self.content, background=self.white_smoke)
      self.search_frame.pack(side="top", fill="x", expand=True, padx=10, pady=10)

      self.searchbar = tk.Entry(self.search_frame, font=self.normal_text)
      self.searchbar.pack(side="left", fill="x", expand="true")
      self.searchbar.bind("<Return>", lambda event: self.search(self.refresh_frame))

      self.search_btn = tk.Button(self.search_frame, text="Search", image=self.search_icon, compound="left", command=lambda: self.search(self.refresh_frame))
      self.search_btn.pack(side="left", padx=20)

      self.refresh_frame = tk.Frame(self.content, background=self.white_smoke)
      self.refresh_frame.pack(fill="x", expand="true")

    #Show list of all the ToDo tasks
    def create_to_do_list(self):
      self.header_title.config(text="To-Do List Manager")

      #List of individual ToDo Tasks
      for x in ToDo.searchToDoList(self.searchbar.get()):
        self.note_frame = tk.Frame(self.refresh_frame, background=self.powder_blue)
        self.note_frame.pack(fill="x", expand="true", padx=10, pady=10)
        self.note_frame.bind("<Button-1>", lambda event, obj=x: self.edit_note(obj))

        self.progress = ProgressBars(self.note_frame, "left", 75, 10, self.powder_blue, "black", "green", self.edit_note, x)
        self.progress.setProgress(x.getProgress())

        self.mid_frame = tk.Frame(self.note_frame, background=self.powder_blue)
        self.mid_frame.pack(side="left", fill="both", expand="true")
        self.mid_frame.bind("<Button-1>", lambda event, obj=x: self.edit_note(obj))

        self.title = tk.Label(self.mid_frame, text=x.getTitle(), background=self.powder_blue, font=self.monospace_h1, anchor="w", wraplength=360, justify="left")
        self.title.pack(fill="x", padx=10, pady="10")
        self.title.bind("<Button-1>", lambda event, obj=x: self.edit_note(obj))

        self.deadline = tk.Label(self.mid_frame, text="Deadline: " + x.getDeadline(), background=self.powder_blue, font=self.normal_text, anchor="w")
        self.deadline.pack(fill="x", padx=10, pady="10")
        self.deadline.bind("<Button-1>", lambda event, obj=x: self.edit_note(obj))

        self.trash = tk.Label(self.note_frame, image=self.trash_icon, background=self.powder_blue)
        self.trash.pack(side="right")
        self.trash.bind("<Button-1>", lambda event, obj=x, widget=self.note_frame: self.delete(obj, widget))

        if (x.getPin()=="True"):
          self.pin = tk.Label(self.note_frame, image=self.pin2_icon, background=self.powder_blue)
        else:
          self.pin = tk.Label(self.note_frame, image=self.pin1_icon, background=self.powder_blue)
        self.pin.pack(side="right")
        self.pin.bind("<Button-1>", lambda event, obj=x, widget=self.pin: self.pinning(obj,widget))

      self.lower_padding = tk.Label(self.refresh_frame, background=self.white_smoke)
      self.lower_padding.pack(pady=40)

      self.add_note_btn = tk.Button(self.container, image= self.add_icon, background=self.pacific_blue, highlightthickness=0, border=0, command=self.create_note)
      self.add_note_btn.place(x=520, y=740)
      # self.add_note_btn.place(x=520, y=450) #You can adjust the y according to your screen
      self.add_note_btn.lift()
      self.adjust_canvas()    

    #Clear previous widgets to allow new contents in the page
    def clear(self, parent):
      try:
        self.add_note_btn.destroy()
      except:
        pass
      for widget in parent.winfo_children():
        widget.destroy()

    #Clearing page before displaying todo list
    def search(self, parent):
      self.clear(parent)
      self.create_to_do_list()

    #Change the pin icon and save data when pin icon clicked
    def pinning(self, obj, widget):
      pin1 = self.pin1_icon
      pin2 = self.pin2_icon
      if obj.getPin() == "False":
        widget.config(image=pin2)
      else:
        widget.config(image=pin1)
      obj.togglePin()

    #Delete file and remove the widget when trash icon clicked
    def delete(self, obj, widget):
      obj.deleteFile()
      for child in widget.winfo_children():
        child.destroy()
      widget.destroy()
      self.adjust_canvas()
    
    #Create a new empty ToDo object and bring user to edit page
    def create_note(self):
      obj = ToDo()
      self.edit_note(obj)

    #Edit page for user to edit the task's data
    def edit_note(self, obj):
      self.clear(self.content)

      #Deleting navbar to prevent user going to other modules and not save the data
      self.clear(self.navbar)
      self.navbar.destroy()

      self.note_background_frame = tk.Frame(self.content, background=self.powder_blue)
      self.note_background_frame.pack(fill="both", expand=True, padx=10, pady=10)

      self.back_btn = tk.Button(self.note_background_frame, background=self.powder_blue, image=self.back_icon ,command=lambda:self.up_button(obj), highlightthickness=0, border=0)
      self.back_btn.pack(side="top", padx=10, pady=10, anchor="w")

      self.note_header = tk.Frame(self.note_background_frame, background=self.powder_blue)
      self.note_header.pack(side="top", fill="x", expand="true", padx=10)

      self.note_progress_frame = tk.Frame(self.note_header, background=self.powder_blue)
      self.note_progress_frame.pack(side="left")

      #Progress bar can be clicked instead of just button
      self.note_progress = ProgressBars(self.note_progress_frame, "top", 150, 20, self.powder_blue, "black", "green", self.set_progress_popup, obj)
      self.note_progress.setProgress(obj.getProgress())

      self.note_progress_btn = tk.Button(self.note_progress_frame, text="Update Progress", background="#90EE90", anchor="center", command= lambda: self.set_progress_popup(obj), font=self.normal_text)
      self.note_progress_btn.pack(pady=10, side="top")

      self.note_mid_frame = tk.Frame(self.note_header, background=self.powder_blue)
      self.note_mid_frame.pack(side="left", fill="both", expand="true")

      '''
      Insert the saved title to the field
      Automatically move to add and move to next line (not advance enough to move entire word yey)
      Unfocus the field when return key is pressed
      Save the contents when field is unfocus
      '''
      self.note_title = tk.Text(self.note_mid_frame, height=1, background=self.powder_blue, font=self.monospace_h1, wrap="word")
      self.note_title.pack(fill="x", padx=10, pady="10")
      self.note_title.insert("1.0", obj.getTitle())
      self.note_title.bind("<KeyPress>", lambda event: self.adjust_lines(event, self.note_title))
      self.note_title.bind("<Return>", lambda event: self.unfocus_field(event))
      self.note_title.bind("<FocusOut>", lambda event: self.submit_title(obj))
      self.set_lines(self.note_title)

      self.note_deadline = tk.Button(self.note_mid_frame, text="Deadline: {}".format(obj.getDeadline()), background=self.light_green, font=self.h2, command= lambda: self.datepicker_popup(obj))
      self.note_deadline.pack(padx=10, pady="10", side="bottom")

      self.note_padding = tk.Label(self.note_background_frame, background=self.powder_blue)
      self.note_padding.pack(padx=10, pady=10, side="bottom")

      self.note_description_label = tk.Label(self.note_background_frame, background=self.powder_blue, font=self.h2, text="Description: ", anchor="w")
      self.note_description_label.pack(padx=10, fill="x", expand=True)

      self.note_description = tk.Text(self.note_background_frame, background=self.powder_blue, height=32, font=self.normal_text, wrap="word")
      self.note_description.pack(pady=10, padx=10, side="bottom", expand=True, fill="both")
      self.note_description.insert("1.0", obj.getDescription())
      self.note_description.bind("<Return>", lambda event: self.unfocus_field_v2(event))
      self.note_description.bind("<FocusOut>", lambda event: self.submit_description(obj))
      
      self.adjust_canvas()


    #Return to main to-do list page
    def up_button(self, obj):
      obj.setTitle(self.note_title.get("1.0", "end-1c"))
      obj.setDescription(self.note_description.get("1.0", "end-1c"))
      self.create_to_do_content()
      self.create_navbar()


    #Create a popup for user to input their progress
    def set_progress_popup(self,obj):
      popup = tk.Toplevel()
      popup.title("Set Progress")
      
      progress_label = tk.Label(popup, text="Enter Your Progress:", anchor="w", font=self.h1)
      progress_label.pack(padx=10, pady=10, expand=True, fill="x")

      progress_entry = tk.Entry(popup, font=self.h1)
      progress_entry.pack(padx=10)
      progress_entry.insert(0, obj.getProgress())

      label = tk.Label(popup, text="Please enter an integer (1-100): ", foreground="red")
      label.pack_forget()
      
      progress_submit = tk.Button(popup, text="Update Progress", font=self.h1, command=lambda:self.set_progress(progress_entry, popup, obj, label))
      progress_submit.pack(padx=10, pady=10)

      popup.geometry("320x190+{}+{}".format(self.main.winfo_rootx() + (self.main.winfo_width() - 320)//2, self.main.winfo_rooty() + (self.main.winfo_height() - 630)//2))
    
    #Save Title
    def submit_title(self, obj):
      obj.setTitle(self.note_title.get("1.0", "end-1c"))
    
    #Save description
    def submit_description(self, obj):
      obj.setDescription(self.note_description.get("1.0", "end-1c"))

    #Validate input, save input, and close popup
    def set_progress(self, progress_entry, popup, obj, label):
      label.pack_forget()
      if (obj.setProgress(progress_entry.get())):
        self.note_progress.setProgress(obj.getProgress())
        popup.destroy()
      else:
        label.pack(before=progress_entry)
    
    #Create a popup to select deadline
    def datepicker_popup(self, obj):
      popup = tk.Toplevel(background=self.white_smoke)
      popup.title("Select deadline")
      try:
        date = datetime.datetime.strptime(obj.getDeadline(), "%Y-%m-%d")
        cal = Calendar(popup, selectmode='day', date_pattern='yyyy-mm-dd', mindate=datetime.date.today(), showweeknumbers=False, firstweekday='sunday', font=self.h2, 
                     headersbackground = self.powder_blue, selectbackground=self.powder_blue, selectforeground="black" , background = self.pacific_blue, 
                     disableddaybackground=self.earlgrey, disableddayforeground=self.muskeg_grey, weekendbackground="white", weekendforeground="black", 
                     othermonthbackground=self.gainsboro, othermonthforeground="black", othermonthwebackground=self.gainsboro, othermonthweforeground="black", 
                     year = int(date.strftime("%Y")), month = int(date.strftime("%m")), day = int(date.strftime("%d")))
      except:
        #If deadline is none
        cal = Calendar(popup, selectmode='day', date_pattern='yyyy-mm-dd', mindate=datetime.date.today(), showweeknumbers=False, firstweekday='sunday', font=self.h2, 
                      headersbackground = self.powder_blue, selectbackground=self.powder_blue, selectforeground="black" , background = self.pacific_blue, 
                      disableddaybackground=self.earlgrey, disableddayforeground=self.muskeg_grey, weekendbackground="white", weekendforeground="black", 
                      othermonthbackground=self.gainsboro, othermonthforeground="black", othermonthwebackground=self.gainsboro, othermonthweforeground="black")
      cal.pack(pady=20, padx=20)
      deadline_frame = tk.Frame(popup, background=self.white_smoke)
      deadline_frame.pack(pady=10, side="bottom")
      none_deadline_btn = tk.Button(deadline_frame, text="No Deadline", font=self.h2, background=self.pacific_blue, foreground="white", command=lambda:self.set_date("None", popup, obj))
      none_deadline_btn.pack(padx=10, side="left")
      deadline_btn = tk.Button(deadline_frame, text="Select", font=self.h2, background=self.pacific_blue, foreground="white", command=lambda:self.set_date(cal, popup, obj))
      deadline_btn.pack(padx=10, side="left")
      popup.geometry("420x355+{}+{}".format(self.main.winfo_rootx() + (self.main.winfo_width() - 420)//2, self.main.winfo_rooty() + (self.main.winfo_height() - 755)//2))

    #save selected deadline and close popup
    def set_date(self, calendar, popup, obj):
      if calendar == "None": deadline = "None"
      else: deadline = calendar.get_date()
      popup.destroy()
      self.note_deadline.config(text="Deadline: {}".format(deadline))
      obj.setDeadline(deadline)

      # Used for testing
      # print("Deadline : {}".format(deadline))

    #Adjusting line for Title
    def adjust_lines(self, event, widget):
      self.set_lines(widget)
      self.adjust_canvas()

    def set_lines(self, widget):
      width = 15
      min = 1
      char_count = len(widget.get("1.0", "end-1c"))
      roof_division = -(char_count//-width)           #Reversing floor division to do roof division
      new_height = max(min, roof_division)              
      widget.config(height = new_height) 
      
      #Used for testing
      #print(char_count)

    #Exit field when return pressed
    def unfocus_field(self, event):
      self.master.focus_set()
      return "break"
    
    #Exit field when return pressed, move to next line when alt key is pressed too
    def unfocus_field_v2(self, event):
      if event.state == 8:              #return only
        return self.unfocus_field(event)
      elif event.state == 131080:       #return + alt key
        pass
      else:                             #return + shift/ctrl/... 
        return "break"

      # Used for testing
      # print(f"Event state: {event.state}, Key: {event.keysym}")
    
    #Resize content window to match canvas size
    def adjust_canvas(self):
      self.canvas.bind("<Configure>", self.on_canvas_resize)
      self.content.update_idletasks()
      self.canvas.config(scrollregion=self.canvas.bbox("all"))
    
    def on_canvas_resize(self, event):
        width = event.width
        self.canvas.itemconfig(self.content_id, width=width)



########## End of To-Do List Manager Module ##########

    def load_pomodoro_timer(self):
          self.clear(self.main)
          self.create_header()
          self.header_title.config(text="Pomodoro Timer")
          PomodoroTimer(self.main)
          self.create_navbar()

    def load_gpa_calculator(self):
      self.clear(self.main)
      self.create_header()
      self.header_title.config(text="GPA Calculator")
      #self.create_gpa_calculator
      self.create_navbar()


#Detect mouse wheel scroll                                                           --Elden
#Windows mouse wheel
def on_windows_mouse_wheel(event, canvas):
  if not canvas.winfo_exists(): 
    return
  elif event.delta > 0:
    canvas.yview_scroll(-1, "units")  # Scroll up
  else:
    canvas.yview_scroll(1, "units")   # Scroll down

#Linux mouse wheel
def on_linux_mouse_wheel(event, canvas):
  if not canvas.winfo_exists(): 
    return
  elif event.num == 4:
    canvas.yview_scroll(-1, "units")
  elif event.num == 5:
    canvas.yview_scroll(1, "units")

########## Custom Circular Progress Bar) ##########


class ProgressBars:
  
  #Constructor
  def __init__(self, parent, side, length, thickness, wallpaper_colour, track_colour, fill_colour, external_function, argument = ""):
    self.__parent = parent
    self.__side = side
    self.__length = length
    self.__thickness = thickness
    self.__wallpaper_colour = wallpaper_colour
    self.__track_colour = track_colour
    self.__fill_colour = fill_colour
    self.__external_function = external_function
    self.__argument = argument
    
    # Creating a square background                                              -Elden
    self.__canvas = tk.Canvas(self.__parent, width=self.__length, height=self.__length, bg=self.__wallpaper_colour, highlightbackground=self.__wallpaper_colour)
    self.__canvas.pack(side=self.__side)

    #bind the progress bar to a mouseclick                                      -Elden
    self.__canvas.bind("<Button-1>", self.on_click)
        
    # Draw the background circle                                                -Elden
    self.__progress_track = self.__canvas.create_oval(self.__thickness, self.__thickness, self.__length-self.__thickness, self.__length-self.__thickness, 
                                              outline=self.__track_colour, width=self.__thickness)
        
    # Draw the foreground arc (progress bar)                                    -Elden
    self.__progress_fill = self.__canvas.create_arc(self.__thickness, self.__thickness, self.__length-self.__thickness, self.__length-self.__thickness, 
                                               start=90, extent=0, outline=self.__fill_colour, width=self.__thickness, style="arc")
        
    # Create a text item in the center to display the progress value
    self.__text = self.__canvas.create_text(self.__length/2, self.__length/2, text="0%", font=("Arial", 14, "bold"))

  #Update the progress                                                          -Elden
  def setProgress(self, progress):
    self.__canvas.itemconfig(self.__text, text=f"{progress}%")

    progress = int(progress)/100 * 360
    self.__canvas.itemconfig(self.__progress_fill, extent=progress)

    #if progress_fill goes full 360, arc will disappear, thus change track colour for the appearance
    if progress == 360:
      self.__canvas.itemconfig(self.__progress_track, outline=self.__fill_colour)
    else:
      self.__canvas.itemconfig(self.__progress_track, outline=self.__track_colour)
  
  #Execute external functions                                                   -Elden
  def on_click(self, event):
    self.__external_function(self.__argument)

  def on_click_with_event(self, event):
    self.__external_function(event)

  # Use
  # progress_bar = ProgressBar(root, 200, 20, "white", "black", "green", function())
  # progress_bar.setprogress(10)

########## Class for To-Do List Manager Module #########

class ToDo:
  #Static variables
  __next_id = 0
  __max_id = 0
  __toDoList = []

  #Constructor
  def __init__(self, title="Untitled", progress=0, deadline="None", description="", existing=False):
    self.__id =self.getNextId()
    self.__title = title
    self.__progress = progress
    self.__deadline = deadline
    self.__description = description
    self.__pinned = "False"
    self.incNextId()
    if not existing:
      self.generateFile()
      self.__toDoList.append(self)
     
      
  #Getters and Setters
  def getId(self):
    return self.__id

  def setId(self, id):
    self.__id = id
  

  def getTitle(self):
    return self.__title
  
  def setTitle(self, title):
    self.__title = title
    self.generateFile()

  
  def getProgress(self):
    return self.__progress
  
  def setProgress(self, progress):
    try:
      progress = round(float(progress))
    except:
      return False
    else: 
      self.__progress = min(100,max(0,progress))
      self.generateFile()
      return True

  
  def getDeadline(self):
    return self.__deadline
  
  def setDeadline(self, deadline):
    self.__deadline = deadline
    self.generateFile()

  
  def getDescription(self):
    return self.__description
  
  def setDescription(self, description):
    self.__description = description
    self.generateFile()

  
  def getPin(self):
    return self.__pinned
  
  def setPin(self, pin):
    self.__pinned = pin
    self.generateFile()
  

  #Other Methods
  def togglePin(self):
    if self.getPin() == "False": self.setPin("True")
    else: self.setPin("False")

  #Used in file creation
  def toString(self):
    return ("{}\n{}\n{}\n{}\n{}\n{}".format(self.getId(), self.getTitle(), self.getProgress(), self.getDeadline(), self.getPin(), self.getDescription()))
  
  #Used for testing
  def __repr__(self):
    return "ToDo({},{},{},{},{},{})".format(self.getId(), self.getTitle(), self.getProgress(), self.getDeadline(), self.getPin(), self.getDescription())

  #Find file using Id
  def getFile(self, id):
    return("ToDoFiles//ToDo{}.txt".format(id))
  
  # def getFile(self):
  #   return("ToDoFiles//ToDo{}.txt".format(self.getId()))

  #File creation/overwrite
  def generateFile(self):
    try:
      file = open(self.getFile(self.getId()), "w")
      file.write(self.toString())
      file.close()
    except:
      print("Error creating file")

  #Assigning values of the files to the object
  def readFile(self, id):
    try:
      file = open(self.getFile(id), "r")
      self.setId(file.readline().strip())
      self.setTitle(file.readline().strip())
      self.setProgress(file.readline().strip())
      self.setDeadline(file.readline().strip())
      self.setPin(file.readline().strip())
      self.setDescription(file.read().strip())
      file.close()
    except:
      print("Error reading file")


  #Deleting file and removing from list
  def deleteFile(self):
    try:
      self.__toDoList.remove(self)
      if os.path.exists(self.getFile(self.getId())):
        os.remove(self.getFile(self.getId()))
      else:
        print("File has already been removed")
    except:
      print("Error removing file")
  
  #class methods
  @classmethod
  def setNextId(cls, next_id):
    cls.__next_id = next_id
    try:
      file = open("ToDoFiles//ToDoConfig.txt", "w")
      file.write(cls.__next_id)
    except:
      print("Error writing file")
    file.close()

  #Next Id increment
  @classmethod
  def incNextId(cls):
    cls.__next_id = int(cls.__next_id) + 1
    cls.setNextId(str(cls.__next_id))
  
  @classmethod
  def getNextId(cls):
    try:
      file = open("ToDoFiles//ToDoConfig.txt", "r")
      cls.__next_id = file.read().strip()
      try: int(cls.__next_id)
      except: cls.__next_id = "1"
      else: 
        if cls.__next_id < 1:
          cls.__next_id = "1"
    except:
      cls.__next_id = 1
      file = open("ToDoFiles//ToDoConfig.txt", "w")
      file.write(str(cls.__next_id))
    while os.path.exists("ToDoFiles//ToDo{}.txt".format(cls.__next_id)):
      cls.incNextId()
    file.close()
    return cls.__next_id

  #Recovery in case folder and files were deleted or modified
  @classmethod
  def fixConfig(cls):
    if not os.path.exists("ToDoFiles"): os.makedirs("ToDoFiles", exist_ok=True)
    fixing_range = 10000
    for x in range(int(cls.getNextId()) + fixing_range, 0, -1):
      if os.path.exists("ToDoFiles//ToDo{}.txt".format(x)):
        cls.__max_id = str(x)
        break

  @classmethod
  def initialiseToDoList(cls):
    # del cls.__toDoList[-1]
    cls.fixConfig()
    for x in range(int(cls.__max_id)+1):
      if os.path.exists("ToDoFiles//ToDo{}.txt".format(x)):
        obj = ToDo(existing=True)
        obj.readFile(x)
        cls.__toDoList.append(obj)

  #Sorting so that earlier deadlines are displayed first
  @classmethod
  def sortToDoList(cls):
    cls.__toDoList.sort(key=lambda todo: (todo.__deadline, todo.__pinned))

  @classmethod
  def getToDoList(cls):
    cls.sortToDoList()
    return cls.__toDoList

  #Search function to filter results
  @classmethod
  def searchToDoList(cls, search):
    pinnedSearchList = []
    unpinnedSearchList = []
    for x in cls.getToDoList():
      if search.upper().strip() in x.getTitle().upper().strip():
        if (x.getPin() == "False"):
          unpinnedSearchList.append(x)
        else:
          pinnedSearchList.append(x)
    pinnedSearchList.extend(unpinnedSearchList)
    return pinnedSearchList



class PomodoroTimer:

    def __init__(self,argu=""):
        self.root = argu

        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font = ("Arial", 16))
        self.s.configure("TButton", font = ("Arial", 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill = "both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)
        
        self.grid_button = ttk.Button(self.grid_layout, text = "Start", command = self.start_timer_thread)
        self.grid_button.grid(row=0,column=0)
        self.skip_button = ttk.Button(self.grid_layout, text = "Skip", command = self.skip_timer)
        self.skip_button.grid(row=0,column=1)
        self.reset_button = ttk.Button(self.grid_layout, text = "Reset", command = self.reset_timer)
        self.reset_button.grid(row=0,column=3)
        self.pomodoro_label = ttk.Label(self.grid_layout, text = "Pomodoro: 0", font = ("Arial", 16))
        self.pomodoro_label.grid(row=1,column=1,columnspan=2,pady=10)

        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font = ("Arial", 48))
        self.pomodoro_timer_label.pack(pady=20)
        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font = ("Arial", 48))
        self.short_break_timer_label.pack(pady=20)
        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font = ("Arial", 48))
        self.long_break_timer_label.pack(pady=20)

        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short break")
        self.tabs.add(self.tab3, text="Long break")

        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        self.running = False
        

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True
            
    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1
            
        if timer_id == 1:
            full_seconds = 60 * 25
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds ,60)
                self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_label.config(text=f"Pomodoros: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                    self.start_timer()
                else:
                    self.tabs.select(1)
                    self.start_timer()
        elif timer_id == 2:
            full_seconds = 60 * 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds ,60)
                self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
            self.start_timer()
        elif timer_id == 3:
            full_seconds = 60 * 15
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds ,60)
                self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
            self.start_timer()
                
    def skip_timer(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodoro_timer_label.config(text="25:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="15:00")

        self.stopped = True
        self.skipped = True
            
    def reset_timer(self):
        self.tabs.select(0)
        self.stopped = True
        self.skipped = False
        self.pomodoros = 0
        self.pomodoro_timer_label.config(text="25:00")
        self.short_break_timer_label.config(text="05:00")
        self.long_break_timer_label.config(text="15:00")
        self.pomodoro_label.config(text="Pomodoro: 0")
        self.running = False


root = tk.Tk()
root.title("My App")
root.geometry("624x936")  #480x720 576x864 624x936 672x1008 720x1280
root.resizable(False, True)

#Set up for ToDo Module             -Elden
ToDo.initialiseToDoList()

#Initialise Gui
my_app_instance = Gui(root)
root.mainloop()