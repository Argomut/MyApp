#Pang Qian Fu
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
import os

class cgpa():
    def __init__(self,argu=""):
        self.newwindow = argu
        self.initialfile()
        self.frame1 = Frame(self.newwindow)
        self.frame1.pack()
        
        lbl = Label(self.frame1,text="CGPA Calculator",font=("Times New Roman",48,"bold"),anchor="n")
        lbl.pack(expand = True)
        self.started()
        
        #self.newwindow.mainloop()
        
    def started(self):
        self.frame2 = Frame(self.newwindow)
        self.frame3 = Frame(self.newwindow)
        self.frame2.pack(pady=40)
        self.frame3.pack(pady=20)
        entertxt = Label(self.frame2,text="Please choose your number of course:",font=("Times New Roman",20,"bold"))

        self.sltnumc = IntVar()
        self.sltnumc.set("0")
        cnum = [1,2,3,4,5,6,7,8,9,10]
        numcourse = ttk.Combobox(self.frame2,textvariable=self.sltnumc,values=cnum,font=("Times New Roman", 16),state="readonly",width=5,justify="center")
        
        entertxt.grid(row = 1,column = 1)
        numcourse.grid(row = 1,column = 2,padx = 50)
        numcourse.bind("<<ComboboxSelected>>",lambda event:self.printcourse(self.frame3))
        
    def printcourse(self,event):
        for widget in self.frame3.winfo_children():
            widget.destroy()
        
        lblc = Label(self.frame3,text="Course",font=("Times New Roman",16,"bold"))
        lblcdt = Label(self.frame3,text="Credit Hours Earn",font=("Times New Roman",16,"bold"))
        lblcg = Label(self.frame3,text="Grade",font=("Times New Roman",16,"bold"))
        lblc.grid(row = 0,column = 1)
        lblcdt.grid(row = 0,column = 2)
        lblcg.grid(row = 0,column = 3)

        gradelist = ["A+","A","A-","B+","B","B-","C+","C","F"]
        scn = int(self.sltnumc.get())
        self.cvars = []
        self.cdtvars = []        
        
        for a in range(1,scn+1):
            cg = StringVar()
            cg.set("Select grade")
            self.cvars.append(cg)
            cdt = StringVar()
            cdt.set("Enter credit hours")
            self.cdtvars.append(cdt)
            
            lblcgrid = Label(self.frame3,text=f"Course {a}:",font=("Times New Roman",20,"bold"))
            cdtearn = Entry(self.frame3,textvariable=cdt,font=("Times New Roman", 14),justify="center",width=15)
            cgrid = ttk.Combobox(self.frame3,textvariable=cg,values=gradelist,font=("Times New Roman", 14),state="readonly",width=10,justify="center") 
            lblcgrid.grid(row = a,column = 1,padx = 50)
            cdtearn.grid(row = a,column = 2,padx = 20)
            cgrid.grid(row = a,column = 3,padx = 20)
            cdtearn.bind("<FocusIn>",self.fi)
        
        self.btnok = Button(self.frame3,text="Done",bg="lightblue",activebackground="lightgrey",relief="ridge",bd=3,font=("Arial",15,"bold"),cursor="hand2",command=self.getcc)
        self.btnok.grid(row = scn+1,column=2,pady=20,sticky="ew")
        
    def fi(self,event):
        event.widget.select_range(0,END)
        event.widget.icursor(END)
                            
    def getcc(self):
        totalcredit = 0
        for idx,(cdtvar,gradevar) in enumerate(zip(self.cdtvars,self.cvars),start=1):
            try:
                ccredit = cdtvar.get()
                grade = gradevar.get()
                
                if ccredit.strip() == "Enter credit hours":
                    messagebox.showerror("Missing Credit Hours",f"Missing Input in Course{idx} : Please enter credit hours!")
                    self.cdtvars[idx - 1].set("Enter credit hours")
                    return
                if not ccredit.isdigit():
                    messagebox.showerror("Invalid Input",f"Invalid Input in Course{idx} : Credit Hours must be a number")
                    return
                credit = int(ccredit)
                if credit < 0:
                    messagebox.showerror("Invalid Value",f"Invalid Input in Course{idx} : Credit hours cannot be negative!")
                    self.cdtvars[idx - 1].set("Enter credit hours")
                    return
                if grade == "Select grade":
                    messagebox.showerror("Missing Grade",f"Invalid Input in Course{idx} : Please select a grade")
                    return
                    
                totalcredit += credit 
                print(idx,credit,grade,totalcredit)
            
            except Exception as e:
                messagebox.showerror("Unexpected Error",f"Something wrong:{e}")
                return
        self.cltcgpa(self.cdtvars,self.cvars,totalcredit)
            
    def cltcgpa(self,cdtvars,cvars,totalcredit):
        cdtinput = [int(cdtvar.get()) for cdtvar in cdtvars]
        gradeinput = [cvar.get() for cvar in cvars]
        gradepoint = {"A+":4.00,"A":4.00,"A-":3.75,"B+":3.50,"B":3.00,"B-":2.75,"C+":2.50,"C":2.00,"F":0.00}
        qualitypoint = []
        #print(cdtinput,gradeinput,totalcredit)
        for cdtearn,grd in zip(cdtinput,gradeinput):
            grdpoint = gradepoint.get(grd,0.00)
            qualitypoint.append(cdtearn * grdpoint)
            #print(grdpoint,qualitypoint)

        totalqp = sum(qualitypoint)
        gpa = totalqp/totalcredit
        global tcgpa,ttotalcredit
        tcgpa += totalqp
        ttotalcredit += totalcredit
        acgpa = tcgpa / ttotalcredit
        
        self.recordfile(gpa,totalcredit,acgpa,ttotalcredit)
        self.displaygpa(gpa,totalcredit,acgpa,ttotalcredit)
    
    def recordfile(self,gpa,totalcredit,acgpa,ttotalcredit):
        try:
            with open('GPAfile//gpa.txt','a') as f:
                f.write(f"{gpa:.4f}\n")
                f.write(f"{totalcredit:.1f}\n")
                f.write(f"{acgpa:.4f}\n")
                f.write(f"{ttotalcredit:.1f}\n")
        except Exception as e:
            print(f"Error Opening File:{e}")

    def displaygpa(self,gpa,totalcredit,acgpa,ttotalcredit):
        self.btnok.config(state="disabled",cursor="arrow")
        self.frame4 = Frame(self.newwindow)
        self.frame4.pack(pady=20)
        self.frame5 = Frame(self.newwindow)
        self.frame5.pack(pady=20)
        
        showgpa = Label(self.frame4,text=f"{gpa:.4f}",font=("Times New Roman",30,"bold")).grid(row=1,column=0,padx=40)
        showgpaw = Label(self.frame4,text=" GPA ",font=("Times New Roman",14,"bold")).grid(row=2,column=0,padx=40)
        showcdt = Label(self.frame4,text=f"{totalcredit:.1f}",font=("Times New Roman",30,"bold")).grid(row=3,column=0,padx=40)
        showcdtw = Label(self.frame4,text=" Credit Hours Earned ",font=("Times New Roman",14,"bold")).grid(row=4,column=0,padx=40)
        showcgpa = Label(self.frame4,text=f"{acgpa:.4f}",font=("Times New Roman",30,"bold")).grid(row=1,column=1,padx=40)
        showcgpaw = Label(self.frame4,text=" CGPA ",font=("Times New Roman",14,"bold")).grid(row=2,column=1,padx=40)
        showtcdt = Label(self.frame4,text=f"{ttotalcredit:.1f}",font=("Times New Roman",30,"bold")).grid(row=3,column=1,padx=40)
        showtcdtw = Label(self.frame4,text=" Total Credit Hours Earned ",font=("Times New Roman",14,"bold")).grid(row=4,column=1,padx=40)

        btnreset = Button(self.frame5,text=" Reset ",bg="lightblue",activebackground="lightgrey",relief="ridge",bd=1,font=("Arial",15,"bold"),cursor="hand2",command=self.reset).grid(row=1,column=1,padx=20)
        btnns = Button(self.frame5,text=" Next Sem ",bg="lightblue",activebackground="lightgrey",relief="ridge",bd=1,font=("Arial",15,"bold"),cursor="hand2",command=self.ns).grid(row=1,column=2,padx=20)
        btnexit = Button(self.frame5,text=" History ",bg="lightblue",activebackground="lightgrey",relief="ridge",bd=1,font=("Arial",15,"bold"),cursor="hand2",command=self.history).grid(row=1,column=3,padx=20)

    def reset(self):
        for frame in [self.frame2, self.frame3,self.frame4,self.frame5]:
            for widget in frame.winfo_children():
                widget.destroy()
            frame.pack_forget()

        global tcgpa,ttotalcredit
        tcgpa = 0
        ttotalcredit = 0
        self.sltnumc.set("0")
        self.cvars = []
        self.cdtvars = []
        self.initialfile()

        self.started()
    
    def initialfile(self):
        try:
            with open('GPAfile//gpa.txt','w') as f:
                f.write()
        except Exception as e:
            print(f"Error Opening File:{e}")
    
    def ns(self):
        for frame in [self.frame2,self.frame3,self.frame4,self.frame5]:
            for widget in frame.winfo_children():
                widget.destroy()
            frame.pack_forget()    
        self.cvars = []
        self.cdtvars = []
        self.started()
        
    def history(self):
        for frame in [self.frame2,self.frame3,self.frame4,self.frame5]:
            for widget in frame.winfo_children():
                widget.destroy()    
            frame.pack_forget()  
        
        self.frametop = Frame(self.newwindow)
        self.frametop.pack()
        lbl = Label(self.frametop,text="History",font=("Times New Roman",36,"bold"),anchor="n").grid(row=1,column=1,padx=50)
        self.framebody = Frame(self.newwindow)
        self.framebody.pack()
        btnback = Button(self.frametop,text=" Back ",bg="lightblue",activebackground="lightgrey",relief="ridge",bd=1,font=("Arial",15,"bold"),cursor="hand2",anchor="center",command=self.back).grid(row=1,column=2,padx=50)
        filename = "gpa.txt"
        records = self.gpafile(filename)

        rownum = 0
        for idx, record in enumerate(records,start=1):
            print(f"Sem{idx}")
            print(record["gpa"])
            print(record["credit"])
            print(record["cgpa"])
            print(record["totalcredit"])
            semlbl = Label(self.framebody,text=f"Semester {idx}",font=("Times New Roman",20,"bold"),anchor="w").grid(row=rownum,column=1,pady=20)
            hshowgpa = Label(self.framebody,text=f"{record['gpa']}",font=("Times New Roman",30,"bold")).grid(row=rownum+1,column=1,padx=20)
            hshowgpaw = Label(self.framebody,text=" GPA ",font=("Times New Roman",14,"bold")).grid(row=rownum+2,column=1,padx=20)
            hshowcdt = Label(self.framebody,text=f"{record['credit']}",font=("Times New Roman",30,"bold")).grid(row=rownum+3,column=1,padx=20)
            hshowcdtw = Label(self.framebody,text=" Credit Hours Earned ",font=("Times New Roman",14,"bold")).grid(row=rownum+4,column=1,padx=20)
            hshowcgpa = Label(self.framebody,text=f"{record['cgpa']}",font=("Times New Roman",30,"bold")).grid(row=rownum+1,column=2,padx=20)
            hshowcgpaw = Label(self.framebody,text=" CGPA ",font=("Times New Roman",14,"bold")).grid(row=rownum+2,column=2,padx=20)
            hshowtcdt = Label(self.framebody,text=f"{record['totalcredit']}",font=("Times New Roman",30,"bold")).grid(row=rownum+3,column=2,padx=20)
            hshowtcdtw = Label(self.framebody,text=" Total Credit Hours Earned ",font=("Times New Roman",14,"bold")).grid(row=rownum+4,column=2,padx=20)
            rownum += 5


    def back(self):
        for frame in [self.frametop,self.framebody]:
            for widget in frame.winfo_children():
                widget.destroy()
            frame.pack_forget()

        self.started()

    def gpafile(self,filename):
        try:
            with open('GPAfile//gpa.txt','r') as f:
                lines = f.readlines() 

            records = []
            for i in range(0,len(lines),4):
                if i+3 < len(lines):
                    fgpa = lines[i].strip()
                    fcdt = lines[i+1].strip()
                    fcgpa = lines[i+2].strip()
                    ftcdt = lines[i+3].strip()
                    print(fgpa,fcdt,fcgpa,ftcdt)

                    record = {"gpa":fgpa,"credit":fcdt,"cgpa":fcgpa,"totalcredit":ftcdt}
                    records.append(record)

            return records
        
        except Exception as e:
            print(f"Error Opening File:{e}")



# newwindow = Tk()
# newwindow.geometry("1000x800")
# newwindow.resizable(True,True)
# newwindow.title("CGPA Calculator")

tcgpa=0
ttotalcredit=0

# cgpa()
