# Import required Libraries
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2

#Functions
def array2Window(arr):
      mylabel = tk.Label(text="clicked")
      mylabel.pack()     
#      img = Image.fromarray(arr)
#
#      # Convert image to PhotoImage
#      imgtk             = ImageTk.PhotoImage(image = img)
#      output_image      = tk.Label(image=imgtk)
#      output_image.image= imgtk
#      output_image.pack()

# Create an instance of TKinter Window or frame
win= tk.Tk()
win.geometry("1080x720")# Create a Label to capture the Video frames

# Output image
cap= np.zeros((300,300,3), dtype=np.uint8)

#Frames
coordenadas = tk.Frame()

#Widgets
greeting = tk.Label(text="Welcome to Python Render Pipeline", fg="white", bg="black",width=50, height=3)
entryX      = tk.Entry(master=coordenadas)
entryY       = tk.Entry(master=coordenadas)
run_btn = tk.Button(command=array2Window(cap), text= "Run")

#Packing
greeting.pack()
entryX.pack(side=tk.LEFT)
entryY.pack()
run_btn.pack()
coordenadas.pack()


# Repeat after an interval to capture continiously

win.mainloop()