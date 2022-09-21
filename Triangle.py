import math as m
class Triangle:
    def __init__(self,P1,P2,P3,display):
        self.P1         = P1
        self.P2         = P2
        self.P3         = P3
        self.display    = display

    def trazar_linea(self, A, B, display):

        #Pendiente
        Mx = B[0] - A[0]
        My = B[1] - A[1]

        #Pendiente Mayor
        if (abs(Mx) > abs(My)):
            S = abs(Mx)
        elif(abs(Mx) <= abs(My)):
            S = abs(My)
        
        if (S == 0):
            return
        #Deltas
        Dx = Mx/S
        Dy = My/S

        currentPos = A[0:2]

        for i in range(abs(S)):
            newPoint = [m.floor(A[0] + Dx * i), m.floor(A[1] + Dy * i)]
            display[newPoint[1],newPoint[0]] = (255,255,255)
    
    def trazar_triangulo(self):
        self.trazar_linea(self.P1, self.P2, self.display)
        self.trazar_linea(self.P2, self.P3, self.display)
        self.trazar_linea(self.P3, self.P1, self.display)