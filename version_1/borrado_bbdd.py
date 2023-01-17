# Formulario para borrar todos los registros pertenecientes a una tabla.
# Parte de la vista del modelo MVC.

from PyQt5 import QtCore 
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from crud_bd import borra_contenido


class BorrarTabla(object):
    
    def __init__(self, ventana: QDialog):
        
        super().__init__()

        #Obtiene la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 4.159)
        alto = float(size.height() / 6.668)
        

        self.frm_borrar_tabla = ventana
        self.frm_borrar_tabla.setObjectName("frm_borrar_tabla")
        self.frm_borrar_tabla.resize(ancho, alto)
        self.frm_borrar_tabla.setMinimumSize(ancho, alto)
        self.frm_borrar_tabla.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_borrar_tabla.setWindowIcon(icon)

        self.gridLayout = QGridLayout(self.frm_borrar_tabla)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lbl_0 = QLabel(self.frm_borrar_tabla)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)

        self.cmb_tabla = QComboBox(self.frm_borrar_tabla)
        self.cmb_tabla.setObjectName("cmb_tabla")
        self.gridLayout.addWidget(self.cmb_tabla, 0, 1, 1, 2)
        self.cmb_tabla.addItem('Remuneraciones')
        self.cmb_tabla.addItem('Deducciones')
        self.cmb_tabla.addItem('Cargas de familia')
        self.cmb_tabla.addItem('Ganancias otros empleadores')
        self.cmb_tabla.addItem('Promedio bruto')
        self.cmb_tabla.addItem('Ded. Esp. Inc. Primera parte')
        self.cmb_tabla.addItem('Ded. Esp. Inc. Segunda parte')

        self.cmb_tabla.currentTextChanged.connect(self.on_cmb_click)

        self.lbl_1 = QLabel(self.frm_borrar_tabla)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 0, 1, 1)

        self.cmb_mes = QComboBox(self.frm_borrar_tabla)
        self.cmb_mes.setObjectName("cmb_mes")
        self.gridLayout.addWidget(self.cmb_mes, 1, 1, 1, 1)
        self.cmb_mes.addItem('*')

        i = 1
        while i <= 12:
            self.cmb_mes.addItem(str(i))
            i += 1

        self.lbl_2 = QLabel(self.frm_borrar_tabla)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 1, 2, 1, 1)

        self.cmb_year = QComboBox(self.frm_borrar_tabla)
        self.cmb_year.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.cmb_year, 1, 3, 1, 1)
        self.cmb_year.addItem('*')
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')

        self.btn_cerrar = QPushButton(self.frm_borrar_tabla)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 2, 2, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_borrar_tabla.close())

        self.btn_ejecutar = QPushButton(self.frm_borrar_tabla)
        self.btn_ejecutar.setObjectName("btn_ejecutar")
        self.gridLayout.addWidget(self.btn_ejecutar, 2, 3, 1, 1)
        self.btn_ejecutar.clicked.connect(lambda: self.elimina_informacion())

        QtCore.QMetaObject.connectSlotsByName(self.frm_borrar_tabla)

        _translate = QtCore.QCoreApplication.translate
        self.frm_borrar_tabla.setWindowTitle(_translate("self.frm_borrar_tabla", "Borrar registros"))
        self.lbl_0.setText(_translate("self.frm_borrar_tabla", "Nombre tabla:"))
        self.lbl_1.setText(_translate("self.frm_borrar_tabla", "Mes:"))
        self.lbl_2.setText(_translate("self.frm_borrar_tabla", "Año:"))
        self.btn_cerrar.setText(_translate("self.frm_borrar_tabla", "Cerrar"))
        self.btn_ejecutar.setText(_translate("self.frm_borrar_tabla", "Ejecutar"))


    def on_cmb_click(self):
        
        if self.cmb_tabla.currentText() == 'Cargas de familia':
            self.cmb_mes.setEnabled(False)
        else:
            self.cmb_mes.setEnabled(True)


    def elimina_informacion(self):

        try:   
    
            tabla = self.cmb_tabla.currentText()
        
            year = list()
            year.append(self.cmb_year.currentText())

            month = list()
            month.append(self.cmb_mes.currentText())

            mensaje = f'El siguiente procedimiento borrará los registros de la tabla {tabla}. ¿Desea continuar?'
            msg_box = QMessageBox.question(self.frm_borrar_tabla, 'Advertencia', mensaje, QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        
            if msg_box == QMessageBox.Yes:
            
                resultado = borra_contenido(tabla, month, year)
            
                if resultado == True:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setText("Se eliminaron los registros de la base de datos.")
                    msg_box.setWindowTitle("Información")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    #msg_box.buttonClicked.connect(msgButtonClick)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    msg_box.setWindowIcon(icon) 
                    msg_box.exec()
                    self.frm_borrar_tabla.close()
                else:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setText("Error en el proceso de borrado.")
                    msg_box.setWindowTitle("Error")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    #msg_box.buttonClicked.connect(msgButtonClick)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    msg_box.setWindowIcon(icon) 
                    msg_box.exec()

        except Exception as error:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()