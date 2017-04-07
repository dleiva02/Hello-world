# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Apr  3 10:24:58 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(444, 124)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo_cnfl._pequeno.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.buttonBox_Aceptar = QtGui.QDialogButtonBox(MainWindow)
        self.buttonBox_Aceptar.setGeometry(QtCore.QRect(0, 80, 201, 32))
        self.buttonBox_Aceptar.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_Aceptar.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_Aceptar.setObjectName(_fromUtf8("buttonBox_Aceptar"))
        self.checkBox_Editor = QtGui.QCheckBox(MainWindow)
        self.checkBox_Editor.setGeometry(QtCore.QRect(10, 50, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Editor.setFont(font)
        self.checkBox_Editor.setObjectName(_fromUtf8("checkBox_Editor"))
        self.label_3 = QtGui.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox_Consulta = QtGui.QCheckBox(MainWindow)
        self.checkBox_Consulta.setGeometry(QtCore.QRect(90, 50, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_Consulta.setFont(font)
        self.checkBox_Consulta.setObjectName(_fromUtf8("checkBox_Consulta"))
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(210, 50, 231, 71))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("logo_cnfl_grande.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))

        #Para seleccionar un checkBox u otro
        self.checkBox_Consulta.stateChanged.connect(self.uncheck2)
        self.checkBox_Editor.stateChanged.connect(self.uncheck)


        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.buttonBox_Aceptar, QtCore.SIGNAL(_fromUtf8("accepted()")), MainWindow.accept)
        QtCore.QObject.connect(self.buttonBox_Aceptar, QtCore.SIGNAL(_fromUtf8("rejected()")), MainWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Generación de curvas Típicas", None))
        self.checkBox_Editor.setText(_translate("MainWindow", "Editor", None))
        self.label_3.setText(_translate("MainWindow", "Seleccione el modo de modo de operación", None))
        self.checkBox_Consulta.setText(_translate("MainWindow", "Consulta", None))


        #optimizar esto
    def uncheck(self,state):
         if state >0:
              self.checkBox_Consulta.setChecked(False)
              self.modo='editor'
              
    def uncheck2(self,state):
         if state >0:
              self.checkBox_Editor.setChecked(False)     
              self.modo='consulta'



#
#def run():
#    if __name__ == "__main__":
#        import sys
#        app = QtGui.QApplication(sys.argv)
#        MainWindow = QtGui.QDialog()
#        ui = Ui_MainWindow()
#        ui.setupUi(MainWindow)
#        MainWindow.show() 
#        result = MainWindow.exec_()    
#           
#        if result:
#            print(ui.hola)  
#            #sys.exit(app.exec_()) 
#            return 0
#run()