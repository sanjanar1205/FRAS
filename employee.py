from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")       #width, height, x and y axis
        self.root.title("Face Recognition System")


        #Text Variables for entry fill
        self.var_dep = StringVar()
        self.var_Year = StringVar()
        self.var_EmpID = StringVar()
        self.var_Name = StringVar()
        self.var_Gen = StringVar()
        self.var_DOB = StringVar()
        self.var_Email = StringVar()
        self.var_PhNo = StringVar()
        self.var_Address = StringVar()
        self.var_Job_Title = StringVar()
        self.var_DOJ = StringVar()
        self.var_Manager = StringVar()
        self.var_radiobtn1 = StringVar()
        self.var_search_by = StringVar()  
        self.var_search_txt = StringVar()


        #Image one
        img = Image.open(r"/Users/shruti/Downloads/i1.jpeg")
        img = img.resize((1500, 800))
        self.photoimg = ImageTk.PhotoImage(img)

        l1 = Label(self.root, image=self.photoimg)
        l1.place(x=0, y=0, width=1500, height=800)

        title_l1 = Label(l1,text="EMPLOYEE DETAILS", font=("times new roman",30,"bold"),bg="white",fg="black")
        title_l1.place(x=0,y=10,width=1450,height=40)

        main_frame = Frame(l1,bd=2,bg="black")   # bd = border
        main_frame.place(x=20,y=70,width=1400,height=800)

        #Left Label Frame
        Left_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Left_Frame.place(x=10,y=10,width=680,height=700)

        img_left = Image.open(r"/Users/shruti/Downloads/e.jpeg")
        img_left = img_left.resize((660, 200))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_label = Label(self.root, image=self.photoimg_left)
        left_label.place(x=45, y=100, width=660, height=200)


        #Right Label Frame
        Right_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=700,y=10,width=680,height=700)

        #Information
        info_frame=LabelFrame(Left_Frame,bd=2,relief=RIDGE,text="Informaion",font=("times new roman",12,"bold"))
        info_frame.place(x=13,y=210,width=652,height=70)
        #Department
        dep_label=Label(info_frame,text="Department",font=("times new roman",15,"bold"))
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(info_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=30,state="readonly")
        dep_combo["values"]=("Select Department","Operation","Marketing","Cloud","Sales and Customer Success","Product and Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        #Year
        year_label=Label(info_frame,text="Year",font=("times new roman",15,"bold"))
        year_label.grid(row=0,column=2,padx=10)

        year_combo=ttk.Combobox(info_frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),width=30,state="readonly")
        year_combo["values"]=("Select Year","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10)

        #Employee Information 
        emp_frame=LabelFrame(Left_Frame,bd=2,relief=RIDGE,text="Employee Information",font=("times new roman",12,"bold"))
        emp_frame.place(x=13,y=290,width=652,height=300)

        ID_label=Label(emp_frame,text="Employee ID: ",font=("times new roman",16,"bold"))
        ID_label.grid(row=0,column=0,pady=10,padx=10,sticky=W)

        ID_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_EmpID,font=("times new roman",12,"bold"))
        ID_entry.grid(row=0,column=1,pady=10,padx=10,sticky=W)

        name_label=Label(emp_frame,text="Employee Name: ",font=("times new roman",16,"bold"))
        name_label.grid(row=0,column=2,pady=10,padx=10,sticky=W)

        name_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_Name,font=("times new roman",12,"bold"))
        name_entry.grid(row=0,column=3,pady=10,padx=10,sticky=W)

        gender_label=Label(emp_frame,text="Gender: ",font=("times new roman",16,"bold"))
        gender_label.grid(row=1,column=0,pady=10,padx=10,sticky=W)

        # gender_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_Gen,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=1,column=1,pady=10,padx=10,sticky=W)
        gender_combo=ttk.Combobox(emp_frame,textvariable=self.var_Gen,font=("times new roman",12,"bold"),width=22,state="readonly")
        gender_combo["values"]=("Select Gender","Female","Male","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=10)

        dob_label=Label(emp_frame,text="Date Of Birth: ",font=("times new roman",16,"bold"))
        dob_label.grid(row=1,column=2,pady=10,padx=10,sticky=W)

        dob_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_DOB,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=3,pady=10,padx=10,sticky=W)

        email_label=Label(emp_frame,text="Email: ",font=("times new roman",16,"bold"))
        email_label.grid(row=2,column=0,pady=10,padx=10,sticky=W)

        email_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_Email,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,pady=10,padx=10,sticky=W)

        phoneno_label=Label(emp_frame,text="Phone Number: ",font=("times new roman",16,"bold"))
        phoneno_label.grid(row=2,column=2,pady=10,padx=10,sticky=W)

        phoneno_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_PhNo,font=("times new roman",12,"bold"))
        phoneno_entry.grid(row=2,column=3,pady=10,padx=10,sticky=W)

        address_label=Label(emp_frame,text="Address: ",font=("times new roman",16,"bold"))
        address_label.grid(row=3,column=0,pady=10,padx=10,sticky=W)

        address_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_Address,font=("times new roman",12,"bold"))
        address_entry.grid(row=3,column=1,pady=10,padx=10,sticky=W)

        jtitle_label=Label(emp_frame,text="Job Title: ",font=("times new roman",16,"bold"))
        jtitle_label.grid(row=3,column=2,pady=10,padx=10,sticky=W)

        jtitle_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_Job_Title,font=("times new roman",12,"bold"))
        jtitle_entry.grid(row=3,column=3,pady=10,padx=10,sticky=W)

        DOJ_label=Label(emp_frame,text="Date Of Joining: ",font=("times new roman",16,"bold"))
        DOJ_label.grid(row=4,column=0,pady=10,padx=10,sticky=W)

        DOJ_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_DOJ,font=("times new roman",12,"bold"))
        DOJ_entry.grid(row=4,column=1,pady=10,padx=10,sticky=W)

        manager_label=Label(emp_frame,text="Manager: ",font=("times new roman",16,"bold"))
        manager_label.grid(row=4,column=2,pady=10,padx=10,sticky=W)

        manager_entry=ttk.Entry(emp_frame,width=24,textvariable=self.var_Manager,font=("times new roman",12,"bold"))
        manager_entry.grid(row=4,column=3,pady=10,padx=10,sticky=W)

        #radio Buttons
        self.var_radiobtn1=StringVar()
        radiobtn1=ttk.Radiobutton(emp_frame,variable=self.var_radiobtn1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(emp_frame,variable=self.var_radiobtn1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        #Buttons
        buttons_frame=LabelFrame(Left_Frame,bd=2,relief=RIDGE)
        buttons_frame.place(x=13,y=560,width=652,height=50)

        save_btn=Button(buttons_frame,command=self.add_data,text="Save",width=18,font=("times new roman",13,"bold"))
        save_btn.grid(row=0,column=0,pady=10)

        update_btn=Button(buttons_frame,command=self.update_data,text="Update",width=18,font=("times new roman",13,"bold"))
        update_btn.grid(row=0,column=1,pady=10)

        delete_btn=Button(buttons_frame,command=self.delete_data,text="Delete",width=18,font=("times new roman",13,"bold"))
        delete_btn.grid(row=0,column=2,pady=10)

        reset_btn=Button(buttons_frame,command=self.reset_data,text="Reset",width=18,font=("times new roman",13,"bold"))
        reset_btn.grid(row=0,column=3,pady=10)
        

        buttons1_frame=LabelFrame(Left_Frame,bd=2,relief=RIDGE)
        buttons1_frame.place(x=13,y=620,width=652,height=50)

        takesample_btn=Button(buttons1_frame,command=self.generate_data,text="Take Photo Sample",width=41,font=("times new roman",13,"bold"))
        takesample_btn.grid(row=1,column=0,pady=10)

        updatesample_btn=Button(buttons1_frame,text="Update Photo Sample",width=41,font=("times new roman",13,"bold"))
        updatesample_btn.grid(row=1,column=1,pady=10)

        #Search Systen
        search_frame=LabelFrame(Right_Frame,bd=2,relief=RIDGE,text="Search Information",font=("times new roman",12,"bold"))
        search_frame.place(x=13,y=10,width=652,height=80)

        search_label=Label(search_frame,text="SEARCH BY: ",bg="Red",fg="white",font=("times new roman",16,"bold"))
        search_label.grid(row=0,column=0,pady=10,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search_by,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","EmpID","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1)

        search_entry=ttk.Entry(search_frame,textvariable=self.var_search_txt,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,pady=10,sticky=W)


        search_btn=Button(search_frame,command=self.search_data,text="Search",width=14,font=("times new roman",13,"bold"))
        search_btn.grid(row=0,column=3)

        show_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=14,font=("times new roman",13,"bold"))
        show_btn.grid(row=0,column=4)

        #Table Frame
        table_frame=LabelFrame(Right_Frame,bd=2,relief=RIDGE)
        table_frame.place(x=13,y=100,width=652,height=550)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","Year","EmpID","Name","Gen","DOB","Email","PhNo","Address","Job_Title","DOJ","Manager","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("Year",text="Year")
        self.employee_table.heading("EmpID",text="Employee ID")
        self.employee_table.heading("Name",text="Employee Name")
        self.employee_table.heading("Gen",text="Gender")
        self.employee_table.heading("DOB",text="Date Of Birth")
        self.employee_table.heading("Email",text="Email")
        self.employee_table.heading("PhNo",text="Phone Number")
        self.employee_table.heading("Address",text="Address")
        self.employee_table.heading("Job_Title",text="Job Title")
        self.employee_table.heading("DOJ",text="Date Of Joining")
        self.employee_table.heading("Manager",text="Manager")
        self.employee_table.heading("Photo",text="PhotoSampleStatus")
        self.employee_table["show"]="headings"

        self.employee_table.column("dep",width=100)
        self.employee_table.column("Year",width=100)
        self.employee_table.column("EmpID",width=100)
        self.employee_table.column("Name",width=100)
        self.employee_table.column("Gen",width=100)
        self.employee_table.column("DOB",width=100)
        self.employee_table.column("Email",width=100)
        self.employee_table.column("PhNo",width=100)
        self.employee_table.column("Address",width=100)
        self.employee_table.column("Job_Title",width=100)
        self.employee_table.column("DOJ",width=100)
        self.employee_table.column("Manager",width=100)
        self.employee_table.column("Photo",width=150)
        self.employee_table["show"]="headings"

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Fuction Declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_EmpID.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="me",password="employee@123",database="employee_details")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_Year.get(),
                    self.var_EmpID.get(),
                    self.var_Name.get(),
                    self.var_Gen.get(),
                    self.var_DOB.get(),
                    self.var_Email.get(),
                    self.var_PhNo.get(),
                    self.var_Address.get(),
                    self.var_Job_Title.get(),
                    self.var_DOJ.get(),
                    self.var_Manager.get(),
                    self.var_radiobtn1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee details has been added Successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To :{str(e)}",parent=self.root)

        
    
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="me",password="employee@123",database="employee_details")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from employee")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.employee_table.focus()
        content=self.employee_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_Year.set(data[1])
        self.var_EmpID.set(data[2])
        self.var_Name.set(data[3])
        self.var_Gen.set(data[4])
        self.var_DOB.set(data[5])
        self.var_Email.set(data[6])
        self.var_PhNo.set(data[7])
        self.var_Address.set(data[8])
        self.var_Job_Title.set(data[9])
        self.var_DOJ.set(data[10])
        self.var_Manager.set(data[11])
        self.var_radiobtn1.set(data[12])
        
        
    # Update Function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_EmpID.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this employee details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="me",password="employee@123",database="employee_details")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update employee set Department=%s,Year=%s,Name=%s,Gender=%s,DOB=%s,Email=%s,Phone_No=%s,Address=%s,Job_Title=%s,DOJ=%s,Manager=%s,PhotoSample=%s where Employee_ID=%s",(
                            self.var_dep.get(),
                            self.var_Year.get(),
                            self.var_Name.get(),
                            self.var_Gen.get(),
                            self.var_DOB.get(),
                            self.var_Email.get(),
                            self.var_PhNo.get(),
                            self.var_Address.get(),
                            self.var_Job_Title.get(),
                            self.var_DOJ.get(),
                            self.var_Manager.get(),
                            self.var_radiobtn1.get(),
                            self.var_EmpID.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Employee details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)

    # Delete Function
    def delete_data(self):
        if self.var_EmpID.get()=="":
            messagebox.showerror("Error","Employee ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee Delete Page","Do you want to delete this employee",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="me",password="employee@123",database="employee_details")
                    my_cursor=conn.cursor()
                    sql="delete from employee where Employee_ID=%s"
                    val=(self.var_EmpID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showerror("Delete","Successfully deleted employee details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)


    # Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_Year.set("Select Year"),
        self.var_EmpID.set(""),
        self.var_Name.set(""),
        self.var_Gen.set("Select Gender"),
        self.var_DOB.set(""),
        self.var_Email.set(""),
        self.var_PhNo.set(""),
        self.var_Address.set(""),
        self.var_Job_Title.set(""),
        self.var_DOJ.set(""),
        self.var_Manager.set(""),
        self.var_radiobtn1.set("")
    
    # Search Function
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="me", password="employee@123", database="employee_details")
        my_cursor = conn.cursor()

        search_by = self.var_search_by.get()
        search_txt = self.var_search_txt.get()

        if search_by == "EmpID":
            my_cursor.execute("SELECT * FROM employee WHERE Employee_ID LIKE %s", (f"%{search_txt}%",))
        elif search_by == "Name":
            my_cursor.execute("SELECT * FROM employee WHERE Name LIKE %s", (f"%{search_txt}%",))

        data = my_cursor.fetchall()

        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        else:
            messagebox.showinfo("No Result", "No matching data found.", parent=self.root)

        conn.close()


    
    # Generate Dataset
    def generate_data(self):
        if self.var_dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_EmpID.get()=="":
            messagebox.showerror("Error","All Feilds are required",parent=self.root)
        else:
            try:
                # conn=mysql.connector.connect(host="localhost",username="me",password="employee@123",database="employee_details")
                # my_cursor=conn.cursor()
                # my_cursor.execute("select * from employee")
                # myresult=my_cursor.fetchall()
                # id=0
                # for x in myresult:
                #     id+=1
                # my_cursor.execute("Update employee set Department=%s,Year=%s,Name=%s,Gender=%s,DOB=%s,Email=%s,Phone_No=%s,Address=%s,Job_Title=%s,DOJ=%s,Manager=%s,PhotoSample=%s where Employee_ID=%s",(
                #             self.var_dep.get(),
                #             self.var_Year.get(),
                #             self.var_Name.get(),
                #             self.var_Gen.get(),
                #             self.var_DOB.get(),
                #             self.var_Email.get(),
                #             self.var_PhNo.get(),
                #             self.var_Address.get(),
                #             self.var_Job_Title.get(),
                #             self.var_DOJ.get(),
                #             self.var_Manager.get(),
                #             self.var_radiobtn1.get(),
                #             self.var_EmpID.get()
                #         ))
                # conn.commit()
                # self.fetch_data()
                # self.reset_data()
                # conn.commit()
                conn = mysql.connector.connect(host="localhost", username="me", password="employee@123", database="employee_details")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select * from employee where Employee_ID = %s", (self.var_EmpID.get(),))
                myresult = my_cursor.fetchone()
                
                if myresult is None:
                    messagebox.showerror("Error", "Employee ID not found", parent=self.root)
                    return
                
                emp_id = self.var_EmpID.get()
                conn.commit()
                conn.close()
                     
                
                # Load predefined data on face frontal from opencv

                face_classifier=cv2.CascadeClassifier("/Users/shruti/Desktop/sanjana/face_recognition_project/haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3, which specifies how much the image size is reduced at each image scale.
                    # Minimum Neighbour = 5, minimum number of neighbors each potential window should have to retain it as a face.


                    for (x,y,w,h) in faces:    #x and y coordinates, width,height
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped 
                    return None
                
                cap=cv2.VideoCapture(0)    # For opening the camera
                # If you want to open other camera you can write (1)
                # And also can give image path inside VideoCapture() to open a specific image.
                img_id=0  
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                        # Ensure the 'data' directory exists
                        directory = "data"
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        file_path_name = os.path.join(directory, "user." + str(emp_id) + "." + str(img_id) + ".jpg")

                        # file_path_name="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path_name,face)
                        cv2.putText(face,str(img_id),(10, 50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),1)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==3 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed!!!")

            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)

                    



if __name__ == "__main__":
    root = Tk()
    obj = employee(root)
    root.mainloop()