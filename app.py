# Import required Libraries
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2

from Coordinates import *
from Camera import Camera
from Triangle import Triangle

#Constantes
Up          =  Vector3(0, 1, 0)
Right       =  Vector3(1, 0, 0)
Forward     =  Vector3(0, 0, 1)
Backward    =  Vector3(0, 0, -1)

width = 800
ratio = 0.75
height = width * ratio

arr = np.zeros((int(height), width, 3), np.uint8)

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

      camara = Camera(W, U, V,camaraPos, height,width,8, 1, 2)

      camara.setMatrizcambio()
      camara.setViewMatrix()

      punto_camara = camara.get_coordenadas_respecto_camara(pointPos)

      punto_plano_cercano = camara.get_coordenadas_plano_cercano(punto_camara)

      punto_pantalla = camara.get_coordenadas_pantalla(punto_plano_cercano)

      print(punto_pantalla[1], punto_pantalla[0])
      arr[punto_pantalla] = (255,255,255)
      arr[0,0] = (0,255,0)
      cv2.imshow("Result",arr)
      return punto_pantalla[1], punto_pantalla[0], punto_plano_cercano[2][0]
      
def createTriangle(camaraPos, pointPos1, pointPos2, pointPos3):
      p1= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos1)
      p2= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos2)
      p3= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos3)

      print("")
      print("P1:", p1, "P2:", p2, "P3:", p3, )

      triangle = Triangle(p1, p2, p3, arr)
      triangle.trazar_linea(p1, p2, arr)
      triangle.trazar_linea(p2, p3, arr)
      triangle.trazar_linea(p3, p1, arr)
      cv2.imshow("Result",arr)



# Create an instance of TKinter Window or frame
win= tk.Tk()
win.geometry("850x480")# Create a Label to capture the Video frames

#Frames
coordenadas = tk.Frame()

#--WIDGETS--
greeting    = tk.Label(text="Welcome to Python Render Pipeline", fg="white", bg="black",width=50, height=3)
cameraLbl   = tk.Label(text="Camera coordinates", master=coordenadas)
point_1_Lbl    = tk.Label(text="Point 1 coordinates", master=coordenadas)
point_2_Lbl    = tk.Label(text="Point 2 coordinates", master=coordenadas)
point_3_Lbl    = tk.Label(text="Point 3 coordinates", master=coordenadas)
#Camara
Camera_X_entry = tk.Entry(master=coordenadas)
Camera_Y_entry = tk.Entry(master=coordenadas)
Camera_Z_entry = tk.Entry(master=coordenadas)

Point_1_X_entry = tk.Entry(master=coordenadas)
Point_1_Y_entry = tk.Entry(master=coordenadas)
Point_1_Z_entry = tk.Entry(master=coordenadas)

Point_2_X_entry = tk.Entry(master=coordenadas)
Point_2_Y_entry = tk.Entry(master=coordenadas)
Point_2_Z_entry = tk.Entry(master=coordenadas)

Point_3_X_entry = tk.Entry(master=coordenadas)
Point_3_Y_entry = tk.Entry(master=coordenadas)
Point_3_Z_entry = tk.Entry(master=coordenadas)


Camera_X_entry.insert(0,"0")
Camera_Y_entry.insert(0,"0")
Camera_Z_entry.insert(0,"0")

Point_1_X_entry.insert(0,"0")
Point_1_Y_entry.insert(0,"0")
Point_1_Z_entry.insert(0,"10")


Point_2_X_entry.insert(0,"0")
Point_2_Y_entry.insert(0,"4")
Point_2_Z_entry.insert(0,"10")


Point_3_X_entry.insert(0,"5")
Point_3_Y_entry.insert(0,"0")
Point_3_Z_entry.insert(0,"10")


#Punto
run_btn     = tk.Button(command=lambda: createTriangle(Vector3(int(Camera_X_entry.get()), int(Camera_Y_entry.get()), int(Camera_Z_entry.get())),
                                                Vector3(float(Point_1_X_entry.get()), float(Point_1_Y_entry.get()), float(Point_1_Z_entry.get())),
                                                Vector3(float(Point_2_X_entry.get()), float(Point_2_Y_entry.get()), float(Point_2_Z_entry.get())),
                                                Vector3(float(Point_3_X_entry.get()), float(Point_3_Y_entry.get()), float(Point_3_Z_entry.get())),
                                                ) , text= "Run")
#Packing
greeting.pack()
cameraLbl.pack()

Camera_X_entry.pack()
Camera_Y_entry.pack()
Camera_Z_entry.pack()

point_1_Lbl.pack()

Point_1_X_entry.pack()
Point_1_Y_entry.pack()
Point_1_Z_entry.pack()

point_2_Lbl.pack()
Point_2_X_entry.pack()
Point_2_Y_entry.pack()
Point_2_Z_entry.pack()

point_3_Lbl.pack()
Point_3_X_entry.pack()
Point_3_Y_entry.pack()
Point_3_Z_entry.pack()

coordenadas.pack()

run_btn.pack()

win.mainloop()