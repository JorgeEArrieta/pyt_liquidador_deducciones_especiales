#Formulario para visualizar los registros especificos de un empleado seleccionado en el formulario
#visualiza deducciones. Asimismo utiliza funciones releacionadas al CRUD de la base de datos.
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
from crud_bd import visualiza_deducciones
from crud_bd import actualiza_deducciones
from crud_bd import elimina_deducciones

class VerDeducciones(QDialog):

    def __init__(self, legajo, year, ventana: QDialog):

        self.legajo = legajo
        self.year = year

        #Obtiene datos de la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3.1099)
        alto = float(size.height() / 2.751)
        
        #Formulario
        super().__init__(ventana)

        self.frm_deducciones = ventana
        self.frm_deducciones.setObjectName("self.frm_deducciones")
        self.frm_deducciones.resize(ancho, alto)
        self.frm_deducciones.setMinimumSize(ancho, alto)
        self.frm_deducciones.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_deducciones.setWindowIcon(icon) 
        
        self.gridLayout = QGridLayout(self.frm_deducciones)
        self.gridLayout.setObjectName("gridLayout")

        self.txt_agosto = QLineEdit(self.frm_deducciones)
        self.txt_agosto.setObjectName("txt_agosto")
        self.gridLayout.addWidget(self.txt_agosto, 3, 6, 1, 1)
        self.txt_agosto.insert(str(visualiza_deducciones(legajo, 8)))

        self.lbl_2 = QLabel(self.frm_deducciones)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 3, 0, 1, 1)

        self.lbl_11 = QLabel(self.frm_deducciones)
        self.lbl_11.setMinimumSize(QtCore.QSize(61, 16))
        self.lbl_11.setMaximumSize(QtCore.QSize(61, 16))
        self.lbl_11.setObjectName("lbl_11")
        self.gridLayout.addWidget(self.lbl_11, 6, 5, 1, 1)

        self.txt_marzo = QLineEdit(self.frm_deducciones)
        self.txt_marzo.setObjectName("txt_marzo")
        self.gridLayout.addWidget(self.txt_marzo, 4, 1, 1, 2)
        self.txt_marzo.insert(str(visualiza_deducciones(legajo, 3)))

        self.btn_cerrar = QPushButton(self.frm_deducciones)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 8, 4, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_deducciones.close())

        self.txt_enero = QLineEdit(self.frm_deducciones)
        self.txt_enero.setObjectName("txt_enero")
        self.gridLayout.addWidget(self.txt_enero, 2, 1, 1, 2)
        self.txt_enero.insert(str(visualiza_deducciones(legajo, 1)))
        
        self.txt_julio = QLineEdit(self.frm_deducciones)
        self.txt_julio.setObjectName("txt_julio")
        self.gridLayout.addWidget(self.txt_julio, 2, 6, 1, 1)
        self.txt_julio.insert(str(visualiza_deducciones(legajo, 7)))

        self.txt_septiembre = QLineEdit(self.frm_deducciones)
        self.txt_septiembre.setObjectName("txt_septiembre")
        self.gridLayout.addWidget(self.txt_septiembre, 4, 6, 1, 1)
        self.txt_septiembre.insert(str(visualiza_deducciones(legajo, 9)))

        self.lbl_12 = QLabel(self.frm_deducciones)
        self.lbl_12.setObjectName("lbl_12")
        self.gridLayout.addWidget(self.lbl_12, 7, 5, 1, 1)

        self.lbl_6 = QLabel(self.frm_deducciones)
        self.lbl_6.setObjectName("lbl_6")
        self.gridLayout.addWidget(self.lbl_6, 7, 0, 1, 1)

        self.txt_noviembre = QLineEdit(self.frm_deducciones)
        self.txt_noviembre.setObjectName("txt_noviembre")
        self.gridLayout.addWidget(self.txt_noviembre, 6, 6, 1, 1)
        self.txt_noviembre.insert(str(visualiza_deducciones(legajo, 11)))

        self.txt_mayo = QLineEdit(self.frm_deducciones)
        self.txt_mayo.setObjectName("txt_mayo")
        self.gridLayout.addWidget(self.txt_mayo, 6, 1, 1, 2)
        self.txt_mayo.insert(str(visualiza_deducciones(legajo, 5)))

        self.txt_octubre = QLineEdit(self.frm_deducciones)
        self.txt_octubre.setObjectName("txt_octubre")
        self.gridLayout.addWidget(self.txt_octubre, 5, 6, 1, 1)
        self.txt_octubre.insert(str(visualiza_deducciones(legajo, 10)))

        self.txt_febrero = QLineEdit(self.frm_deducciones)
        self.txt_febrero.setObjectName("txt_febrero")
        self.gridLayout.addWidget(self.txt_febrero, 3, 1, 1, 2)
        self.txt_febrero.insert(str(visualiza_deducciones(legajo, 2)))

        self.lbl_10 = QLabel(self.frm_deducciones)
        self.lbl_10.setObjectName("lbl_10")
        self.gridLayout.addWidget(self.lbl_10, 5, 5, 1, 1)

        self.lbl_1 = QLabel(self.frm_deducciones)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 2, 0, 1, 1)

        self.txt_diciembre = QLineEdit(self.frm_deducciones)
        self.txt_diciembre.setObjectName("txt_diciembre")
        self.gridLayout.addWidget(self.txt_diciembre, 7, 6, 1, 1)
        self.txt_diciembre.insert(str(visualiza_deducciones(legajo, 12)))

        self.lbl_8 = QLabel(self.frm_deducciones)
        self.lbl_8.setObjectName("lbl_8")
        self.gridLayout.addWidget(self.lbl_8, 3, 5, 1, 1)

        self.lbl_9 = QLabel(self.frm_deducciones)
        self.lbl_9.setObjectName("lbl_9")
        self.gridLayout.addWidget(self.lbl_9, 4, 5, 1, 1)

        self.txt_junio = QLineEdit(self.frm_deducciones)
        self.txt_junio.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.txt_junio, 7, 1, 1, 2)
        self.txt_junio.insert(str(visualiza_deducciones(legajo, 6)))

        self.txt_abril = QLineEdit(self.frm_deducciones)
        self.txt_abril.setObjectName("txt_abril")
        self.gridLayout.addWidget(self.txt_abril, 5, 1, 1, 2)
        self.txt_abril.insert(str(visualiza_deducciones(legajo, 4)))

        self.btn_eliminar = QPushButton(self.frm_deducciones)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 8, 5, 1, 1)
        self.btn_eliminar.clicked.connect(lambda: self.del_deduc())

        self.lbl_5 = QLabel(self.frm_deducciones)
        self.lbl_5.setObjectName("lbl_5")
        self.gridLayout.addWidget(self.lbl_5, 6, 0, 1, 1)

        self.lbl_4 = QLabel(self.frm_deducciones)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 5, 0, 1, 1)

        self.lbl_7 = QLabel(self.frm_deducciones)
        self.lbl_7.setObjectName("lbl_7")
        self.gridLayout.addWidget(self.lbl_7, 2, 5, 1, 1)

        self.lbl_3 = QLabel(self.frm_deducciones)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 4, 0, 1, 1)

        self.lbl_0 = QLabel(self.frm_deducciones)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 2)

        self.line = QFrame(self.frm_deducciones)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 7)

        self.btn_guardar = QPushButton(self.frm_deducciones)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout.addWidget(self.btn_guardar, 8, 6, 1, 1)
        self.btn_guardar.clicked.connect(lambda: self.act_deduc())

        self.txt_legajo = QLineEdit(self.frm_deducciones)
        self.txt_legajo.setObjectName("txt_legajo")
        self.gridLayout.addWidget(self.txt_legajo, 0, 2, 1, 2)
        self.txt_legajo.insert(str(legajo))
        self.txt_legajo.setReadOnly(True)

        QtCore.QMetaObject.connectSlotsByName(self.frm_deducciones)

        _translate = QtCore.QCoreApplication.translate
        self.frm_deducciones.setWindowTitle(_translate("self.frm_deducciones", "Deducciones"))
        self.lbl_2.setText(_translate("self.frm_deducciones", "Febrero:"))
        self.lbl_11.setText(_translate("self.frm_deducciones", "Noviembre:"))
        self.btn_cerrar.setText(_translate("self.frm_deducciones", "Cerrar"))
        self.lbl_12.setText(_translate("self.frm_deducciones", "Diciembre:"))
        self.lbl_6.setText(_translate("self.frm_deducciones", "Junio:"))
        self.lbl_10.setText(_translate("self.frm_deducciones", "Octubre:"))
        self.lbl_1.setText(_translate("self.frm_deducciones", "Enero:"))
        self.lbl_8.setText(_translate("self.frm_deducciones", "Agosto:"))
        self.lbl_9.setText(_translate("self.frm_deducciones", "Septiembre:"))
        self.btn_eliminar.setText(_translate("self.frm_deducciones", "Eliminar"))
        self.lbl_5.setText(_translate("self.frm_deducciones", "Mayo:"))
        self.lbl_4.setText(_translate("self.frm_deducciones", "Abril:"))
        self.lbl_7.setText(_translate("self.frm_deducciones", "Julio:"))
        self.lbl_3.setText(_translate("self.frm_deducciones", "Marzo:"))
        self.lbl_0.setText(_translate("self.frm_deducciones", "Número de legajo:"))
        self.btn_guardar.setText(_translate("self.frm_deducciones", "Guardar"))


    def act_deduc(self):
        
        """
        Llama al procedimiento para actualizar el registro seleccionado. Si el procediemiento es true, 
        ejecuta un QMessageBox dando aviso al usuario y cierra el formulario. 
        """

        try:
            array_resultado = list()
    
            if self.txt_enero.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '1', self.year, self.txt_enero.text()))
            if self.txt_febrero.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '2', self.year, self.txt_febrero.text()))
            if self.txt_marzo.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '3', self.year, self.txt_marzo.text()))
            if self.txt_abril.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '4', self.year, self.txt_abril.text()))
            if self.txt_mayo.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '5', self.year, self.txt_mayo.text()))
            if self.txt_junio.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '6', self.year, self.txt_junio.text()))
            if self.txt_julio.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '7', self.year, self.txt_julio.text()))
            if self.txt_agosto.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '8', self.year, self.txt_agosto.text()))
            if self.txt_septiembre.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '9', self.year, self.txt_septiembre.text()))
            if self.txt_octubre.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '10', self.year, self.txt_octubre.text()))
            if self.txt_noviembre.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '11', self.year, self.txt_noviembre.text()))
            if self.txt_diciembre.text() > '0':
                array_resultado.append(actualiza_deducciones(self.legajo, '12', self.year, self.txt_diciembre.text()))
    
            resultado = True
        
            for i in array_resultado:
                if i == False:
                    resultado = False
                    break
        
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
                self.frm_deducciones.close()
    
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Error en el proceso de actualización.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                #msg_box.buttonClicked.connect(msgButtonClick)
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


    def del_deduc(self):
    
        """
        Llama al procedimiento para actualizar el registro seleccionado. Si el procediemiento es true, 
        ejecuta un QMessageBox dando aviso al usuario y cierra el formulario. 
        """

        try:
            mensaje = f'El siguiente procedimiento borrará todas las deducciones del empleado {self.legajo}. ¿Desea continuar?'
            msg_box = QMessageBox.question(self.frm_deducciones, 'Advertencia', mensaje, QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

            if msg_box == QMessageBox.Yes:
                resultado = elimina_deducciones(self.legajo, self.year)

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
                    self.frm_deducciones.close()
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