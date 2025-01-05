import tkinter as tk


def on_windows_mouse_wheel(event, canvas):
  if not canvas.winfo_exists():
    return
  elif event.delta > 0:
    canvas.yview_scroll(-1, "units")  # Scroll up
  else:
    canvas.yview_scroll(1, "units")   # Scroll down


def adjust_canvas():
    canvas.bind("<Configure>", on_canvas_resize)
    container.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
   
def on_canvas_resize(event):
    width = event.width
    canvas.itemconfig(container_id, width=width)


def create_popup():
    popup = tk.Toplevel()
    popup.title("Add New Job Listing")


    popup_company = tk.Label(popup, image=big_company_icon, anchor="w", text="Hiring Company 1", compound="top", font=normal_text)
    popup_company.pack(padx=10, pady=10, fill="x")


    popup_title_label = tk.Label(popup, text="Position", font=h1, anchor="w", justify="left")
    popup_title_label.pack(padx=10, pady=10, fill="x")


    popup_title = tk.Entry(popup, font=h1)
    popup_title.pack(padx=10, fill="x")


    popup_salary_label = tk.Label(popup, text="Salary", font=h1, anchor="w", justify="left")
    popup_salary_label.pack(padx=10, pady=10, fill="x")


    popup_salary = tk.Entry(popup, font=h1)
    popup_salary.pack(padx=10, fill="x")


    popup_requirements_label = tk.Label(popup, text="Requirements", font=h1, anchor="w", justify="left")
    popup_requirements_label.pack(padx=10, pady=10, fill="x")


    popup_requirements = tk.Text(popup, font=h1, height=8)
    popup_requirements.pack(padx=10, fill="x")


    popup_submit = tk.Button(popup, text="Add Job Listing", font=h1, background="#AAF0C9", command=popup.destroy)
    popup_submit.pack(padx=10, pady=10)


    popup.geometry("900x700")


root = tk.Tk()
root.title("FA")
root.geometry("1080x920")
root.resizable(True, True)


h1 = ("Garamond ", 20)
h2 = ("Arial", 18)
normal_text = ("Times New Roman",16)


#Note you need to have the png files in the directory to work, google
job_icon = tk.PhotoImage(file="job.png")
job_icon = job_icon.subsample(6)


company_icon = tk.PhotoImage(file="company.png")
company_icon = company_icon.subsample(9)


big_company_icon = tk.PhotoImage(file="company.png")
big_company_icon = big_company_icon.subsample(5)


notification_icon = tk.PhotoImage(file="notification.png")
notification_icon = notification_icon.subsample(4)


add_icon = tk.PhotoImage(file="icon//add.png")
add_icon = add_icon.subsample(7)


search_icon = tk.PhotoImage(file="icon//search.png")
search_icon = search_icon.subsample(12)


header_frame = tk.Frame(root, background="green")
header_frame.pack(side= "top", fill="x")


header_title = tk.Label(header_frame, text="Company X", font=h1, background="green", foreground="white")
header_title.pack(side="left", padx=10, pady=10)


content_frame = tk.Frame(root, background="blue")
content_frame.pack(side="top", fill="both", expand=True)


canvas = tk.Canvas(content_frame)
canvas.pack(side="left", fill="both", expand=True)


scrollbar = tk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)


container = tk.Frame(canvas)
container_id = canvas.create_window((0,0), window=container, anchor="nw")


canvas.bind_all("<MouseWheel>", lambda event, canvas=canvas: on_windows_mouse_wheel(event, canvas))


search_frame = tk.Frame(container)
search_frame.pack(side="top", fill="x", expand=True, padx=10, pady=10)


searchbar = tk.Entry(search_frame, font=normal_text)
searchbar.pack(side="left", fill="x", expand=True)


search_btn = tk.Button(search_frame, text="Search", image=search_icon, compound="left")
search_btn.pack(side="left", padx=20)


job1_frame = tk.Frame(container, background="lightgreen")
job1_frame.pack(padx=10, pady=10, fill="x")


company_logo = tk.Label(job1_frame, image=big_company_icon, anchor="w", text="Hiring Company 1", compound="top", font=normal_text, background="lightgreen")
company_logo.pack(padx=10, pady=10, fill="x")


job1_title = tk.Label(job1_frame, text="Sales Manager", font=h2, anchor="w", background="lightgreen")
job1_title.pack(padx=10, pady=10, fill="x")


job1_salary = tk.Label(job1_frame, text="Salary: RM 10k", font=h2, anchor="w", background="lightgreen")
job1_salary.pack(padx=10, pady=10, fill="x")


job1_requirement = tk.Label(job1_frame, text="Must be more than 18 years old\nMust have personal transportation\nMust live near location X\nMust have 2 years of experience\nMust have a diploma in business administration\n...", font=h2, anchor="w", justify="left", background="lightgreen")
job1_requirement.pack(padx=10, pady=10, fill="x")


job2_frame = tk.Frame(container, background="lightgreen")
job2_frame.pack(padx=10, pady=10, fill="x")


company_logo = tk.Label(job2_frame, image=big_company_icon, anchor="w", text="Hiring Company 1", compound="top", font=normal_text, background="lightgreen")
company_logo.pack(padx=10, pady=10, fill="x")


job2_title = tk.Label(job2_frame, text="Sales Assistant", font=h2, anchor="w", background="lightgreen")
job2_title.pack(padx=10, pady=10, fill="x")


job2_salary = tk.Label(job2_frame, text="Salary: RM 8k", font=h2, anchor="w", background="lightgreen")
job2_salary.pack(padx=10, pady=10, fill="x")


job2_requirement = tk.Label(job2_frame, text="Must be more than 18 years old\nMust have personal transportation\nMust live near location X\nMust have 1 years of experience\n...", font=h2, anchor="w", justify="left", background="lightgreen")
job2_requirement.pack(padx=10, pady=10, fill="x")


add_listing_btn = tk.Button(content_frame, image=add_icon, highlightthickness=0, border=0, background="green", command=create_popup)
add_listing_btn.place(x=980, y=700)




adjust_canvas()


navbar_frame = tk.Frame(root, background="green")
navbar_frame.pack(side="bottom", fill="x")


nav_btn1 = tk.Button(navbar_frame, image=job_icon, text="Job Listing", compound="top", font=normal_text, background="#AAF0C9")
nav_btn1.pack(side="left", expand=True, fill="both")
nav_btn2 = tk.Button(navbar_frame, image=notification_icon, text="Notification", compound="top", font=normal_text, background="#AAF0C9")
nav_btn2.pack(side="left", expand=True, fill="both")
nav_btn3 = tk.Button(navbar_frame, image=company_icon, text="Account", compound="top", font=normal_text, background="#AAF0C9")
nav_btn3.pack(side="left", expand=True, fill="both")


root.mainloop()