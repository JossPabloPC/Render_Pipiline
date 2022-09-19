from Coordinates import Vector3
import numpy as np
import math

class Camera:
    def __init__(self, W, U, V, coordenada, height, width, l, f, c):
        self.W = W
        self.U = U
        self.V = V

        self.height = height    #alto plano imagen 
        self.width  = width     #ancho plano imagen
        self.ratio = width/height #Aspect ratio
        self.f = f              #Distacia plano imagen
        self.l = l              #Distancia plano lejano
        self.c = c              #Distancia plano cercano

        self.coordenada = coordenada
        self.matrizDeCambio = np.array([[0,0,0],
                                        [0,0,0],
                                        [0,0,0]], dtype=np.float) 
        
        self.viewMatrix = np.array ([[0,0,0,0],
                                     [0,0,0,0],
                                     [0,0,0,0],
                                     [0,0,0,0]], dtype=np.float)

        self.matriz_Tp = np.array([[self.f/1, 0,0,0],
                                  [0, self.f/self.ratio,0,0],
                                  [0, 0, -(self.l+self.c)/(self.l-self.c), (2*self.l*self.c)/(self.l-self.c)],
                                  [0,0,-1,0]])

    def obtener_W(self, punto):
        self.W = Vector3.restar_vector(self.coordenada, punto)
        print("W == X: " + str(self.W.x) + " Y: " + str(self.W.y) + " Z: " + str(self.W.z) + " Magnitud: " + str(self.W.magnitud) )
    
    def setMatrizcambio(self):
        #U - Right 
        self.matrizDeCambio[0,0] = self.U.x
        self.matrizDeCambio[0,1] = self.U.y
        self.matrizDeCambio[0,2] = self.U.z

        #V - UP
        self.matrizDeCambio[1,0] = self.V.x
        self.matrizDeCambio[1,1] = self.V.y
        self.matrizDeCambio[1,2] = self.V.z

        #W - Forward
        self.matrizDeCambio[2,0] = self.W.x
        self.matrizDeCambio[2,1] = self.W.y
        self.matrizDeCambio[2,2] = self.W.z

        print(self.matrizDeCambio)
    
    def setViewMatrix(self):
        arr_coordenada = np.array([[self.coordenada.x], [self.coordenada.y], [self.coordenada.z]])
        self.arregloDerecho = np.matmul(self.matrizDeCambio, arr_coordenada)
        
        self.viewMatrix[0:3,0:3] = self.matrizDeCambio
        self.viewMatrix[0:3,3] = -self.arregloDerecho[:,0]
        self.viewMatrix[3,:] = [0,0,0,1]
        print("---.---.---.---")
        print("View Matrix")
        print(self.viewMatrix)

    def get_coordenadas_respecto_camara(self, punto_original):
        punto_multiplicable = np.array([[punto_original.x], [punto_original.y], [punto_original.z], [1]])
        print("")
        punto_respecto_camara = np.matmul(self.viewMatrix, punto_multiplicable)
        print(punto_respecto_camara)

        return punto_respecto_camara
    
    def get_coordenadas_plano_cercano(self, punto_respecto_camara):
        coordenadas_plano_cercano = np.matmul(self.matriz_Tp, punto_respecto_camara)
        coordenadas_plano_cercano = coordenadas_plano_cercano/coordenadas_plano_cercano[3]
        print()
        print("coordenadas_plano_cercano:")
        print(coordenadas_plano_cercano)
        return coordenadas_plano_cercano

    def get_coordenadas_pantalla(self, punto_plano_cercano):
        x = ((self.width - 0)/(2)) * punto_plano_cercano[0] + ((self.width - 0)/(2))*(1)
        y = ((self.height - 0)/(2 * self.ratio)) * punto_plano_cercano[1] + ((self.height - 0)/(2 * self.ratio))*(self.ratio)
        x = self.width  - x[0]
        y = self.height - y[0]
        return math.ceil(y),math.ceil(x)