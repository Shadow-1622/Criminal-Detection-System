from tkinter import * 
import tkinter as tk
from tkinter import filedialog
import numpy as np
import face_recognition as fr
import cv2


from PIL import Image,ImageTk

window = tk.Toplevel()
window.geometry("300x400")
window.title("Welcome to LikeGeeks app")



def facere():

    
    video_capture = cv2.VideoCapture(0)
    
    #Load a sample picture and learn how to recognize it
    
    Mohanty_image = fr.load_image_file("Mohanty.jpg")
    Mohanty_face_encoding = fr.face_encodings(Mohanty_image)[0]
    
    Aditya_image = fr.load_image_file("Aditya.jpg")
    Aditya_face_encoding = fr.face_encodings(Aditya_image)[0]
    
    

    
    
    known_face_encondings = [Mohanty_face_encoding, Aditya_face_encoding]
    known_face_names = ["Mohanty","Aditya"]
    
    while True: 
        ret, frame = video_capture.read()
    
        rgb_frame = frame[:, :, ::-1]
    
        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)
    
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    
            matches = fr.compare_faces(known_face_encondings, face_encoding)
    
            name = "Unknown"
    
            face_distances = fr.face_distance(known_face_encondings, face_encoding)
    
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
            cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
        cv2.imshow('Webcam_facerecognition', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()
    

def gunre():
    watch_cascade=cv2.CascadeClassifier('C:/Users/Aditya/Downloads/Face-Recognition-For-Security-System--main/src/classifier/cascade.xml')
    
    #cap=cv2.VideoCapture(0)
    cap=cv2.VideoCapture('Guns Slideshow.mp4')
    while True:
        ret,img=cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        watch = watch_cascade.detectMultiScale(gray,1.3,3)
        for(x,y,w,h) in watch:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=img[y:y+h,x:x+w]
    
     
        cv2.imshow('img',img)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
        
        if True:
            messagebox.showwarning(title=None, message="Gun Detected Alert")
            break
    cap.release()
    cv2.destroyAllWindows()
    


label2 = Label(window, text= "Criminal Activities",font=("Arial",25)).pack()

button1 = Button(window, text= "Criminal Face Recognition", padx= 100, pady= 20, fg="white", bg="black",command=facere).pack()
label1 = Label(window, text=" ").pack()
button2 = Button(window, text= "Gun Detection", padx= 100, pady= 20, fg="white", bg="black", command=gunre).pack()





window.mainloop()

    
