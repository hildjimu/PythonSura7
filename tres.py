#Crear un menú de dos opciones
contador=0
print("Enamorate de Antioquia")
print("Menu")
print("1. Agregar pueblos ")
print("2. Mostrar rutas ")
print("3. Salir ")

pueblos=[]
while(contador!=3):
    pueblo={}
    contador= int(input("Digita una opción "))
    if(contador==1):
        print("Agregando pueblo: ")
        pueblo['nombre']= input("Ingrese el nombre del pueblo: ")
        pueblo['Distancia']= input("Ingrese la distancia del pueblo: ")
        pueblo['Población']= input("Ingrese el numero de personas del pueblo: ")
        pueblos.append(pueblo)

    elif(contador==2):
        print("mostrando rutas: ")
        print(pueblos)

    elif(contador==3):
            print("Saliendo: ")
            break

    else:
        print("Opcion Invalida:")