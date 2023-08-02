from Pais import *
import csv
listapaises=[]
with open('C:/Users/SENA/Downloads/pais.csv') as paiscsv:
    
    csvReader=csv.reader(paiscsv)
    for row in csvReader:
        ob=Pais(row[0],row[1],row[2],row[3])
        listapaises.append(ob)
        
    for pai in listapaises:
        print('nombre:',pai.getNombre())
        print('poblacion:',pai.getPoblacion())
        print('altura:',pai.getAltura())
        print('pob_cap:',pai.getPob_cap())