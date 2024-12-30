########## Custom Circular Progress Bar (Elden) ##########


import tkinter as tk

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