# Formulario para cargar masivamente los importes para calcular la deduccion incrementada de la segunda parte.
# Parte de la vista del modelo MVC.


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from importacion import lee_rangosegundoparrafo
from importacion import guarda_dedsparrafo
from importacion import borra_dedsparrafo


class CargaMasiva(object):

    def __init__ (self, ventana: QDialog):

        super().__init__()

        #Obtiene resolución de pantalla.
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3.621)
        alto = float(size.height() / 5.81)

        self.frm_importar_dedsparrafo = ventana
        self.frm_importar_dedsparrafo.setObjectName("frm_importar_dedsparrafo")
        self.frm_importar_dedsparrafo.resize(ancho, alto)
        self.frm_importar_dedsparrafo.setMinimumSize(ancho, alto)
        self.frm_importar_dedsparrafo.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_importar_dedsparrafo.setWindowIcon(icon)

        self.gridLayout = QGridLayout(self.frm_importar_dedsparrafo)
        self.gridLayout.setObjectName("gridLayout")

        self.cmb_resolucion = QComboBox(self.frm_importar_dedsparrafo)
        self.cmb_resolucion.setObjectName("comboBox")
        self.gridLayout.addWidget(self.cmb_resolucion, 0, 1, 1, 3)
        self.cmb_resolucion.addItem('Resolución 5008/2021')
        self.cmb_resolucion.addItem('Resolución 5076/2021')
        self.cmb_resolucion.addItem('RIPTE_2022')
        
        self.btn_actualizar = QPushButton(self.frm_importar_dedsparrafo)
        self.btn_actualizar.setMaximumSize(QtCore.QSize(75, 16777215))
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.gridLayout.addWidget(self.btn_actualizar, 2, 3, 1, 1)
        self.btn_actualizar.clicked.connect(lambda: self.ejecuta_actualizacion())

        self.btn_cerrar = QPushButton(self.frm_importar_dedsparrafo)
        self.btn_cerrar.setMaximumSize(QtCore.QSize(75, 16777215))
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 2, 2, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_importar_dedsparrafo.close())

        self.txt_archivo = QLineEdit(self.frm_importar_dedsparrafo)
        self.txt_archivo.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.txt_archivo, 1, 1, 1, 2)

        self.lbl_0 = QLabel(self.frm_importar_dedsparrafo)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)

        self.lbl_1 = QLabel(self.frm_importar_dedsparrafo)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 0, 1, 1)

        self.btn_archivo = QToolButton(self.frm_importar_dedsparrafo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/file-excel-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_archivo.setIcon(icon1)
        self.btn_archivo.setObjectName("btn_archivo")
        self.gridLayout.addWidget(self.btn_archivo, 1, 3, 1, 1)
        self.btn_archivo.clicked.connect(lambda: self.abre_archivo())

        QtCore.QMetaObject.connectSlotsByName(self.frm_importar_dedsparrafo)

        _translate = QtCore.QCoreApplication.translate
        self.frm_importar_dedsparrafo.setWindowTitle(_translate("self.frm_importar_dedsparrafo", "Carga masiva"))
        self.btn_actualizar.setText(_translate("self.frm_importar_dedsparrafo", "Ejecutar"))
        self.btn_cerrar.setText(_translate("self.frm_importar_dedsparrafo", "Cerrar"))
        self.lbl_0.setText(_translate("self.frm_importar_dedsparrafo", "Resolución:"))
        self.lbl_1.setText(_translate("self.frm_importar_dedsparrafo", "Archivo:"))
        self.btn_archivo.setText(_translate("self.frm_importar_dedsparrafo", "..."))


    def abre_archivo(self):

        try:
        
            opcion = QFileDialog.Options()
            file_name = QFileDialog.getOpenFileName(self.frm_importar_dedsparrafo,"Seleccionar archivo", "",
                                                    "Archivos excel (*xlsx);; All Files (*)", options = opcion)
            self.txt_archivo.clear()
            self.txt_archivo.insert(file_name[0])
        
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
            

    def ejecuta_actualizacion(self):

        try:

            registros = list()
            registros = lee_rangosegundoparrafo(self.txt_archivo.text())

            tabla = self.cmb_resolucion.currentText()

            mensaje = f'El siguiente procedimiento borrara todos los registros correspondientes a la {tabla} y actualizara la información. ¿Desea continuar?'
            msg_box = QMessageBox.question(self.frm_importar_dedsparrafo, 'Advertencia', mensaje, QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

            if msg_box == QMessageBox.Yes:
                self.frm_importar_dedsparrafo.setEnabled(False)

                if tabla == 'Resolución 5008/2021':
                    borra_dedsparrafo('RG_5008')
                elif tabla == 'Resolución 5076/2021':
                    borra_dedsparrafo('RG_5076')
                else:
                    borra_dedsparrafo('RIPTE_2022')
            
                for registro in registros.values:
                    guarda_dedsparrafo(registro[0], registro[1], registro[2], registro[3])

                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Finalizo el proceso de importación de datos.")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                msg_box.exec()

                self.frm_importar_dedsparrafo.setEnabled(True)
            
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

            self.frm_importar_dedsparrafo.close()