import math

class Vector3:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitud = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
    
    def setMagnitud(self):
        self.magnitud = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))
    
    def producto_cruz(vectorA, vectorB):
        vectorC = Vector3(0, 0, 0)
        vectorC.x =   vectorA.y * vectorB.z - vectorA.z * vectorB.y #X
        vectorC.y = - vectorA.x * vectorB.z - vectorA.x * vectorB.z #Y
        vectorC.z =   vectorA.x * vectorB.z - vectorA.y * vectorB.x #Z
        vectorC.magnitud = math.sqrt(math.pow(vectorC.x, 2) + math.pow(vectorC.y, 2) + math.pow(vectorC.z, 2))
        return vectorC
        
    def normalizar_vector(self):
        self.x = self.x / self.magnitud
        self.y = self.y / self.magnitud
        self.z = self.z / self.magnitud
        self.magnitud = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))
        print("Normalizado == X: " + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z) + " Magnitud: " + str(self.magnitud) )



    def restar_vector(vectorA, vectorB):
        vectorC     = Vector3(0, 0, 0)
        vectorC.x   = vectorA.x - vectorB.x
        vectorC.y   = vectorA.y - vectorB.y
        vectorC.z   = vectorA.z - vectorB.z
        vectorC.setMagnitud()
        return vectorC

    def cambiar_signo(self):
        self.x = self.x *1
        self.y = self.y *1
        self.z = self.z *1
        self.magnitud = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))



