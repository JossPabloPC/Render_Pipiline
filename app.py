from flask import Flask
from flask import render_template
from flask import Response
import cv2 as cv
import numpy as np

import Coordinates 

app = Flask(__name__) #Inicializa la app



@app.route("/")
def index():
    cameraPos = Coordinates.Vector3(1, 1, 1)

    img = np.zeros([50,500,3], dtype=np.uint8)
    img[cameraPos.x, cameraPos.y] = 255
    
    cv.imwrite("PipeRenderer/Render_Pipiline/static/image.png", img)
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)