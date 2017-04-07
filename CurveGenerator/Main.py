# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 10:50:32 2017

@author: David Leiva
"""
import sys
from MainWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui



from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QFileDialog
# Initialize Qt resources from file resources.py

import os.path
from PyQt4.QtGui import *
from PyQt4.QtCore import QVariant







def MainWindow_Run(): 
    if __name__ == "__main__":
        
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QDialog()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show() 
        result = MainWindow.exec_()    
        
        if result:
            #print(ui.hola)  
            #MainWindow.close()
            #sys.exit(app.exec_()) 
            QMessageBox.information(None, u"Información",'Se completo con exito, el modo elejido es: ' + ui.modo)
            return 0

MainWindow_Run()