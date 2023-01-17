#Formulario para visualizar los registros especificos de un empleado seleccionado en el formulario
#"visualizar_otros_empleos.py". Asimismo utiliza funciones releacionadas al CRUD de la base de datos.

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
from crud_bd import visualiza_ganoe
from crud_bd import actualiza_ganoe
from crud_bd import elimina_ganoe


class VerGananOE(QDialog):
    
    def __init__(self, id, ventana: QDialog):

        self.id = id

        datos = visualiza_ganoe(self.id)

        #Obtiene datos de la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 2.214)
        alto = float(size.height() / 2.31)

        #Formulario.
        super().__init__()

        self.frm_ganan_oe = ventana
        self.frm_ganan_oe.setObjectName("self.frm_ganan_oe")
        self.frm_ganan_oe.resize(ancho, alto)
        self.frm_ganan_oe.setMinimumSize(ancho, alto)
        self.frm_ganan_oe.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_ganan_oe.setWindowIcon(icon) 
        
        self.gridLayout = QGridLayout(self.frm_ganan_oe)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_3 = QLabel(self.frm_ganan_oe)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 5, 1, 1, 1)

        self.lbl_2 = QLabel(self.frm_ganan_oe)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_2.setFont(font)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 4, 0, 1, 2)

        self.txt_hsexentas = QLineEdit(self.frm_ganan_oe)
        self.txt_hsexentas.setObjectName("txt_hsexentas")
        self.gridLayout.addWidget(self.txt_hsexentas, 7, 5, 1, 2)

        self.txt_segsoc = QLineEdit(self.frm_ganan_oe)
        self.txt_segsoc.setObjectName("txt_segsoc")
        self.gridLayout.addWidget(self.txt_segsoc, 10, 5, 1, 2)

        self.txt_legajo = QLineEdit(self.frm_ganan_oe)
        self.txt_legajo.setObjectName("txt_legajo")
        self.gridLayout.addWidget(self.txt_legajo, 0, 2, 1, 2)

        self.lbl_4 = QLabel(self.frm_ganan_oe)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 5, 4, 1, 1)

        self.lbl_1 = QLabel(self.frm_ganan_oe)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 2, 0, 1, 1)

        self.line = QFrame(self.frm_ganan_oe)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 7)

        self.txt_empleador = QLineEdit(self.frm_ganan_oe)
        self.txt_empleador.setObjectName("txt_empleador")
        self.gridLayout.addWidget(self.txt_empleador, 2, 3, 1, 2)

        self.txt_obrasoc = QLineEdit(self.frm_ganan_oe)
        self.txt_obrasoc.setObjectName("txt_obrasoc")
        self.gridLayout.addWidget(self.txt_obrasoc, 10, 2, 1, 2)

        self.txt_sindicato = QLineEdit(self.frm_ganan_oe)
        self.txt_sindicato.setObjectName("txt_sindicato")
        self.gridLayout.addWidget(self.txt_sindicato, 11, 2, 1, 2)

        self.lbl_15 = QLabel(self.frm_ganan_oe)
        self.lbl_15.setObjectName("lbl_15")
        self.gridLayout.addWidget(self.lbl_15, 2, 2, 1, 1)

        self.txt_hsgrav = QLineEdit(self.frm_ganan_oe)
        self.txt_hsgrav.setObjectName("txt_hsgrav")
        self.gridLayout.addWidget(self.txt_hsgrav, 7, 2, 1, 2)
        
        self.lbl_0 = QLabel(self.frm_ganan_oe)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 2)

        self.lbl_6 = QLabel(self.frm_ganan_oe)
        self.lbl_6.setObjectName("lbl_6")
        self.gridLayout.addWidget(self.lbl_6, 6, 4, 1, 1)

        self.lbl_9 = QLabel(self.frm_ganan_oe)
        self.lbl_9.setObjectName("lbl_9")
        self.gridLayout.addWidget(self.lbl_9, 8, 1, 1, 1)

        self.lbl_12 = QLabel(self.frm_ganan_oe)
        self.lbl_12.setObjectName("lbl_12")
        self.gridLayout.addWidget(self.lbl_12, 10, 1, 1, 1)

        self.lbl_13 = QLabel(self.frm_ganan_oe)
        self.lbl_13.setObjectName("lbl_13")
        self.gridLayout.addWidget(self.lbl_13, 10, 4, 1, 1)

        self.txt_gananbruta = QLineEdit(self.frm_ganan_oe)
        self.txt_gananbruta.setObjectName("txt_gananbruta")
        self.gridLayout.addWidget(self.txt_gananbruta, 5, 2, 1, 2)

        self.lbl_7 = QLabel(self.frm_ganan_oe)
        self.lbl_7.setObjectName("lbl_7")
        self.gridLayout.addWidget(self.lbl_7, 7, 1, 1, 1)

        self.lbl_14 = QLabel(self.frm_ganan_oe)
        self.lbl_14.setObjectName("lbl_14")
        self.gridLayout.addWidget(self.lbl_14, 11, 1, 1, 1)

        self.txt_mes = QLineEdit(self.frm_ganan_oe)
        self.txt_mes.setObjectName("txt_mes")
        self.gridLayout.addWidget(self.txt_mes, 2, 1, 1, 1)

        self.txt_viamov = QLineEdit(self.frm_ganan_oe)
        self.txt_viamov.setObjectName("txt_viamov")
        self.gridLayout.addWidget(self.txt_viamov, 8, 5, 1, 2)

        self.txt_ajuste = QLineEdit(self.frm_ganan_oe)
        self.txt_ajuste.setObjectName("txt_ajuste")
        self.gridLayout.addWidget(self.txt_ajuste, 6, 2, 1, 2)

        self.txt_retnohab = QLineEdit(self.frm_ganan_oe)
        self.txt_retnohab.setObjectName("txt_retnohab")
        self.gridLayout.addWidget(self.txt_retnohab, 5, 5, 1, 2)

        self.btn_eliminar = QPushButton(self.frm_ganan_oe)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 12, 5, 1, 1)
        self.btn_eliminar.clicked.connect(lambda: self.elim_ganoe())

        self.lbl_11 = QLabel(self.frm_ganan_oe)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_11.setFont(font)
        self.lbl_11.setObjectName("lbl_11")
        self.gridLayout.addWidget(self.lbl_11, 9, 0, 1, 2)

        self.lbl_8 = QLabel(self.frm_ganan_oe)
        self.lbl_8.setObjectName("lbl_8")
        self.gridLayout.addWidget(self.lbl_8, 7, 4, 1, 1)

        self.lbl_5 = QLabel(self.frm_ganan_oe)
        self.lbl_5.setObjectName("lbl_5")
        self.gridLayout.addWidget(self.lbl_5, 6, 1, 1, 1)

        self.line_2 = QFrame(self.frm_ganan_oe)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 7)

        self.btn_guardar = QPushButton(self.frm_ganan_oe)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout.addWidget(self.btn_guardar, 12, 6, 1, 1)
        self.btn_guardar.clicked.connect(lambda: self.act_ganoe())

        self.txt_remexenta = QLineEdit(self.frm_ganan_oe)
        self.txt_remexenta.setObjectName("txt_remexenta")
        self.gridLayout.addWidget(self.txt_remexenta, 6, 5, 1, 2)

        self.txt_matdidac = QLineEdit(self.frm_ganan_oe)
        self.txt_matdidac.setObjectName("txt_matdidac")
        self.gridLayout.addWidget(self.txt_matdidac, 8, 2, 1, 2)

        self.lbl_10 = QLabel(self.frm_ganan_oe)
        self.lbl_10.setObjectName("lbl_10")
        self.gridLayout.addWidget(self.lbl_10, 8, 4, 1, 1)

        try:
            self.txt_legajo.insert(datos[0])
            self.txt_legajo.setReadOnly(True)
            self.txt_empleador.insert(datos[1])
            self.txt_mes.insert(datos[2])
            self.txt_gananbruta.insert(datos[3])
            self.txt_retnohab.insert(datos[4])
            self.txt_ajuste.insert(datos[5])
            self.txt_remexenta.insert(datos[6])
            self.txt_hsgrav.insert(datos[7])
            self.txt_hsexentas.insert(datos[8])
            self.txt_matdidac.insert(datos[9])
            self.txt_viamov.insert(datos[10])
            self.txt_obrasoc.insert(datos[11])
            self.txt_segsoc.insert(datos[12])
            self.txt_sindicato.insert(datos[13])
        except:
            pass

        QtCore.QMetaObject.connectSlotsByName(self.frm_ganan_oe)

        _translate = QtCore.QCoreApplication.translate
        self.frm_ganan_oe.setWindowTitle(_translate("self.frm_ganan_oe", "Ganancias otros empleos"))
        self.lbl_3.setText(_translate("self.frm_ganan_oe", "Ganancia bruta:"))
        self.lbl_2.setText(_translate("self.frm_ganan_oe", "Remuneraciones:"))
        self.lbl_4.setText(_translate("self.frm_ganan_oe", "Retribuciones no habituales:"))
        self.lbl_1.setText(_translate("self.frm_ganan_oe", "Mes:"))
        self.lbl_15.setText(_translate("self.frm_ganan_oe", "Empleador:"))
        self.lbl_0.setText(_translate("self.frm_ganan_oe", "Número de legajo:"))
        self.lbl_6.setText(_translate("self.frm_ganan_oe", "Remuneración exenta:"))
        self.lbl_9.setText(_translate("self.frm_ganan_oe", "Material didactico:"))
        self.lbl_12.setText(_translate("self.frm_ganan_oe", "Obra social:"))
        self.lbl_13.setText(_translate("self.frm_ganan_oe", "Seguridad social:"))
        self.lbl_7.setText(_translate("self.frm_ganan_oe", "Hs. ext. gravadas:"))
        self.lbl_14.setText(_translate("self.frm_ganan_oe", "Sindicato:"))
        self.btn_eliminar.setText(_translate("self.frm_ganan_oe", "Eliminar"))
        self.lbl_11.setText(_translate("self.frm_ganan_oe", "Deducciones:"))
        self.lbl_8.setText(_translate("self.frm_ganan_oe", "Hs. ext. exentas:"))
        self.lbl_5.setText(_translate("self.frm_ganan_oe", "Ajustes:"))
        self.btn_guardar.setText(_translate("self.frm_ganan_oe", "Guardar"))
        self.lbl_10.setText(_translate("self.frm_ganan_oe", "Viaticos y movilidad:"))


    def act_ganoe(self):

        try:
            resultado = actualiza_ganoe(self.id, self.txt_empleador.text(), self.txt_gananbruta.text(),
            self.txt_retnohab.text(), self.txt_ajuste.text(), self.txt_remexenta.text(), self.txt_hsgrav.text(),
            self.txt_hsexentas.text(), self.txt_matdidac.text(), self.txt_viamov.text(), self.txt_obrasoc.text(),
            self.txt_segsoc.text(), self.txt_sindicato.text())

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
                self.frm_ganan_oe.close()

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

            self.frm_ganan_oe.close()

    def elim_ganoe(self):

        try:

            resultado = elimina_ganoe(self.id)

            if resultado == True:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se elimino el registro de la base de datos.")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                msg_box.exec()
                self.frm_ganan_oe.close()

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