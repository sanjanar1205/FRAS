from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")       #width, height, x and y axis
        self.root.title("Face Recognition System")
        
        #Image one
        # img = Image.open(r"/Users/shruti/Desktop/sanjana/face_recognition_project/images/i2.jpeg")
        # img = img.resize((1500, 800))
        # self.photoimg = ImageTk.PhotoImage(img)

        # l1 = Label(self.root, image=self.photoimg)
        # l1.place(x=0, y=0, width=1500, height=800)
        root['background']='white'

        # self.var_atten_id=StringVar()
        self.var_atten_empid=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_search = StringVar()


        title_l1 = Label(self.root,text="ATTENDANCE DETAILS", font=("times new roman",30,"bold"),bg="white",fg="black")
        title_l1.place(x=0,y=10,width=1450,height=40)

        main_frame = Frame(self.root,bd=2,bg="black")   # bd = border
        main_frame.place(x=20,y=70,width=1400,height=800)

        #Left Label Frame
        Left_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Attendance Details",font=("times new roman",12,"bold"),bg="black", fg="white")
        Left_Frame.place(x=10,y=5,width=680,height=700)
        
        img_left = Image.open(r"/Users/shruti/Downloads/e.jpeg")
        img_left = img_left.resize((660, 200))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_label = Label(self.root, image=self.photoimg_left)
        left_label.place(x=45, y=100, width=660, height=200)


        emp_details_frame=LabelFrame(Left_Frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"), bg="black")
        emp_details_frame.place(x=8,y=220,width=660,height=500)

        # ID_label=Label(emp_details_frame,text="Attendance ID: ",font=("times new roman",16,"bold"), bg="black",fg="white")
        # ID_label.grid(row=0,column=0,pady=10,padx=10,sticky=W)

        # ID_entry=ttk.Entry(emp_details_frame,textvariable=self.var_atten_id,width=24,font=("times new roman",12,"bold"))
        # ID_entry.grid(row=0,column=1,pady=10,padx=10,sticky=W)
        
        name_label=Label(emp_details_frame,text="Employee Name: ",font=("times new roman",16,"bold"),bg="black",fg="white")
        name_label.grid(row=1,column=0,pady=10,padx=10,sticky=W)

        name_entry=ttk.Entry(emp_details_frame,textvariable=self.var_atten_name,width=24,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,pady=10,padx=10,sticky=W)
        
        time_label=Label(emp_details_frame,text="Time: ",font=("times new roman",16,"bold"),bg="black",fg="white")
        time_label.grid(row=4,column=0,pady=10,padx=10,sticky=W)

        time_entry=ttk.Entry(emp_details_frame,textvariable=self.var_atten_time,width=24,font=("times new roman",12,"bold"))
        time_entry.grid(row=4,column=1,pady=10,padx=10,sticky=W)
        
        EmpID_label=Label(emp_details_frame,text="Employee ID: ",font=("times new roman",16,"bold"),bg="black",fg="white")
        EmpID_label.grid(row=0,column=0,pady=10,padx=10,sticky=W)

        EmpID_entry=ttk.Entry(emp_details_frame,textvariable=self.var_atten_empid,width=24,font=("times new roman",12,"bold"))
        EmpID_entry.grid(row=0,column=1,pady=10,padx=10,sticky=W)
        
        Department_label=Label(emp_details_frame,text="Department: ",font=("times new roman",16,"bold"),bg="black",fg="white")
        Department_label.grid(row=3,column=0,pady=10,padx=10,sticky=W)

        Department_entry=ttk.Entry(emp_details_frame,textvariable=self.var_atten_dep,width=24,font=("times new roman",12,"bold"))
        Department_entry.grid(row=3,column=1,pady=10,padx=10,sticky=W)
        
        Date_label=Label(emp_details_frame,text="Date: ",font=("times new roman",16,"bold"),bg="black",fg="white")
        Date_label.grid(row=5,column=0,pady=10,padx=10,sticky=W)

        Date_entry=ttk.Entry(emp_details_frame,textvariable=self.var_atten_date,width=24,font=("times new roman",12,"bold"))
        Date_entry.grid(row=5,column=1,pady=10,padx=10,sticky=W)

        status_label=Label(emp_details_frame,text="Attendance Status",font=("times new roman",15,"bold"),bg="black",fg="white")
        status_label.grid(row=6,column=0,padx=10)
        
        status_combo=ttk.Combobox(emp_details_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),width=30,state="readonly")
        status_combo["values"]=("Status","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=6,column=1,padx=2,pady=10)
        
        #Buttons
        buttons_frame=LabelFrame(emp_details_frame,bd=2,relief=RIDGE, bg="black")
        buttons_frame.place(x=0,y=380,width=655,height=50)

        save_btn=Button(buttons_frame,text="Import CSV",command=self.importCsv,width=18,font=("times new roman",13,"bold"))
        save_btn.grid(row=3,column=0,pady=10)

        update_btn=Button(buttons_frame,text="Export CSV",command=self.exportCsv,width=18,font=("times new roman",13,"bold"))
        update_btn.grid(row=3,column=1,pady=10)

        delete_btn=Button(buttons_frame,text="Update",width=18,font=("times new roman",13,"bold"))
        delete_btn.grid(row=3,column=2,pady=10)

        reset_btn=Button(buttons_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"))
        reset_btn.grid(row=3,column=3,pady=10)


        #Right Label Frame
        Right_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),bg="black", fg="white")
        Right_Frame.place(x=700,y=10,width=680,height=700)

        # Search Frame
        search_frame = LabelFrame(Right_Frame, bd=2, relief=RIDGE, text="Search Attendance", font=("times new roman", 12, "bold"), bg="black", fg="white")
        search_frame.place(x=10, y=10, width=655, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="black", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", command=self.search_data, width=12, font=("times new roman", 13, "bold"))
        search_btn.grid(row=0, column=2, padx=10)

        #Table Frame
        table_frame = LabelFrame(Right_Frame, bd=2, relief=RIDGE)
        table_frame.place(x=10, y=90, width=655, height=600)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("EmpID","Name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # self.AttendanceReportTable.heading("ID",text="Attendance ID")
        self.AttendanceReportTable.heading("EmpID",text="Employee ID")
        self.AttendanceReportTable.heading("Name",text="Employee Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        # self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("EmpID",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        # self.fetchData([])

    # Fetch Data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(* self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File","*csv"),("ALL File","*.*")],parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File","*csv"),("ALL File","*.*")],parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfully")
        except Exception as e:
            messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)

    
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        # self.var_atten_id.set(rows[0])
        self.var_atten_empid.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_date.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_attendance.set(rows[5])

    def reset_data(self):
        # self.var_atten_id.set("")
        self.var_atten_empid.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")
    
    # Search data
    def search_data(self):
        query = self.var_search.get().lower()
        filtered_data = [row for row in mydata if query in row[0].lower() or query in row[1].lower()]
        self.fetchData(filtered_data)

    


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()