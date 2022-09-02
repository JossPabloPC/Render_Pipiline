# Import required Libraries
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2

from Coordinates import *
from Camera import Camera

#Constantes
Up          =  Vector3(0, 1, 0)
Right       =  Vector3(1, 0, 0)
Forward     =  Vector3(0, 0, 1)
Backward    =  Vector3(0, 0, -1)

width = 800
ratio = 0.75
height = width * ratio

arr = np.zeros((width,int(height),3), np.uint8)

#Functions
def array2Window(arr):
      img = Image.fromarray(arr)

      # Convert image to PhotoImage
      imgtk             = ImageTk.PhotoImage(image = img)
      output_image      = tk.Label(image=imgtk)
      output_image.image= imgtk
      output_image.pack()

def printVector(entryX, entryY, entryZ):
      x = entryX.get()
      y = entryY.get()
      z = entryZ.get()
      vectorA = Vector3(float(x), float(y), float(z))
      vectorA.normalizar_vector()
      label = tk.Label(text= "X: " + str(vectorA.x) + " Y: " + str(vectorA.y) + " Z: " + str(vectorA.z) + " Magnitud: " + str(vectorA.magnitud) )
      label.pack()

def _3D_2_2D(camaraPos, pointPos):
      W = Backward
      U = Right
      V = Up

      camara = Camera(W, U, V,camaraPos, width,height,8, 1, 2)

      camara.setMatrizcambio()
      camara.setViewMatrix()

      punto_camara = camara.get_coordenadas_respecto_camara(pointPos)

      punto_plano_cercano = camara.get_coordenadas_plano_cercano(punto_camara)

      punto_pantalla = camara.get_coordenadas_pantalla(punto_plano_cercano)

      print(punto_pantalla)
      
      arr[punto_pantalla] = (255,255,255)
      img = Image.fromarray(arr)
      imgtk             = ImageTk.PhotoImage(image = img)
      output_image      = tk.Label(image=imgtk)
      output_image.image= imgtk
      output_image.pack()



# Create an instance of TKinter Window or frame
win= tk.Tk()
win.geometry("850x480")# Create a Label to capture the Video frames

# Output image
cap= np.zeros((300,300,3), dtype=np.uint8)

#Frames
coordenadas = tk.Frame()

#--WIDGETS--
greeting    = tk.Label(text="Welcome to Python Render Pipeline", fg="white", bg="black",width=50, height=3)
cameraLbl   = tk.Label(text="Camera coordinates", master=coordenadas)
pointLbl    = tk.Label(text="Point coordinates", master=coordenadas)
#Camara
Camera_X_entry = tk.Entry(master=coordenadas)
Camera_Y_entry = tk.Entry(master=coordenadas)
Camera_Z_entry = tk.Entry(master=coordenadas)

Point_X_entry = tk.Entry(master=coordenadas)
Point_Y_entry = tk.Entry(master=coordenadas)
Point_Z_entry = tk.Entry(master=coordenadas)

Camera_X_entry.insert(0,"1")
Camera_Y_entry.insert(0,"2")
Camera_Z_entry.insert(0,"3")

Point_X_entry.insert(0,"0")
Point_Y_entry.insert(0,"2")
Point_Z_entry.insert(0,"0")


#Punto
run_btn     = tk.Button(command=lambda: _3D_2_2D(Vector3(int(Camera_X_entry.get()), int(Camera_Y_entry.get()), int(Camera_Z_entry.get())),
                                                Vector3(float(Point_X_entry.get()), float(Point_Y_entry.get()), float(Point_Z_entry.get()))
                                                ) , text= "Run")
#Packing
greeting.pack()
cameraLbl.pack()
Camera_X_entry.pack()
Camera_Y_entry.pack()
Camera_Z_entry.pack()
pointLbl.pack()
Point_X_entry.pack()
Point_Y_entry.pack()
Point_Z_entry.pack()
coordenadas.pack()
run_btn.pack()

win.mainloop()