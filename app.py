# Import required Libraries
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2

from Coordinates import *
from Camera import Camera

#Constantes
Up      =  Vector3(0, 1, 0)
Right   =  Vector3(1, 0, 0)
Forward =  Vector3(0, 0, 1)

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

def _3D_2_2D(camera, point):
      camera.obtener_W(point)
      camera.W.normalizar_vector()
      camera.U = Vector3.producto_cruz(camera.V, camera.W)
      print("U == X: " + str(camera.U.x) + " Y: " + str(camera.U.y) + " Z: " + str(camera.U.z) + " Magnitud: " + str(camera.U.magnitud) )
      camera.setMatrizcambio()
      camera.setViewMatrix()


# Create an instance of TKinter Window or frame
win= tk.Tk()
win.geometry("1080x720")# Create a Label to capture the Video frames

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

#Objeto camara
W = Vector3(0,0,0)
U = Vector3(0,0,0)
V = Up
coordenada = Vector3(int(Camera_X_entry.get()), int(Camera_Y_entry.get()), int(Camera_Z_entry.get()))
point = Vector3(float(Point_X_entry.get()), float(Point_Y_entry.get()), float(Point_Z_entry.get()))
camara = Camera(W, U, V, coordenada)

#Punto
run_btn     = tk.Button(command=lambda: _3D_2_2D(camara, point) , text= "Run")

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