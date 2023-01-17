#Formulario para visualizar los registros especificos de un empleado seleccionado en el formulario
#visualiza cargas de familia. Asimismo utiliza funciones releacionadas al CRUD de la base de datos.
#Parte de la vista.


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
from crud_bd import visualiza_cfam
from crud_bd import actualiza_cfam
from crud_bd import elimina_cfam

class VerCFam(QDialog):

    def __init__(self, id, ventana: QDialog):

        self.id = id

        datos = visualiza_cfam(self.id)
        
        #Obtiene datos de la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 4.09)
        alto = float(size.height() / 2.76)

        #Formulario
        super().__init__()
        self.frm_cfamilia = ventana
        self.frm_cfamilia.setObjectName("self.frm_cfamilia")
        self.frm_cfamilia.resize(ancho, alto)
        self.gridLayout = QGridLayout(self.frm_cfamilia)
        self.gridLayout.setObjectName("gridLayout")
        self.frm_cfamilia.setMinimumSize(ancho, alto)
        self.frm_cfamilia.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_cfamilia.setWindowIcon(icon) 

        self.lbl_2 = QLabel(self.frm_cfamilia)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 3, 0, 1, 1)

        self.txt_nombre = QLineEdit(self.frm_cfamilia)
        self.txt_nombre.setObjectName("txt_nombre")
        self.gridLayout.addWidget(self.txt_nombre, 4, 2, 1, 6)

        self.lbl_7 = QLabel(self.frm_cfamilia)
        self.lbl_7.setObjectName("lbl_7")
        self.gridLayout.addWidget(self.lbl_7, 7, 0, 1, 2)

        self.lbl_6 = QLabel(self.frm_cfamilia)
        self.lbl_6.setObjectName("lbl_6")
        self.gridLayout.addWidget(self.lbl_6, 6, 0, 1, 3)

        self.lbl_0 = QLabel(self.frm_cfamilia)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 2)

        self.btn_eliminar = QPushButton(self.frm_cfamilia)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 8, 6, 1, 1)
        self.btn_eliminar.clicked.connect(lambda: self.del_cfam())

        self.txt_parentesco = QLineEdit(self.frm_cfamilia)
        self.txt_parentesco.setObjectName("txt_parentesco")
        self.gridLayout.addWidget(self.txt_parentesco, 7, 4, 1, 2)

        self.btn_cerrar = QPushButton(self.frm_cfamilia)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 8, 5, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_cfamilia.close())


        self.line = QFrame(self.frm_cfamilia)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 8)

        self.txt_apellido = QLineEdit(self.frm_cfamilia)
        self.txt_apellido.setObjectName("txt_apellido")
        self.gridLayout.addWidget(self.txt_apellido, 3, 2, 1, 6)

        self.txt_desde = QLineEdit(self.frm_cfamilia)
        self.txt_desde.setObjectName("txt_desde")
        self.gridLayout.addWidget(self.txt_desde, 5, 2, 1, 1)

        self.txt_porcentaje = QLineEdit(self.frm_cfamilia)
        self.txt_porcentaje.setObjectName("txt_porcentaje")
        self.gridLayout.addWidget(self.txt_porcentaje, 6, 4, 1, 2)

        self.txt_cuil = QLineEdit(self.frm_cfamilia)
        self.txt_cuil.setObjectName("txt_cuil")
        self.gridLayout.addWidget(self.txt_cuil, 2, 2, 1, 6)

        self.lbl_1 = QLabel(self.frm_cfamilia)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 2, 0, 1, 2)

        self.txt_legajo = QLineEdit(self.frm_cfamilia)
        self.txt_legajo.setObjectName("txt_legajo")
        self.gridLayout.addWidget(self.txt_legajo, 0, 2, 1, 5)

        self.btn_guardar = QPushButton(self.frm_cfamilia)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout.addWidget(self.btn_guardar, 8, 7, 1, 1)
        self.btn_guardar.clicked.connect(lambda: self.act_cfam())

        self.lbl_3 = QLabel(self.frm_cfamilia)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 4, 0, 1, 1)

        self.lbl_5 = QLabel(self.frm_cfamilia)
        self.lbl_5.setObjectName("lbl_5")
        self.gridLayout.addWidget(self.lbl_5, 5, 5, 1, 1)

        self.lbl_4 = QLabel(self.frm_cfamilia)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 5, 0, 1, 2)

        self.txt_hasta = QLineEdit(self.frm_cfamilia)
        self.txt_hasta.setObjectName("txt_hasta")
        self.gridLayout.addWidget(self.txt_hasta, 5, 6, 1, 1)

        try:
            self.txt_legajo.insert(datos[0])
            self.txt_legajo.setReadOnly(True)
            self.txt_cuil.insert(datos[1])
            self.txt_apellido.insert(datos[2])
            self.txt_nombre.insert(datos[3])
            self.txt_desde.insert(datos[4])
            self.txt_hasta.insert(datos[5])
            self.txt_porcentaje.insert(datos[6])  
            self.txt_parentesco.insert(datos[7])  
        except:
            pass

        QtCore.QMetaObject.connectSlotsByName(self.frm_cfamilia)

        _translate = QtCore.QCoreApplication.translate
        self.frm_cfamilia.setWindowTitle(_translate("self.frm_cfamilia", "Carga de familia"))
        self.lbl_2.setText(_translate("self.frm_cfamilia", "Apellido(s):"))
        self.lbl_7.setText(_translate("self.frm_cfamilia", "Parentesco:"))
        self.lbl_6.setText(_translate("self.frm_cfamilia", "Porcentaje deducción:"))
        self.lbl_0.setText(_translate("self.frm_cfamilia", "Número de legajo:"))
        self.btn_eliminar.setText(_translate("self.frm_cfamilia", "Eliminar"))
        self.btn_cerrar.setText(_translate("self.frm_cfamilia", "Cerrar"))
        self.lbl_1.setText(_translate("self.frm_cfamilia", "CUIL - Documento:"))
        self.btn_guardar.setText(_translate("self.frm_cfamilia", "Guardar"))
        self.lbl_3.setText(_translate("self.frm_cfamilia", "Nombre(s):"))
        self.lbl_5.setText(_translate("self.frm_cfamilia", "Mes hasta:"))
        self.lbl_4.setText(_translate("self.frm_cfamilia", "Mes desde:"))


    def act_cfam(self):
        
        try:
            resultado = actualiza_cfam(self.id, self.txt_cuil.text(), self.txt_apellido.text(),
            self.txt_nombre.text(), self.txt_desde.text(), self.txt_hasta.text(), self.txt_porcentaje.text(),
            self.txt_parentesco.text())

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
                self.frm_cfamilia.close()
        
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

    def del_cfam(self):

        try:
            resultado = elimina_cfam(self.id)

            if resultado == True:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se elimino al empleado de la base de datos.")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                msg_box.exec()

                self.frm_cfamilia.close()

            else:

                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Error en el proceso de actualización.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
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