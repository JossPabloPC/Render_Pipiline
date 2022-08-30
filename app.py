# Import required Libraries
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2

from Coordinates import Vector3

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

# Create an instance of TKinter Window or frame
win= tk.Tk()
win.geometry("1080x720")# Create a Label to capture the Video frames

# Output image
cap= np.zeros((300,300,3), dtype=np.uint8)

#Frames
coordenadas = tk.Frame()

#--WIDGETS--
greeting    = tk.Label(text="Welcome to Python Render Pipeline", fg="white", bg="black",width=50, height=3)
camera      = tk.Label(text="Camera coordinates")
#Camara
Camera_X_entry = tk.Entry(master=coordenadas)
Camera_Y_entry = tk.Entry(master=coordenadas)
Camera_Z_entry = tk.Entry(master=coordenadas)

Camera_X_entry.insert(0,"X")
Camera_Y_entry.insert(0,"Y")
Camera_Z_entry.insert(0,"Z")

#Punto

run_btn     = tk.Button(command=lambda: printVector(Camera_X_entry, Camera_Y_entry, Camera_Z_entry), text= "Run")

#Packing
greeting.pack()
camera.pack()
Camera_X_entry.pack(side=tk.LEFT)
Camera_Y_entry.pack(side=tk.LEFT)
Camera_Z_entry.pack()
coordenadas.pack()
run_btn.pack()

win.mainloop()