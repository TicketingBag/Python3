"""
Asignación: 3D-Recuperacion
Autor: Eduardo Enrique Moo Cruz
Fecha: 01/02/21
"""

import time
import keyboard
import matplotlib.pyplot as plt 
from math import sin, cos, radians,sqrt

#Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=60
yc=20
zc=20

#Coordenadas del sistema local plano 
x=[]
y=[]
z=[]

def plotPlaneLine(x,y,z,xg,yg,zg,HPx,HPy):
    xg=[]
    yg=[]
    zg=[]
    x,y,z,xg,yg,zg,area1,area2,area3 = hitpoint(x,y,z,xc,yc,zc,xg,yg,zg,HPx,HPy)
    plt.axis([0,200,200,0])
    plt.axis('on')
    plt.grid(False)
    
    #Triangulo A
    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='k') 
    plt.plot([xg[2],xg[1]],[yg[2],yg[1]],color='k')
    plt.plot([xg[1],xg[0]],[yg[1],yg[0]],color='k')

    #Triangulo A1
    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='k')
    plt.plot([xg[3],xg[2]],[yg[3],yg[2]],linestyle=':',color='r')
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],linestyle=':',color='r')

    # triangulo A2
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],linestyle=':',color='r') 
    plt.plot([xg[3],xg[1]],[yg[3],yg[1]],linestyle=':',color='r')
    plt.plot([xg[1],xg[0]],[yg[1],yg[0]],color='k')

    plt.text(xg[3],yg[3],'3')
    plt.text(xg[0],yg[0],'0')
    plt.text(xg[2],yg[2],'2')
    plt.text(xg[1],yg[1],'1')

    #Etiqueta de las areas
    plt.text(20,130,'Area Triángulo A = ' + str(area1))
    plt.text(20,145,'Area Triángulo A2 = ' + str(area2))
    plt.text(20,160,'Area Triángulo A3 = ' + str(area3))
    A=area2+area3
    plt.text(20,175,'A2 + A3 = ' + str(A))

#esta fuera del limite o dentro del limite.
    if (area2+area3 > area1):
        plt.text(20,75,'Fuera del limite',color='r')
        plt.scatter(xg[3],yg[3],s=60,color='r')
    elif (area2+area3 < area1):
        plt.text(20,75,'Dentro del limite',color='g')
        plt.scatter(xg[3],yg[3],s=60,color='g')


    plt.title("3D-Recuperacion")
    plt.show()


def hitpoint(x,y,z,xc,yc,zc,xg,yg,zg,HPx,HPy):

    x=[40,30,80,HPx]
    y=[60,10,60,HPy] 
    z=[0,0,0,0]

    for i in range(len(x)):
        xg.append(x[i]+xc)
        yg.append(y[i]+yc)
        zg.append(z[i]+zc)

#Triangulo A

    #distancia del punto 0 to 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    P01=sqrt(a*a+b*b+c*c) 

    #distancia del punto 1 to 2
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    P12=sqrt(a*a+b*b+c*c) 

    #Distancia del punto 2 to 0
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    P02=sqrt(a*a+b*b+c*c) 

    s1 = (P01+P12+P02)/2 #  S y A
    area1 = sqrt(s1*(s1-P01)*(s1-P12)*(s1-P02))

#Triangulo A1

    #Distancia del punto 0 to 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    P01=sqrt(a*a+b*b+c*c) 

    #Distancia del punto 1 to 3
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    P13=sqrt(a*a+b*b+c*c) 

    #Distancia del punto 3 to 0
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    P03=sqrt(a*a+b*b+c*c)  

    s2 = (P01+P13+P03)/2 # s y a
    area2 = sqrt(s2*(s2-P01)*(s2-P13)*(s2-P03))  

#Triangulo A2

    #Distancia del punto 0 to 2
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    P02=sqrt(a*a+b*b+c*c) 

    #Distancia del punto2 to 3
    a=x[3]-x[2]
    b=y[3]-y[2]
    c=z[3]-z[2]
    P23=sqrt(a*a+b*b+c*c) 

    #Distancia del punto 3 to 0
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    P03=sqrt(a*a+b*b+c*c) 

    s3 = (P02+P23+P03)/2 # s y a
    area3 = sqrt(s3*(s3-P02)*(s3-P23)*(s3-P03))

    return x,y,z,xg,yg,zg,area1,area2,area3

#Se le pedira al usuario que proporcione las coodenadas
while True:
    axis=input('Teclee "V" para colocar las coodenadas o teclee "esc" para salir: ')
    if axis=='esc': 
        break
    if axis=='V':
        HPx=(float(input('X: '))) 
        HPy=(float(input('Y: ')))
        plotPlaneLine(x,y,z,xg,yg,zg,HPx,HPy)