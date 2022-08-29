# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2

# Create an instance of TKinter Window or frame
win= Tk()

# Set the size of the window
win.geometry("700x350")# Create a Label to capture the Video frames
label =Label(win)
label.grid(row=0, column=0)
cap= np.zeros((300,300,3), dtype=np.uint8)

# Define function to show frame
def show_frames():
      # Get the latest frame and convert into Image
      
      img = Image.fromarray(cap)

      # Convert image to PhotoImage
      imgtk = ImageTk.PhotoImage(image = img)
      label.imgtk = imgtk
      label.configure(image=imgtk)

# Repeat after an interval to capture continiously

show_frames()
win.mainloop()