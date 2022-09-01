from Coordinates import Vector3
import numpy as np

class Camera:
    def __init__(self, W, U, V, coordenada, height, width, l, f, c):
        self.W = W
        self.U = U
        self.V = V

        self.height = height    #alto plano imagen 
        self.width  = width     #ancho plano imagen

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

        self.matiz_Tp = np.array([[self.f/self.w, 0,0,0]
                                  [0, self.f/self.h,0,0]
                                  [0, 0, -(self.l+self.c)/(self.l-self.c), (2*self.l*self.c)/(self.l-self.c)]
                                  [0,0,1,0]])

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
        
        self.viewMatrix[0:3,0:3] = self.matrizDeCambio.T
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
    
    def
