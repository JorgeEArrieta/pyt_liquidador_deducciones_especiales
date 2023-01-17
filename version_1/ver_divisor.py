# Formulario para ver un registro individual de la tabla divisor

# Parte de la vista del modelo MVC.

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from crud_bd import leer_reg_divisor
from crud_bd import actualizar_divisor
from crud_bd import elimina_divisor


class VerDivisor(QDialog):


    def __init__(self, id, ventana: QDialog):

        #ID
        self.id = id

        #Obtiene datos de la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3.65)
        alto = float(size.height() / 4.74)

        #Formulario.
        super().__init__()

        self.frm_ver_divisor = ventana
        self.frm_ver_divisor.setObjectName("self.frm_ver_divisor")
        self.frm_ver_divisor.resize(ancho, alto)
        self.frm_ver_divisor.setMinimumSize(ancho, alto)
        self.frm_ver_divisor.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_ver_divisor.setWindowIcon(icon)
        self.gridLayout = QGridLayout(self.frm_ver_divisor)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_0 = QLabel(self.frm_ver_divisor)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)

        self.txt_legajo = QLineEdit(self.frm_ver_divisor)
        self.txt_legajo.setObjectName("txt_legajo")
        self.gridLayout.addWidget(self.txt_legajo, 0, 1, 1, 1)

        self.line = QFrame(self.frm_ver_divisor)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 5)

        self.lbl_1 = QLabel(self.frm_ver_divisor)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 2, 0, 1, 1)

        self.txt_ann = QLineEdit(self.frm_ver_divisor)
        self.txt_ann.setObjectName("txt_ann")
        self.gridLayout.addWidget(self.txt_ann, 2, 1, 1, 1)

        self.lbl_2 = QLabel(self.frm_ver_divisor)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 2, 2, 1, 1)

        self.txt_mes = QLineEdit(self.frm_ver_divisor)
        self.txt_mes.setObjectName("txt_mes")
        self.gridLayout.addWidget(self.txt_mes, 2, 3, 1, 1)

        self.lbl_3 = QLabel(self.frm_ver_divisor)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 3, 0, 1, 1)

        self.txt_divisor = QLineEdit(self.frm_ver_divisor)
        self.txt_divisor.setObjectName("txt_divisor")
        self.gridLayout.addWidget(self.txt_divisor, 3, 1, 1, 1)

        self.btn_eliminar = QPushButton(self.frm_ver_divisor)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 4, 2, 1, 1)
        self.btn_eliminar.clicked.connect(lambda: self.eliminar())

        self.btn_actualizar = QPushButton(self.frm_ver_divisor)
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.gridLayout.addWidget(self.btn_actualizar, 4, 3, 1, 1)
        self.btn_actualizar.clicked.connect(lambda: self.actualizar())

        self.btn_cerrar = QPushButton(self.frm_ver_divisor)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 4, 4, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_ver_divisor.close())
        

        try:
            lista = list()
            lista = leer_reg_divisor(self.id)
            print(lista)

            self.txt_legajo.insert(str(lista[0]))
            self.txt_legajo.setReadOnly(True)

            self.txt_ann.insert(str(lista[1]))
            
            self.txt_mes.insert(str(lista[2]))

            self.txt_divisor.insert(str(lista[3]))

        except:
            pass

        QtCore.QMetaObject.connectSlotsByName(self.frm_ver_divisor)

        _translate = QtCore.QCoreApplication.translate
        self.frm_ver_divisor.setWindowTitle(_translate("self.frm_ver_divisor", "Divisor"))
        self.lbl_0.setText(_translate("self.frm_ver_divisor", "Legajo:"))
        self.lbl_1.setText(_translate("self.frm_ver_divisor", "Año:"))
        self.lbl_2.setText(_translate("self.frm_ver_divisor", "Mes:"))
        self.lbl_3.setText(_translate("self.frm_ver_divisor", "Divisor:"))
        self.btn_eliminar.setText(_translate("self.frm_ver_divisor", "Eliminar"))
        self.btn_actualizar.setText(_translate("self.frm_ver_divisor", "Actualizar"))
        self.btn_cerrar.setText(_translate("self.frm_ver_divisor", "Cerrar"))


    def actualizar(self):

        try:
            legajo = int(self.txt_legajo.text())
            ann = int(self.txt_ann.text())
            mes = int(self.txt_mes.text())
            divisor = int(self.txt_divisor.text())

            resultado = actualizar_divisor(self.id, legajo, ann, mes, divisor)

            if resultado == True:
    
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se realizó el proceso de actualización correctamente.")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                msg_box.exec()
    
                self.frm_ver_divisor.close()
            else:
    
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Error en el proceso de actualización.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
            
                msg_box.exec()

                self.frm_ver_divisor.close()

        except Exception as error:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()
        

    def eliminar(self):

        try:
            resultado = elimina_divisor(self.id)

            if resultado == True:
            
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se realizó el proceso de actualización correctamente.")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                msg_box.exec()
    
                self.frm_ver_divisor.close()
            
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Error en el proceso de actualización.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
            
                msg_box.exec()
    
                self.frm_ver_divisor.close()

        except Exception as error:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()        






