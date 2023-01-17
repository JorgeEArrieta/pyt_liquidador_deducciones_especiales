#Formulario para visualizar los registros especificos de un empleado seleccionado en el formulario
#visualiza empleado. Asimismo utiliza funciones releacionadas al CRUD de la base de datos.
#Parte de la vista.


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from crud_bd import visualiza_empleado
from crud_bd import actualiza_empleado
from crud_bd import elimina_empleado

class VerEmpleado(QDialog):
    
    def __init__(self, legajo, ventana: QDialog):

        #Valores del empleado
        empleado = visualiza_empleado(legajo)

        #Obtiene datos de la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 4.17)
        alto = float(size.height() / 4.29)

        #Formulario
        super().__init__()

        self.frm_empleado = ventana
        self.frm_empleado.setObjectName("self.frm_empleado")
        self.frm_empleado.resize(ancho, alto)
        self.gridLayout = QGridLayout(self.frm_empleado)
        self.gridLayout.setObjectName("gridLayout")
        self.frm_empleado.setMinimumSize(ancho, alto)
        self.frm_empleado.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_empleado.setWindowIcon(icon) 


        self.lbl_0 = QLabel(self.frm_empleado)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)

        self.txt_legajo = QLineEdit(self.frm_empleado)
        self.txt_legajo.setObjectName("txt_legajo")
        self.gridLayout.addWidget(self.txt_legajo, 0, 1, 1, 2)

        self.lbl_1 = QLabel(self.frm_empleado)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 0, 1, 1)

        self.txt_cuil = QLineEdit(self.frm_empleado)
        self.txt_cuil.setObjectName("txt_cuil")
        self.gridLayout.addWidget(self.txt_cuil, 1, 1, 1, 2)

        self.lbl_2 = QLabel(self.frm_empleado)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 2, 0, 1, 1)

        self.txt_name = QLineEdit(self.frm_empleado)
        self.txt_name.setObjectName("txt_name")
        self.gridLayout.addWidget(self.txt_name, 2, 1, 1, 2)

        self.lbl_4 = QLabel(self.frm_empleado)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 3, 0, 1, 1)

        self.txt_fecing = QLineEdit(self.frm_empleado)
        self.txt_fecing.setObjectName("txt_fecing")
        self.gridLayout.addWidget(self.txt_fecing, 3, 1, 1, 2)

        self.btn_cerrar = QPushButton(self.frm_empleado)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 4, 0, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_empleado.close())

        self.btn_eliminar = QPushButton(self.frm_empleado)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 4, 1, 1, 1)
        self.btn_eliminar.clicked.connect(lambda: self.del_empleado())

        self.btn_guardar = QPushButton(self.frm_empleado)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout.addWidget(self.btn_guardar, 4, 2, 1, 1)
        self.btn_guardar.clicked.connect(lambda: self.act_empleado())

        try:
            self.txt_legajo.insert(str(empleado[0]))
            self.txt_legajo.setReadOnly(True)

            self.txt_cuil.insert(str(empleado[1]))

            self.txt_name.insert(str(empleado[2]))
            
            self.txt_fecing.insert(str(empleado[3]))

        except:
            pass

        QtCore.QMetaObject.connectSlotsByName(self.frm_empleado)

        _translate = QtCore.QCoreApplication.translate
        self.frm_empleado.setWindowTitle(_translate("self.frm_empleado", "Empleado"))
        self.lbl_0.setText(_translate("self.frm_empleado", "Número de legajo:"))
        self.lbl_1.setText(_translate("self.frm_empleado", "CUIL:"))
        self.lbl_2.setText(_translate("self.frm_empleado", "Nombre y Apellido:"))
        self.lbl_4.setText(_translate("self.frm_empleado", "Fecha de ingreso:"))
        self.btn_cerrar.setText(_translate("self.frm_empleado", "Cerrar"))
        self.btn_eliminar.setText(_translate("self.frm_empleado", "Eliminar"))
        self.btn_guardar.setText(_translate("self.frm_empleado", "Guardar"))


    def act_empleado(self):

        """
        Llama al procedimiento para actualizar el registro seleccionado. Si el procediemiento es true, 
        ejecuta un QMessageBox dando aviso al usuario y cierra el formulario. 
        """
        try:

            resultado = actualiza_empleado(self.txt_legajo.text(), self.txt_cuil.text(),
                        self.txt_name.text(), self.txt_fecing.text())

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

                self.frm_empleado.close()

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

    def del_empleado(self):
        
        """
        Llama al procedimiento para actualizar el registro seleccionado. Si el procediemiento es true, 
        ejecuta un QMessageBox dando aviso al usuario y cierra el formulario. 
        """

        try:

            resultado = elimina_empleado(self.txt_legajo.text())
        
            if resultado == True:
        
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se elimino al empleado de la base de datos.")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                msg_box.exec()

                self.frm_empleado.close()

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