# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:13:10 2016

@author: David Leiva

Version: 2.1
"""
"""
Implementado en PYTHON por:
David Leiva Arauz, estudiante de Ingeniería Eléctrica, Universidad de
Costa Rica. Octubre, 2016.

La presente función utiliza datos estadisticos obtenidos con las mediciones
realizadas por UVECASE, para generar curvas aleatorias a partir de un promedio 
y su respectiva desviacion estandar, para elllo utiliza una distribucion gaussiana.

hola adding a change

NOTA: Este se adapto del original para ser utilizado en el ambiente QGIS
debido a que utiliza una versión no actualizada de python 
"""

##############   LEIVA    ##################
### Algoritmo para obtener la info #########


import pickle
import numpy as np


###########Funciones para usar el modulo pickle############3

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
        
 
    
###############Obtencion de curva promedio y nueva desviacion estandar##########
def gen_curv_prom(filtro_final,tipo):  
    mat_potencia=[]
    #mat_desviacion=[]                
    for i in range(len(filtro_final)): 
        mat_potencia.append(filtro_final[i][tipo])
        #mat_desviacion.append(filtro_final[i]['Desviacion'])
    
    c=np.vstack((mat_potencia))

    arreglo_potencia=np.array(c)
    #arreglo_desviacion=np.array(mat_desviacion)   
    
    promedio_potencia=arreglo_potencia.mean(axis=0,dtype=np.float64)/1000   
    std_final=arreglo_potencia.std(axis=0,dtype=np.float64)/1000          #kw CREO   
    
    
    return promedio_potencia,std_final





###############Generacion de nueva curva a partir de la curva promedio y desviacion estandar##########

def gen_curv_aleatoria(curva_promedio, desviacion_estandar):
    curva_generada=[]
    temp=0.0
    for i in range(len(curva_promedio)):
        if desviacion_estandar[i]!=0:
            temp= np.random.normal(curva_promedio[i], desviacion_estandar[i],  size=None)
            #while temp<0 or temp> (curva_promedio[i] + 1*desviacion_estandar[i]) or temp< (curva_promedio[i] - 1*desviacion_estandar[i]):
            while temp<0 or temp> (curva_promedio[i] + 1*desviacion_estandar[i]):
            #if temp<0:
                #temp=0
                temp= np.random.normal(curva_promedio[i], desviacion_estandar[i],  size=None)
        else:
            temp=curva_promedio[i]
            
        curva_generada.append(temp)    
   
    return curva_generada



#########Master############




def genNewCurv(Vector_General_DeInfo,consumo_real,rango_energia,tipo_cliente,*localizacion):

    #####Inicialización de variables########
    provincia_destino=''
    canton_destino = ''
    distrito_destino = ''
    empresa_destino=''
 
    if len(localizacion)>0:
        provincia_destino=localizacion[0]
        #print(provincia_destino)
        if len(localizacion)>1:
            canton_destino=localizacion[1]
            if len(localizacion)>2:
                distrito_destino=localizacion[2]    
                if len(localizacion)>3:
                    empresa_destino=localizacion[3]   
    
    
    #Filtro el consumo
    filtro_consumo=[]
    filtro_provincia=[]
    filtro_canton=[]
    filtro_distrito=[]        
    
    for i in range(len(Vector_General_DeInfo)):
        if Vector_General_DeInfo[i]['Consumo']== rango_energia:
            filtro_consumo.append(Vector_General_DeInfo[i])
            
    
    if filtro_consumo:
        for i in range(len(filtro_consumo)):
            if filtro_consumo[i]['Provincia']== provincia_destino:
                filtro_provincia.append(filtro_consumo[i])
                
    if filtro_provincia:
        for i in range(len(filtro_provincia)):
            if filtro_provincia[i]['Canton']== canton_destino:
                filtro_canton.append(filtro_provincia[i])        
            
    if filtro_canton:         
        for i in range(len(filtro_canton)):
            if filtro_canton[i]['Distrito']== distrito_destino:
                filtro_distrito.append(filtro_canton[i])     


    #print(len(filtro_consumo))
    ######Dependiendo del filtro final se llama la función########
    ###### Se obtiene la nueva curva promedio con su desviación estandar######
         
    if filtro_distrito:               
        curva_promedio, desviacion_estandar=gen_curv_prom(filtro_distrito,'Curva')
        curva_promedio_finde,desviacion_estandar_finde = gen_curv_prom(filtro_distrito,'CurvaFinde')
    elif filtro_canton:
        curva_promedio, desviacion_estandar=gen_curv_prom(filtro_canton,'Curva')
        curva_promedio_finde,desviacion_estandar_finde = gen_curv_prom(filtro_canton,'CurvaFinde')
    elif filtro_provincia:
        curva_promedio, desviacion_estandar=gen_curv_prom(filtro_provincia,'Curva')
        curva_promedio_finde,desviacion_estandar_finde = gen_curv_prom(filtro_provincia,'CurvaFinde')    
    else:
        curva_promedio, desviacion_estandar=gen_curv_prom(filtro_consumo,'Curva')
        curva_promedio_finde,desviacion_estandar_finde = gen_curv_prom(filtro_consumo,'CurvaFinde')


    new_curve_sinEscalar=gen_curv_aleatoria(curva_promedio,desviacion_estandar)
    new_curve_sinEscalar_finde=gen_curv_aleatoria(curva_promedio_finde,desviacion_estandar_finde )
    #new_curv       
    ##### Escalamiento
    new_curve= (consumo_real/rango_energia)*np.array(new_curve_sinEscalar)
    new_curve_finde=(consumo_real/rango_energia)*np.array(new_curve_sinEscalar_finde)
    return new_curve,new_curve_finde
    
    
    
    
    
    
    