from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os


class face_recognise:
    # def __init__(self, root):
    #     self.root = root
    #     self.root.geometry("1530x800+0+0")   # width, height, x and y axis
    #     self.root.title("Face Recognition System")

        
    #     img = Image.open(r"/Users/shruti/Desktop/sanjana/face_recognition_project/images/face.jpg")
    #     img = img.resize((1500, 800))
    #     blurred_img = img.filter(ImageFilter.GaussianBlur(radius=1))
    #     self.photoimg = ImageTk.PhotoImage(blurred_img)

    #     l1 = Label(self.root, image=self.photoimg)
    #     l1.place(x=0, y=60, width=1500, height=750)

    #     title_l1 = Label(self.root,text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white",fg="black")
    #     title_l1.place(x=0,y=0,width=1500,height=60)

    #     b1 = Button(l1, text="FACE DETECTOR", cursor="hand",font=("times new roman",30),bg="red", fg="black")
    #     b1.place(x=200, y=300, width=300, height=70)

    # Attendance
    def mark_attendance(self,i,n,d):
        file_path = "Attendance.csv"
        if not os.path.isfile(file_path):
             with open(file_path,"w",newline="\n") as f:
                f.write("Employee ID,Name,Department,Time,Date,Status\n")

        with open(file_path,"r+",newline="\n") as f:
             myData=f.readlines()
             namelist=[]
             for line in myData:
                entry=line.split((","))
                namelist.append(entry[0])
             if (i not in namelist):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y") 
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")
                
    # Face Recognition 
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image, scaleFactor,minNeighbors)
                
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-(predict/300)))

                conn=mysql.connector.connect(host="localhost",username="me",password="employee@123",database="employee_details")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT Employee_ID, Name, Department FROM employee WHERE Employee_ID = %s", (str(id),))
                result = my_cursor.fetchone()
                conn.close()
                # my_cursor.execute("select Employee_ID from employee where Employee_ID = %s"+str(id))
                # i=my_cursor.fetchone()
                # i="+".join(i)

                # my_cursor.execute("select Name from employee where Employee_ID = %s"+str(id))
                # n=my_cursor.fetchone()
                # n="+".join(n)

                # my_cursor.execute("select Department from employee where Employee_ID = %s"+str(id))
                # d=my_cursor.fetchone()
                # d="+".join(d)
                
                if result:
                    i, n, d = result
                    if confidence > 86:
                        cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(i,n,d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord=[x,y,w,h]    
            return coord                 
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("/Users/shruti/Desktop/flask_python/haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    recogniser = face_recognise()
    recogniser.face_recog()