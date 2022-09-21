# Import required Libraries
from tkinter import *
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
ratio = 1
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
      triangle.trazar_triangulo()

      cv2.imshow("Result",arr)

def createCube(camaraPos, pointPos1, pointPos2, pointPos3, pointPos4, pointPos5, pointPos6, pointPos7, pointPos8):
      
      p1= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos1)
      p2= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos2)
      p3= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos3)
      p4= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos4)

      p5= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos5)
      p6= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos6)
      p7= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos7)
      p8= _3D_2_2D(camaraPos= camaraPos, pointPos= pointPos8)

      A = Triangle(p1, p2, p3, arr)
      B = Triangle(p2, p3, p4, arr)
      C = Triangle(p1, p5, p7, arr)
      D = Triangle(p1, p3, p7, arr)
      E = Triangle(p5, p6, p8, arr)
      F = Triangle(p5, p7, p8, arr)
      G = Triangle(p1, p5, p6, arr)
      H = Triangle(p1, p2, p6, arr)
      I = Triangle(p3, p7, p8, arr)
      J = Triangle(p3, p4, p8, arr)
      K = Triangle(p2, p4, p6, arr)
      L = Triangle(p4, p6, p8, arr)
      
      A.trazar_triangulo()
      B.trazar_triangulo()
      C.trazar_triangulo()
      D.trazar_triangulo()
      E.trazar_triangulo()
      F.trazar_triangulo()
      G.trazar_triangulo()
      H.trazar_triangulo()
      I.trazar_triangulo()
      J.trazar_triangulo()
      K.trazar_triangulo()
      L.trazar_triangulo()




# Create an instance of TKinter Window or frame
win= tk.Tk()
win.geometry("850x480")# Create a Label to capture the Video frames

#Frames
coordenadas = tk.Frame()
P1 = tk.Frame()
P2 = tk.Frame()
P3 = tk.Frame()
P4 = tk.Frame()
P5 = tk.Frame()
P6 = tk.Frame()
P7 = tk.Frame()
P8 = tk.Frame()

#--WIDGETS--
greeting    = tk.Label(text="Welcome to Python Render Pipeline", fg="white", bg="black",width=50, height=3)
cameraLbl   = tk.Label(text="Camera coordinates", master=coordenadas)
point_1_Lbl    = tk.Label(text="Point 1 coordinates", master=P1)
point_2_Lbl    = tk.Label(text="Point 2 coordinates", master=P2)
point_3_Lbl    = tk.Label(text="Point 3 coordinates", master=P3)
point_4_Lbl    = tk.Label(text="Point 4 coordinates", master=P4)
point_5_Lbl    = tk.Label(text="Point 5 coordinates", master=P5)
point_6_Lbl    = tk.Label(text="Point 6 coordinates", master=P6)
point_7_Lbl    = tk.Label(text="Point 7 coordinates", master=P7)
point_8_Lbl    = tk.Label(text="Point 8 coordinates", master=P8)
#Camara
Camera_X_entry = tk.Entry(master=coordenadas)
Camera_Y_entry = tk.Entry(master=coordenadas)
Camera_Z_entry = tk.Entry(master=coordenadas)

Point_1_X_entry = tk.Entry(master=P1)
Point_1_Y_entry = tk.Entry(master=P1)
Point_1_Z_entry = tk.Entry(master=P1)

Point_2_X_entry = tk.Entry(master=P2)
Point_2_Y_entry = tk.Entry(master=P2)
Point_2_Z_entry = tk.Entry(master=P2)

Point_3_X_entry = tk.Entry(master=P3)
Point_3_Y_entry = tk.Entry(master=P3)
Point_3_Z_entry = tk.Entry(master=P3)

Point_4_X_entry = tk.Entry(master=P4)
Point_4_Y_entry = tk.Entry(master=P4)
Point_4_Z_entry = tk.Entry(master=P4)

Point_5_X_entry = tk.Entry(master=P5)
Point_5_Y_entry = tk.Entry(master=P5)
Point_5_Z_entry = tk.Entry(master=P5)

Point_6_X_entry = tk.Entry(master=P6)
Point_6_Y_entry = tk.Entry(master=P6)
Point_6_Z_entry = tk.Entry(master=P6)

