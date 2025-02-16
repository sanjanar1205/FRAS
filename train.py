from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Trainer:
    # def __init__(self, root):
    #     self.root = root
    #     self.root.geometry("1530x800+0+0")
    #     self.root.title("Face Recognition System")

    #     img = Image.open(r"/Users/shruti/Downloads/2.jpeg")
    #     img = img.resize((1500, 800))
    #     blurred_img = img.filter(ImageFilter.GaussianBlur(radius=1))
    #     self.photoimg = ImageTk.PhotoImage(blurred_img)

    #     l1 = Label(self.root, image=self.photoimg)
    #     l1.place(x=0, y=0, width=1500, height=800)

        # title_l1 = Label(l1,text="TRAIN", font=("times new roman",30,"bold"),bg="white",fg="black")
        # title_l1.place(x=0,y=340,width=140,height=50)

        # b1_1 = Button(l1, text="TRAIN DATA", command=self.train_classifier, cursor="hand",font=("times new roman",30),fg="black")
        # b1_1.place(x=540, y=340, width=350, height=70)


    # Train Data
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  # os is used to access the path or dir

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Converted into Grayscale image
            image_np=np.array(img,'uint8')   # Numpy is used to convert image into grid image and uint8 is a datatype
            id=int(os.path.split(image)[1].split('.')[1])   

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training",image_np)
            if cv2.waitKey(1)==13:
                break
        ids=np.array(ids)

        # Train The Classifier And Save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")   # Save the trained model to a file
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed")
    


if __name__ == "__main__":
    trainer = Trainer()
    trainer.train_classifier()