#Wong GuanHao
import tkinter as tk
import time
import threading
from tkinter import ttk, PhotoImage

class PomodoroTimer:

    def __init__(self,argu=""):
        self.root = argu

        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font = ("Arial", 16))
        self.s.configure("TButton", font = ("Arial", 16))

        #create tabs for each timer
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill = "both", pady=10, expand=True)
        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short break")
        self.tabs.add(self.tab3, text="Long break")

        #create buttons to start, stop and reset timer
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)
        self.grid_button = ttk.Button(self.grid_layout, text = "Start", command = self.start_timer_thread)
        self.grid_button.grid(row=0,column=0)
        self.skip_button = ttk.Button(self.grid_layout, text = "Skip", command = self.skip_timer)
        self.skip_button.grid(row=0,column=1)
        self.reset_button = ttk.Button(self.grid_layout, text = "Reset", command = self.reset_timer)
        self.reset_button.grid(row=0,column=3)
        
        #create a label for pomodoro count
        self.pomodoro_label = ttk.Label(self.grid_layout, text = "Pomodoro: 0", font = ("Arial", 16))
        self.pomodoro_label.grid(row=1,column=1,columnspan=2,pady=10)

        #create label for the timer for each tab
        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font = ("Arial", 48))
        self.pomodoro_timer_label.pack(pady=20)
        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font = ("Arial", 48))
        self.short_break_timer_label.pack(pady=20)
        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font = ("Arial", 48))
        self.long_break_timer_label.pack(pady=20)

       #default values of the Pomodoro Timer
        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        self.running = False
        
    #Function to able Timer to run while in another tab
    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True
          
    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1 #each timer starts with its correct time given 
            
        if timer_id == 1:
            full_seconds = 60 * 25
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds ,60)
                self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1) #delay for when the timer updates
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_label.config(text=f"Pomodoros: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2) #switch to long break timer
                    self.start_timer()
                else:
                    self.tabs.select(1) #switch to short break timer
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
            
    #reset everything to its default values
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