# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:06:36 2017

@author: David Leiva

Este script es para graficar curvas con frecuencia de cada 10 min 
"""

import numpy as np
import matplotlib.pyplot as plt

def Imprimir(curva,titulo,serie):
    
    eje_x = np.arange(144)
    labels=  np.arange(0,26,2)
    eje_xx= np.arange(0,148,12)
      
    #plt.plot(eje_x, curva,'K', label= serie ,linewidth=2)
    plt.plot(eje_x, curva,label= serie,linewidth=2)    
    plt.legend(prop={'size':20}, loc=2)
    
    plt.xticks(eje_xx, labels)
    plt.title( titulo , fontsize=24, fontweight='bold')
    plt.ylabel('Demanda $[kW]$' , fontsize=20)
    plt.xlabel(u'Tiempo del día (resolución de 10 min)' ,  fontsize=20)
    plt.axis([0, 144 ,0,6])
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    #plt.show()
    
    
    
    
def Imprimir_Error(Promedio,std,titulo,serie):
    blue=(0.12156862745098,0.466666666666667,0.705882352941177)
    eje_x = np.arange(144)
    labels=  np.arange(0,26,2)
    eje_xx= np.arange(0,148,12)
    
    plt.errorbar(eje_x, Promedio, yerr=std,linewidth=1,ecolor=blue,color='red') 
    
    plt.plot(eje_x, Promedio,'r',ls='-', label=serie,linewidth=2)   




   
    plt.legend(prop={'size':14},loc=1)
    plt.xticks(eje_xx, labels)
    plt.title(titulo, fontsize=24, fontweight='bold')
    plt.ylabel('Demanda $[kW]$' , fontsize=14)
    plt.xlabel(u'Tiempo del día (resolución de 10 min)' ,  fontsize=14)
    plt.axis([0, 144 ,0,1.4])
    #manager = plt.get_current_fig_manager()
    #manager.window.showMaximized()
    plt.show()