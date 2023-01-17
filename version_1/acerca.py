# Formulario acerca de... 
# 
# Parte de la vista dle modelo MVC.


import webbrowser
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout


class Acerca(object):

    def __init__(self, ventana: QDialog):

        #Obtiene la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 4.37)
        alto = float(size.height() / 4.57)
        
        super().__init__()

        self.frm_acerca = ventana
        self.frm_acerca.setObjectName("self.frm_acerca")
        self.frm_acerca.resize(ancho, alto)
        self.frm_acerca.setMinimumSize(ancho, alto)
        self.frm_acerca.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_acerca.setWindowIcon(icon) 

        self.gridLayout = QGridLayout(self.frm_acerca)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_0 = QLabel(self.frm_acerca)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 3)

        self.lbl_1 = QLabel(self.frm_acerca)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 0, 1, 1)

        self.lbl_2 = QLabel(self.frm_acerca)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 2, 0, 1, 3)

        self.lbl_3 = QLabel(self.frm_acerca)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 3, 0, 1, 2)

        self.btn_web = QPushButton(self.frm_acerca)
        self.btn_web.setObjectName("btn_web")
        self.gridLayout.addWidget(self.btn_web, 4, 1, 1, 1)
        self.btn_web.clicked.connect(lambda: self.webpage())

        self.btn_cerrar = QPushButton(self.frm_acerca)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 4, 2, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_acerca.close())

        QtCore.QMetaObject.connectSlotsByName(self.frm_acerca)

        _translate = QtCore.QCoreApplication.translate
        self.frm_acerca.setWindowTitle(_translate("self.frm_acerca", "Acerca de..."))
        self.lbl_0.setText(_translate("self.frm_acerca", "PayroolTools - Deducción especial incrementada."))
        self.lbl_1.setText(_translate("self.frm_acerca", "Versión 1.0.0"))
        self.lbl_2.setText(_translate("self.frm_acerca", "Desarrollado por Jorge Eduardo Arrieta para Payroll Tools."))
        self.lbl_3.setText(_translate("self.frm_acerca", "Año, 2022 - Buenos Aires, Argentina"))
        self.btn_web.setText(_translate("self.frm_acerca", "Sitio Web"))
        self.btn_cerrar.setText(_translate("self.frm_acerca", "Cerrar"))


    def webpage(self):
        webbrowser.open("http://www.payrolltools.ar", new=2, autoraise=True) 