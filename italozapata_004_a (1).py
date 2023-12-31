# -*- coding: utf-8 -*-
"""ItaloZapata_004_A

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xQw0-MYqn-r1bW9gRO2eTVw8Pp59sdI9
"""

from os import system
system("cls")

from datetime import datetime

tiempo = datetime

fila_A= [1,11,21,31,41,51,61,71,81,91]
fila_B = [2,12,22,32,42,52,62,72,82,92]
fila_C = [3,13,23,34,43,53,63,73,83,93]
fila_D = [4,14,24,34,44,54,64,74,84,94]
fila_E = [5,15,25,35,45,55,65,75,85,95]
fila_F = [6,16,26,36,46,56,66,76,86,96]
fila_G = [7,17,27,37,47,57,67,77,87,97]
fila_H = [8,18,28,38,48,58,68,78,88,98]
fila_j = [9,19,29,39,49,59,69,79,89,99]
fila_i = [10,20,30,40,50,60,70,80,90,100]

Asistentes= []
def menu():
    print("""
    Creativos.cl

1.- Comprar entradas
2.- Mostrar Ubicaciones disponibles
3.- Ver listado de asistentes
4.- Mostrar gananacias totales
5.- Salir\n""")

def Mostrar_Ubicaciones():
    system("cls")
    print("       _____________________________")
    print("       |          ECENARIO          |")
    print("       |____________________________|")
    for asiento in range(0,10):
        print(f"FILA {asiento+1} |{fila_A[asiento]}|{fila_B[asiento]}|{fila_C[asiento]}|{fila_D[asiento]}|{fila_E[asiento]}|{fila_F[asiento]}|{fila_G[asiento]}|{fila_H[asiento]}|{fila_j[asiento]}|{fila_i[asiento]}")
    print("")
    input("Enter para continuar\n")

def ComprarEntradas():
  Mostrar_Ubicaciones()
  rut = int(input("\nIngrese su Rut sin dijito verificador ni puntos :"))
  lis_rut =[rut]
  Asistentes.append(lis_rut)
  entrada = int(input("Precios de asientos\nPlatuniun $120000  1-20\nGold $80000  21-50\nSilver $50000  51-100\nIngresa el asiento :"))
  if entrada ==11 or entrada == 21 or entrada == 31 or entrada == 41 or entrada == 51 or entrada == 61 or entrada ==71 or entrada == 81 or entrada == 91:
    calculo = entrada//10
    fila_A[calculo] = "X"
    if entrada ==1:
      fila_A[entrada-1]
  elif entrada ==12 or entrada ==22 or entrada == 32 or entrada == 42 or entrada == 52 or entrada == 62 or entrada == 72 or entrada ==82 or entrada == 92:
    calculo = entrada//10
    fila_B[calculo] = "X"
    if entrada==2:
      fila_B[entrada-1]
  elif entrada ==13 or entrada == 23 or entrada == 33 or entrada == 43 or entrada == 53 or entrada == 63 or entrada ==73 or entrada == 83 or entrada == 93:
    calculo = entrada//10
    fila_C[calculo] = "X"
    if entrada==3:
      fila_C[entrada-1]
  elif entrada ==14 or entrada == 24 or entrada == 34 or entrada == 44 or entrada == 54 or entrada == 64 or entrada ==74 or entrada == 84 or entrada == 94:
    calculo = entrada//10
    fila_D[calculo] = "X"
    if entrada==4:
      fila_D[entrada-1]
  elif entrada ==15 or entrada == 25 or entrada == 35 or entrada == 45 or entrada == 55 or entrada == 65 or entrada ==75 or entrada == 85 or entrada == 95:
    calculo = entrada//10
    fila_E[calculo] = "X"
    if entrada==5:
      fila_E[entrada-1]
  elif entrada ==16 or entrada == 26 or entrada == 36 or entrada == 46or entrada == 56 or entrada == 66 or entrada ==76 or entrada == 86 or entrada == 96:
    calculo = entrada//10
    fila_F[calculo] = "X"
    if entrada==6:
      fila_F[entrada-1]
  elif entrada ==17 or entrada == 27 or entrada == 37 or entrada == 47 or entrada == 57 or entrada == 67 or entrada ==77 or entrada == 87 or entrada == 97:
    calculo = entrada //10
    fila_G[calculo] = "X"
    if entrada==7:
      fila_G[entrada-1]
  elif entrada ==18 or entrada == 28 or entrada == 38 or entrada == 48 or entrada == 58 or entrada == 68 or entrada ==78 or entrada == 88 or entrada == 98:
    calculo = entrada //10
    fila_H[calculo] = "X"
    if entrada==8:
      fila_H[entrada-1]
  elif entrada ==19 or entrada == 29 or entrada == 39 or entrada == 49 or entrada == 59 or entrada == 69 or entrada ==79 or entrada == 89 or entrada == 99:
    calculo = entrada //10
    fila_j[calculo] = "X"
    if entrada==9:
      fila_j[entrada-1]
  elif entrada ==20or entrada == 30 or entrada == 40 or entrada == 50 or entrada == 60 or entrada == 70 or entrada ==80 or entrada == 90 or entrada == 100:
    calculo = entrada // 10
    fila_i[calculo] = "X"
    if entrada==10:
      fila_i[entrada-1]

def Listado_Asistentes(): # Si no se muestra nada es porque no hay nadie registrado en lista de Asistentes
  system("cls")
  print("Registro de personas")
  print("--------------------")
  for persona in Asistentes:
    print(f"{persona+1} / {Asistentes[persona]}")
  input("Enter para volver al menu")

def Ganancias_Totales():
  system("cls")
  P = 120000
  G = 80000
  S = 50000
  cantidad =int(input("Ingresa la cantidad :"))
  total = (P*cantidad)+(G*cantidad)+(S*cantidad)
  print("Tipo de entrada /  Cantidad  /  Total")
  print(f"Platiniun       /  {cantidad}  /  {P*cantidad}$")
  print(f"Gold            /  {cantidad}  /  {G*cantidad}$")
  print(f"Silver          /  {cantidad}  /  {S*cantidad}$")
  print(f"TOTAL           /  {cantidad*3}  / {total}$")

def Salir():
  system("cls")
  print(f"Gracias por usar nuestro Servicios {nombre}")
  print(f"Programa utilizado el {tiempo}\n")

nombre=input("Para comenzar ingresa tu nombre y apellido porfavor : ")
while True:
    try:
        system("cls")
        menu()
        op=input("\nIngrese opción una opcion mostrada anteriormente : ")
        match op:
            case "1":
              ComprarEntradas()
            case "2":
              Mostrar_Ubicaciones()
            case "3":
              Listado_Asistentes()
            case "4":
              Ganancias_Totales()
            case "5":
              Salir()
              break
    except ValueError as op:
        print("Solo los datos numericos dados en pantalla")