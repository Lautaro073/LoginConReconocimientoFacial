
import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
import os
from tkinter import *
from PIL import Image, ImageTk
import imutils
import math

# Function Log
def Log():
    print("hola")

# Function Sing
def Sign():
    print("chau")

# Path
OutFolderPathUser= 'C:/Users/El Yisus Pai/Desktop/LAB IV/Unidad 4/punto 4/FaceRecognitionAntoSpoofing/Database/Users'
athUserCheck= 'C:/Users/El Yisus Pai/Desktop/LAB IV/Unidad 4/punto 4/FaceRecognitionAntoSpoofing/Database/Users'
OutFolderPathFace= 'C:/Users/El Yisus Pai/Desktop/LAB IV/Unidad 4/punto 4/FaceRecognitionAntoSpoofing/Database/Faces'

# Info List
info = []

# Ventana Principal

pantalla = Tk()
pantalla.title("FACE RECOGNITION SYSTEM")
pantalla.geometry("1280x720")

# Fondo
imagenF = PhotoImage(file="C:/Users/El Yisus Pai/Desktop/LAB IV/Unidad 4/punto 4/FaceRecognitionAntoSpoofing/SetUp/Inicio.png")
background = Label(image = imagenF, text="Inicio")
background.place(x=0, y=0, relheight=1, relwidth=1)

# Input Text Log
# Name
inputNameReg = Entry(pantalla)
inputNameReg.place(x=100, y=320)

# User
inputUserReg = Entry(pantalla)
inputUserReg.place(x=100, y=430)

# Pass
inputPassReg = Entry(pantalla)
inputPassReg.place(x=100, y=540)


# Input Text Sign Up
# User
InputUserLog = Entry(pantalla)
InputUserLog.place(x=750, y=380)
# Pass
InputPassLog = Entry(pantalla)
InputPassLog.place(x=750, y=500)

# Button
# Log
imagenBR = PhotoImage(file="C:/Users/El Yisus Pai/Desktop/LAB IV/Unidad 4/punto 4/FaceRecognitionAntoSpoofing/SetUp/BtLogin.png")
BtReg = Button(pantalla, text="Registro", image=imagenBR, height="40", width="200", command=Log)
BtReg.place(x=300, y=580)

# Sig
imagenBL = PhotoImage(file="C:/Users/El Yisus Pai/Desktop/LAB IV/Unidad 4/punto 4/FaceRecognitionAntoSpoofing/SetUp/BtSign.png")
BtSign = Button(pantalla, text="Registro", image=imagenBL, height="40", width="200", command=Sign)
BtSign.place(x=900, y=580)




pantalla.mainloop()


