
import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
import os
from tkinter import *
from PIL import Image, ImageTk
import imutils
import math

# Log Biometric Function
def Log_Biometric():
    global pantalla2, conteo, parpadeo, img_info, step, cap, lblVideo

    # Check Cap
    if cap is not None:
        ret, frame = cap.read()

        # Resize
        frame = imutils.resize(frame, width=1280, height=720)

        # Frame Show
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Conv Video
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        # Show Video
        lblVideo.configure(image = img)
        lblVideo.image = img
        lblVideo.after(10, Log_Biometric)

    else:
        cap.release()



# Function Log
def Log():
   global RegName, RegUser, RegPass, InputNameReg, InputUserReg, InputPassReg, cap, lblVideo, pantalla2
   # Extract: Name - User - Pass
   RegName = InputNameReg.get()
   RegUser = InputUserReg.get()
   RegPass = InputPassReg.get()

   # Incomplete Form
   if len(RegName) == 0 or len(RegUser) == 0 or len(RegPass) == 0:
       # Print Error
    print(" FORMULARIO INCOMPLETO ")
   # Complete Form
   else:
       # Check Users
       UserList = os.listdir(PathUserCheck)

       # Name Users
       UserName = []

       # Check User List
       for lis in UserList:
           # Extraer User
           User = lis
           User = User.split('.')
           # Save User
           UserName.append(User[0])


        # Check User
       if RegUser in UserName:
           # Registrado
           print(" USUARIO REGISTRADO ANTERIORMENTE ")

       else:
           # No Registrado
           # Save Info
           info.append(RegName)
           info.append(RegUser)
           info.append(RegPass)

           # Export Info
           f = open(f"{OutFolderPathUser}/{RegUser}.txt", "w")
           f.write(RegName + ",")
           f.write(RegUser + ",")
           f.write(RegPass)
           f.close()

           # Clean
           InputNameReg.delete(0, END)
           InputUserReg.delete(0, END)
           InputPassReg.delete(0, END)

           # New Screen
           pantalla2 = Toplevel(pantalla)
           pantalla2.title("LOGIN BIOMETRIC")
           pantalla2.geometry("1280x720")

           # Label Video
           lblVideo = Label(pantalla2)
           lblVideo.place(x=0, y=0)

           # VideoCaptura
           cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
           cap.set(3, 1280)
           cap.set(4, 720)
           Log_Biometric()







# Function Sing
def Sign():
    print("chau")

# Path
OutFolderPathUser= './Database/Users'
PathUserCheck= './Database/Users'
OutFolderPathFace= './Database/Faces'


# Variables


# Info List
info = []

# Ventana Principal

pantalla = Tk()
pantalla.title("FACE RECOGNITION SYSTEM")
pantalla.geometry("1280x720")

# Fondo
imagenF = PhotoImage(file="./SetUp/Inicio.png")
background = Label(image = imagenF, text="Inicio")
background.place(x=0, y=0, relheight=1, relwidth=1)

# Input Text Log
# Name
InputNameReg = Entry(pantalla)
InputNameReg.place(x=100, y=320)

# User
InputUserReg = Entry(pantalla)
InputUserReg.place(x=100, y=430)

# Pass
InputPassReg = Entry(pantalla)
InputPassReg.place(x=100, y=540)


# Input Text Sign Up
# User
InputUserLog = Entry(pantalla)
InputUserLog.place(x=750, y=380)
# Pass
InputPassLog = Entry(pantalla)
InputPassLog.place(x=750, y=500)

# Button
# Log
imagenBR = PhotoImage(file="./SetUp/BtLogin.png")
BtReg = Button(pantalla, text="Registro", image=imagenBR, height="40", width="200", command=Log)
BtReg.place(x=300, y=580)

# Sig
imagenBL = PhotoImage(file="./SetUp/BtSign.png")
BtSign = Button(pantalla, text="Registro", image=imagenBL, height="40", width="200", command=Sign)
BtSign.place(x=900, y=580)




pantalla.mainloop()