Point_7_X_entry = tk.Entry(master=P7)
Point_7_Y_entry = tk.Entry(master=P7)
Point_7_Z_entry = tk.Entry(master=P7)

Point_8_X_entry = tk.Entry(master=P8)
Point_8_Y_entry = tk.Entry(master=P8)
Point_8_Z_entry = tk.Entry(master=P8)

Camera_X_entry.insert(0,"0")
Camera_Y_entry.insert(0,"2")
Camera_Z_entry.insert(0,"-5")

Point_1_X_entry.insert(0,"0")
Point_1_Y_entry.insert(0,"1")
Point_1_Z_entry.insert(0,"0")


Point_2_X_entry.insert(0,"1")
Point_2_Y_entry.insert(0,"1")
Point_2_Z_entry.insert(0,"0")


Point_3_X_entry.insert(0,"0")
Point_3_Y_entry.insert(0,"0")
Point_3_Z_entry.insert(0,"0")

Point_4_X_entry.insert(0,"1")
Point_4_Y_entry.insert(0,"0")
Point_4_Z_entry.insert(0,"0")

Point_5_X_entry.insert(0,"0")
Point_5_Y_entry.insert(0,"1")
Point_5_Z_entry.insert(0,"-1")

Point_6_X_entry.insert(0,"1")
Point_6_Y_entry.insert(0,"1")
Point_6_Z_entry.insert(0,"-1")

Point_7_X_entry.insert(0,"0")
Point_7_Y_entry.insert(0,"0")
Point_7_Z_entry.insert(0,"-1")

Point_8_X_entry.insert(0,"1")
Point_8_Y_entry.insert(0,"0")
Point_8_Z_entry.insert(0,"-1")


#Punto
run_btn     = tk.Button(command=lambda: createCube(Vector3(int(Camera_X_entry.get()), int(Camera_Y_entry.get()), int(Camera_Z_entry.get())),
                                                Vector3(float(Point_1_X_entry.get()), float(Point_1_Y_entry.get()), float(Point_1_Z_entry.get())),
                                                Vector3(float(Point_2_X_entry.get()), float(Point_2_Y_entry.get()), float(Point_2_Z_entry.get())),
                                                Vector3(float(Point_3_X_entry.get()), float(Point_3_Y_entry.get()), float(Point_3_Z_entry.get())),
                                                Vector3(float(Point_4_X_entry.get()), float(Point_4_Y_entry.get()), float(Point_4_Z_entry.get())),
                                                Vector3(float(Point_5_X_entry.get()), float(Point_5_Y_entry.get()), float(Point_5_Z_entry.get())),
                                                Vector3(float(Point_6_X_entry.get()), float(Point_6_Y_entry.get()), float(Point_6_Z_entry.get())),
                                                Vector3(float(Point_7_X_entry.get()), float(Point_7_Y_entry.get()), float(Point_7_Z_entry.get())),
                                                Vector3(float(Point_8_X_entry.get()), float(Point_8_Y_entry.get()), float(Point_8_Z_entry.get())),
                                                ) , text= "Run", master = coordenadas)
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

point_4_Lbl.pack()
Point_4_X_entry.pack()
Point_4_Y_entry.pack()
Point_4_Z_entry.pack()

point_5_Lbl.pack()
Point_5_X_entry.pack()
Point_5_Y_entry.pack()
Point_5_Z_entry.pack()

point_6_Lbl.pack()
Point_6_X_entry.pack()
Point_6_Y_entry.pack()
Point_6_Z_entry.pack()

point_7_Lbl.pack()
Point_7_X_entry.pack()
Point_7_Y_entry.pack()
Point_7_Z_entry.pack()

point_8_Lbl.pack()
Point_8_X_entry.pack()
Point_8_Y_entry.pack()
Point_8_Z_entry.pack()

coordenadas.pack()
P1.pack(side=TOP)
P2.pack(side=TOP)
P3.pack(side=TOP)
P4.pack(side=TOP)
P5.pack(side=TOP)
P6.pack(side=TOP)
P7.pack(side=TOP)
P8.pack(side=TOP)

run_btn.pack()

win.mainloop()