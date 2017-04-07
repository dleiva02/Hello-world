# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:42:01 2016

@author: Cesar
@modified by: David Leiva
"""

import os
import glob
import csv
import matplotlib.pyplot as plt
import time
import numpy as np
#import random
from openpyxl import load_workbook

#@Leiva 
import pickle

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, protocol=1)
        #pickle.dump(obj, f, protocol=1)
def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


#==============================================================================
# Este programa se encarga de obtener los valores estadísticos necesarios para 
# generar curvas de carga para cargas residenciales
#==============================================================================

import unicodedata
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))



Vector_General_DeInfo=[]
#Incializar variables
dic_conjunto={}
dic_Nombre={'Nombre':''}
dic_provincia={'Provincia':''}
dic_canton={'Canton':''}
dic_distrito={'Distrito':''}
dic_empresa={'Empresa':''}
dic_consumo={'Consumo':''}
dic_curvaPromedio={'Curva':[]}
dic_curvaFinde={'CurvaFinde':[]}
#dic_curvaDesviacion={'Desviacion':[]}



dic_conjunto.update(dic_Nombre)
dic_conjunto.update(dic_provincia)
dic_conjunto.update(dic_canton)
dic_conjunto.update(dic_distrito)
dic_conjunto.update(dic_empresa)
dic_conjunto.update(dic_consumo)
dic_conjunto.update(dic_curvaPromedio)
dic_conjunto.update(dic_curvaFinde)








##Extracción de los datos desde los archivos .csv del UVECASE
##Primero genero la lista que contenga todos los .csv
direccion=os.getcwd()+'\Data\Residencial_Actualizado'
#direccion=os.getcwd()+'\Data\Residencial_Todos'
archivos=list(glob.glob(os.path.join(direccion,'*csv')))

##Se obtienen los datos de los clientes asignados en el control de actas
#direccion1=os.getcwd()+'\Actas\control_actas_pruebaleiva.xlsx'
#direccion1=os.getcwd()+'\Actas\Muestra3.xlsx'
direccion1=os.getcwd()+'\Actas\Base de Datos QGIS M-2016.xlsm'



actas = load_workbook(filename=direccion1)

hoja = actas['Base de Datos QGISCoordenadas']


numero_medidor = []
empresa_distribuidora=[]
provincia=[]
canton=[]
distrito=[]

##Se encuentra la última celda en la que hay datos
t=0
for b in range(1,100000):
    t=t+1
    if str(hoja['G'+str(b)].value) == 'None':
        break

##Se obtienen los # de medidor, empresa distribuidora y ubicación geográfica
for ent in range(2,t):
    if str(hoja['G'+str(ent)].value) == 'None':
        break
    numero_medidor.append(hoja['G'+str(ent)].value)
    empresa_distribuidora.append(hoja['H'+str(ent)].value)
    provincia.append(hoja['J'+str(ent)].value)
    canton.append(hoja['K'+str(ent)].value)
    distrito.append(hoja['L'+str(ent)].value)
   
   
   
##Tratamiento de los strings a Mayusculaas y sin tildes
for x in range(len(provincia)):
    provincia[x]=elimina_tildes(provincia[x].upper().replace(" ", "")) 
    canton[x]=elimina_tildes(canton[x].upper().replace(" ", ""))
    distrito[x]=elimina_tildes(distrito[x].upper().replace(" ", ""))    
    empresa_distribuidora[x]=elimina_tildes(empresa_distribuidora[x].upper().replace(" ", ""))



#sentence.replace(" ", "")

#==============================================================================
# Asignación de fp y P promedios por hora para cada cliente
#==============================================================================

#Se guardan los valores de energía total, fp y P por compañía
#Energía
e_total=[]

#Potencia activa
P_total_finde=[]
P_total_entre=[]

#Se crean los diccionarios que contienen los datos de cada compañía
companias_pot_finde={}
companias_pot_entre={}
companias_fp_finde={}
companias_fp_entre={} 

#Se crea el vector que define los rangos que se van a utilizar
e=[]
a= np.arange(0,350,25)
b=np.arange(350,500,50)
c=np.arange(500,1000,100)
d=np.arange(1000,3000,500)
e.extend(a)
e.extend(b)
e.extend(c)
e.extend(d)
#Se crean los diccionarios para los rangos que contiene cada compañía
#Rangos [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500,3000]
rango_P_fin={}; rango_P_entre={}











numerosdemedidor=[]
#print(e)
#print(rango_fp_fin)
##Se revisa cada archivo
for archi in archivos:
    try:
       print(archi)
       #dic_temporal=  dict(dic_conjunto)       #se incializa el diccionario a utilizar
       #dic_temporal['Nombre']=archi 
       
       individual=open(archi,'r')
       lectura=list(csv.reader(individual))
    #   print(archi)
    ##Se encuentra el primer dato que se desea leer       
       for s in range(len(lectura)):
           lim=lectura[s]
           if lim == ['Interval Raw Data']:
               primero = s+2
               break
    
    ##Se llega hasta el último dato que se desea evaluar
       for n in range(11,len(lectura)):
           limite=lectura[n]
           if limite == ['Event Raw Data']:
               ultimo = n-2
               break
    
       
    ## Se obtiene la potencia activa y el factor de potencia 
       P=[]
       fp=[]
       ##Se guarda la lista de cada valor deseado
       for n in range(primero,ultimo):     
           
           activa=lectura[n][173]#Potencia activa dada
           P.append(activa)          
    ##Se guardan los valores válidos por día en vector servibles
       
       servibles_finde=[]
       servibles_entre=[]
           
       for t in range(primero,ultimo):
           tiempo=str(lectura[t][0])
           if '-' in tiempo:
               t_1=tiempo.replace('-',' ')
               tiempillo=time.strptime(t_1,"%d %b %Y %H:%M:%S")
               hora = str(tiempillo[3])
               minuto = str(tiempillo[4])
               segundo = str(tiempillo[5])
               hora_total = str(hora+':'+minuto+':'+segundo) #Obtengo el vector de tiempo deseado para comparar
           else:
               t_1=tiempo.replace('/',' ')
               tiempillo=time.strptime(t_1,"%d %m %Y %H:%M:%S")
               hora = str(tiempillo[3])
               minuto = str(tiempillo[4])
               segundo = str(tiempillo[5])
               hora_total = str(hora+':'+minuto+':'+segundo) #Obtengo el vector de tiempo deseado para comparar    
          #Se utiliza aux_t para evitar que se salga del rango del índice
           aux_t = int (t + 143)
           if hora_total == '0:0:0':
               if aux_t <= ultimo:
                   tiempo2=lectura[t+143][0]
                   if '-' in tiempo2:
                       t_2=tiempo2.replace('-',' ')
                       tiempillo2=time.strptime(t_2,"%d %b %Y %H:%M:%S")
                       hora2 = str(tiempillo2[3])
                       minuto2 = str(tiempillo2[4])
                       segundo2 = str(tiempillo2[5])
                       hora_total2 = str(hora2+':'+minuto2+':'+segundo2) #Obtengo el vector de tiempo deseado para comparar
                       dia= str(tiempillo2[6])
                   else:
                       t_2=tiempo.replace('/',' ')
                       tiempillo2=time.strptime(t_2,"%d %m %Y %H:%M:%S")
                       hora2 = str(tiempillo2[3])
                       minuto2 = str(tiempillo2[4])
                       segundo2 = str(tiempillo2[5])
                       hora_total2 = str(hora2+':'+minuto2+':'+segundo2) #Obtengo el vector de tiempo deseado para comparar
                       dia= str(tiempillo2[6])
                              
                   if hora_total2 == '23:50:0':
                       val_validos_entre=[] #Potencia para días entre semana
                       val_validos_finde=[] #Potencia para fin de semana
                       
                       if dia == '5': 
                           #Se cuenta desde la posición 0 de P y fp
                           for j in range (t-primero,t+133):
                               val_validos_finde.append(P[j])
                           #Se guardan los datos de sábado en fin de semana    
                           servibles_finde.append(val_validos_finde)
                       elif dia == '6':
                           #Se cuenta desde la posición 0 de P y fp
                           for j in range (t-primero,t+133):
                               val_validos_finde.append(P[j])
                           #Se guardan los datos de domingo en fin de semana    
                           servibles_finde.append(val_validos_finde)
                       else:
                           #Se cuenta desde la posición 0 de P y fp
                           for j in range (t-primero,t+133): 
                               val_validos_entre.append(P[j])
                           #Se guardan los datos entre semana    
                           servibles_entre.append(val_validos_entre)
                           
       
       #Convierte el array a floats para hacer el promedio                
       dat_entre=np.array(servibles_entre,dtype=np.float64)
       dat_fin=np.array(servibles_finde,dtype=np.float64)
       
       
    
       ###LEIVA
       #Cálculo de promedios para fin de semana y entre semana
       promedio_fin=dat_fin.mean(axis=0)
       promedio_entre=dat_entre.mean(axis=0)
       
       #Edit
       arr=np.array(dat_entre)
       promedio_temp=arr.mean(axis=0,dtype=np.float64)/1000 #kW CREO
       std_temp=arr.std(axis=0,dtype=np.float64)/1000       #kw CREO
       ###LEIVA   
       
       
       
       
       #Cálculo de energía mensual (kWh): E=Pt=(10/60)*(P/1000)*#días
       energia_fin=(promedio_fin.sum())*(8/6000) 
       energia_entre=(promedio_entre.sum())*(20/6000)
       energia_total=int(energia_fin+energia_entre)
          
          
          
       #Se guarda la energía total y P para todas las empresas
       e_total.append(energia_total)
       P_total_finde.append(promedio_fin)
       P_total_entre.append(promedio_entre)
       
       
       
       
       ## Se obtiene el valor de posición para el medidor que se busca para agrupar
       key2=str(lectura[3][1])
       key2_separa=str.split(key2)
    #   print(key2_separa[0])
    #   print(type(numero_medidor[0]))
       numero=0
       numerosdemedidor.append(key2_separa[0])
       for n in range(len(numero_medidor)):
    #       if key2_separa[0] == '102967':
    #           print('ok')
           if key2_separa[0] == str(numero_medidor[n]):
               print('ok')
    #           print(numero_medidor[n])
               break
           numero=numero+1
    #   print(numero)    
       if numero < len(numero_medidor):
           dic_temporal=  dict(dic_conjunto)       #se incializa el diccionario a utilizar
           dic_temporal['Nombre']=archi 
           prov_temp=provincia[numero]
           cant_temp=canton[numero]
           dist_temp=distrito[numero]
           #Se crea la división por rangos para cada compañía
           
           for ranguitos in range(25):
               if energia_total >= e[ranguitos] and energia_total < e[ranguitos+1]:
                   
                   #dic_temporal['Consumo']=str(e[ranguitos+1])
                   #Para determinar cual rango es el más cercano
                   rango_select=min([e[ranguitos],e[ranguitos+1]], key=lambda x:abs(x-energia_total))
                   
                   dic_temporal['Consumo']=rango_select
                   
                   dic_temporal['Empresa']= 'CNFL' 
                   dic_temporal['Provincia']=prov_temp
                   dic_temporal['Canton']=cant_temp
                   dic_temporal['Distrito']=dist_temp
                   
                   #dic_temporal['Curva']=promedio_temp
                   dic_temporal['Curva']=dat_entre
                   dic_temporal['CurvaFinde']=dat_fin
                   
    
               
        
           Vector_General_DeInfo.append(dic_temporal)         
                   
    
    except: 
      pass
        
    
    #guardar el objeto python
save_obj(Vector_General_DeInfo, os.getcwd()+ '\ObjetosPython\Vector_General_DeInfoLeiva')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
