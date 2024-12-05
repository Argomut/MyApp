import tkinter as tk

class ProgressBars:
  def __init__(self, parent, length, thickness, wallpaper_colour, track_colour, fill_colour):
    self.__parent = parent
    self.__length = length
    self.__thickness = thickness
    self.__wallpaper_colour = wallpaper_colour
    self.__track_colour = track_colour
    self.__fill_colour = fill_colour
    
    # Creating a square background
    self.__canvas = tk.Canvas(self.__parent, width=self.__length, height=self.__length, bg=self.__wallpaper_colour)
    self.__canvas.pack()
        
    # Draw the background circle
    self.__progress_track = self.__canvas.create_oval(self.__thickness, self.__thickness, self.__length-self.__thickness, self.__length-self.__thickness, 
                                              outline=self.__track_colour, width=self.__thickness)
        
    # Draw the foreground arc (progress bar)
    self.__progress_fill = self.__canvas.create_arc(self.__thickness, self.__thickness, self.__length-self.__thickness, self.__length-self.__thickness, 
                                               start=90, extent=0, outline=self.__fill_colour, width=self.__thickness, style="arc")
        
    # Create a text item in the center to display the progress value
    self.__text = self.__canvas.create_text(self.__length/2, self.__length/2, text="0%", font=("Arial", 14, "bold"))

  def setProgress(self, progress):
    #exception handling
    # Limit value between 0 and 100
    # value = max(0, min(value, 100))
    self.__canvas.itemconfig(self.__text, text=f"{progress}%")

    progress = progress/100 * 360
    self.__canvas.itemconfig(self.__progress_fill, extent=progress)

  # use
  # progress_bar = ProgressBar(root, 200, 20, "white", "black", "green")
  # progress_bar.setprogress(10)