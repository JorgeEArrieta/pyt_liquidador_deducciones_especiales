# Formulario para ver valores individuales de la segunda parte de la deducción especial incrementada.
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
from crud_bd import registro_dedsegundoparrafo
from crud_bd import actualiza_dedsegundoparrafo
from crud_bd import elimina_dedsegundoparrafo


class VerDedSParte(object):
    def __init__(self, id, ventana: QDialog):
        #Guarda el id para operaciones relacionadas al crud
        self.id = id

        #Obtiene los valores para mostrar en las cajas de texto.
        valores = list()
        valores = registro_dedsegundoparrafo(self.id)

        #Obtiene resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3.07)
        alto = float(size.height() / 5.37)

        #Formulario.
        super().__init__()

        self.frm_deduccion = ventana
        self.frm_deduccion.setObjectName("frm_deduccion")
        self.frm_deduccion.resize(ancho, alto)
        self.frm_deduccion.setMinimumSize(ancho, alto)
        self.frm_deduccion.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_deduccion.setWindowIcon(icon)

        self.gridLayout = QGridLayout(self.frm_deduccion)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_0 = QLabel(self.frm_deduccion)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)

        self.txt_resolucion = QLineEdit(self.frm_deduccion)
        self.txt_resolucion.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.txt_resolucion, 0, 1, 1, 2)

        self.line = QFrame(self.frm_deduccion)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 6)

        self.lbl_1 = QLabel(self.frm_deduccion)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 2, 0, 1, 1)

        self.txt_valmin = QLineEdit(self.frm_deduccion)
        self.txt_valmin.setObjectName("txt_valmin")
        self.gridLayout.addWidget(self.txt_valmin, 2, 1, 1, 1)
        
        self.lbl_2 = QLabel(self.frm_deduccion)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 2, 2, 1, 2)

        self.txt_valmax = QLineEdit(self.frm_deduccion)
        self.txt_valmax.setObjectName("txt_valmax")
        self.gridLayout.addWidget(self.txt_valmax, 2, 4, 1, 2)

        self.lbl_3 = QLabel(self.frm_deduccion)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 3, 0, 1, 1)

        self.txt_deduccion = QLineEdit(self.frm_deduccion)
        self.txt_deduccion.setObjectName("txt_valmin_2")
        self.gridLayout.addWidget(self.txt_deduccion, 3, 1, 1, 1)

        self.btn_eliminar = QPushButton(self.frm_deduccion)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 4, 3, 1, 2)
        self.btn_eliminar.clicked.connect(lambda: self.elimina_registro())

        self.btn_guardar = QPushButton(self.frm_deduccion)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout.addWidget(self.btn_guardar, 4, 5, 1, 1)
        self.btn_guardar.clicked.connect(lambda: self.actualiza_registro())
        
        self.btn_cerrar = QPushButton(self.frm_deduccion)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 4, 2, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_deduccion.close())

        try:
            self.txt_resolucion.insert(valores[0])
            self.txt_resolucion.setReadOnly(True)

            self.txt_valmin.insert(str(valores[1]))
        
            self.txt_valmax.insert(str(valores[2]))

            self.txt_deduccion.insert(str(valores[3]))
        
        except:
            pass

        QtCore.QMetaObject.connectSlotsByName(self.frm_deduccion)

        _translate = QtCore.QCoreApplication.translate
        self.frm_deduccion.setWindowTitle(_translate("self.frm_deduccion", "Deducción"))
        self.lbl_0.setText(_translate("self.frm_deduccion", "Resolución:"))
        self.lbl_1.setText(_translate("self.frm_deduccion", "Valor mínimo:"))
        self.lbl_2.setText(_translate("self.frm_deduccion", "Valor máximo:"))
        self.lbl_3.setText(_translate("self.frm_deduccion", "Deducción:"))
        self.btn_eliminar.setText(_translate("self.frm_deduccion", "Eliminar"))
        self.btn_guardar.setText(_translate("self.frm_deduccion", "Guardar"))
        self.btn_cerrar.setText(_translate("self.frm_deduccion", "Cerrar"))


    def actualiza_registro(self):
        
        try:

            id = int(self.id)
            valor_min = float(self.txt_valmin.text())
            valor_max = float(self.txt_valmax.text())
            deduccion = float(self.txt_deduccion.text())

            query = actualiza_dedsegundoparrafo(id, valor_min, valor_max, deduccion)

            if query == True:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se actualizo el registro de forma correcta.")
                msg_box.setWindowTitle("Informacion")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon)
                msg_box.exec()

                self.frm_deduccion.close()

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
        
        except TypeError:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en formato. Revisar la información ingresada.")
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
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()

    def elimina_registro(self):
    
        try:

            id = int(self.id)

            query = elimina_dedsegundoparrafo(id)
        
            if query == True:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se elimino al registro de forma correcta.")
                msg_box.setWindowTitle("Informacion")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon)
                msg_box.exec()

                self.frm_deduccion.close()
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Error en el proceso.")
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
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()
        