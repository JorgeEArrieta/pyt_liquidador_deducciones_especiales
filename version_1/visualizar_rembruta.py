#Formulario visualizar remuneración bruta.
#Parte de la Vista del modelo MVC.

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QMessageBox
from ver_remuneracion_bruta import VerRemBruta
from crud_bd import lista_empleados
from crud_bd import lect_bbdd_rem_deduc

class VisualizarRemBruta(QDialog):

    def __init__(self, ventana: QDialog):
        
        #Declararción del formulario.
        super().__init__(ventana)
        frm_lista_rembruta = ventana
        frm_lista_rembruta.setObjectName("frm_lista_rembruta")
        frm_lista_rembruta.resize(601, 326)
        frm_lista_rembruta.setMinimumSize(601, 326)
        frm_lista_rembruta.setMaximumSize(601, 326)
        frm_lista_rembruta.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_lista_rembruta.setWindowIcon(icon) 
        
        #Labels.
        self.lbl_0 = QLabel(frm_lista_rembruta)
        self.lbl_0.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.lbl_0.setObjectName("lbl_0")

        self.lbl_1 = QLabel(frm_lista_rembruta)
        self.lbl_1.setGeometry(QtCore.QRect(160, 10, 41, 16))
        self.lbl_1.setObjectName("lbl_1")

        self.lbl_2 = QLabel(frm_lista_rembruta)
        self.lbl_2.setGeometry(QtCore.QRect(310, 10, 41, 16))
        self.lbl_2.setObjectName("lbl_2")

        #Combo box
        self.cmb_legajo = QComboBox(frm_lista_rembruta)
        self.cmb_legajo.setGeometry(QtCore.QRect(60, 10, 81, 22))
        self.cmb_legajo.setObjectName("cmb_legajo")
        self.cmb_legajo.addItem('*')

        try:
            empleados = lista_empleados()

            for empleado in empleados:
                self.cmb_legajo.addItem(str(empleado))

        except:
            pass

        self.cmb_year = QComboBox(frm_lista_rembruta)
        self.cmb_year.setGeometry(QtCore.QRect(200, 10, 81, 22))
        self.cmb_year.setObjectName("cmb_year")
        self.cmb_year.addItem('*')
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')

        self.cmb_mes = QComboBox(frm_lista_rembruta)
        self.cmb_mes.setGeometry(QtCore.QRect(350, 10, 81, 22))
        self.cmb_mes.setObjectName("cmb_mes")
        self.cmb_mes.addItem('*')

        i = 1

        while i <= 12:
            self.cmb_mes.addItem(str(i))
            i += 1

        #Declaración del treeview
        self.tw_empleados = QTableWidget(frm_lista_rembruta)
        self.tw_empleados.setGeometry(QtCore.QRect(10, 50, 581, 231))
        self.tw_empleados.setObjectName("tw_empleados")
        
        #Se establece la tabla como no editable y que no se permita el drag & drop
        self.tw_empleados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_empleados.setDragDropOverwriteMode(False)

        #Modo de selección de datos.
        self.tw_empleados.setSelectionMode(QAbstractItemView.SingleSelection)

        #Declaración de los botones del formulario.
        self.btn_cerrar = QPushButton(frm_lista_rembruta, clicked= frm_lista_rembruta.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(520, 290, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")
        
        self.btn_ver = QPushButton(frm_lista_rembruta, clicked = self.ver_rembruta)
        self.btn_ver.setGeometry(QtCore.QRect(440, 290, 75, 23))
        self.btn_ver.setObjectName("btn_ver")

        self.btn_visualiza = QPushButton(frm_lista_rembruta, clicked = self.on_cmb_click)
        self.btn_visualiza.setGeometry(QtCore.QRect(360, 290, 75, 23))
        self.btn_visualiza.setObjectName("btn_visualiza")

        
        QtCore.QMetaObject.connectSlotsByName(frm_lista_rembruta)

        _translate = QtCore.QCoreApplication.translate
        frm_lista_rembruta.setWindowTitle(_translate("frm_lista_rembruta", "Listado de remuneraciones brutas"))
        self.lbl_0.setText(_translate("frm_lista_rembruta", "Legajo:"))
        self.lbl_1.setText(_translate("frm_lista_rembruta", "Año:"))
        self.lbl_2.setText(_translate("frm_lista_rembruta", "Mes:"))
        self.btn_cerrar.setText(_translate("frm_lista_rembruta", "Cerrar"))
        self.btn_ver.setText(_translate("frm_lista_rembruta", "Ver"))
        self.btn_visualiza.setText(_translate("frm_lista_rembruta", "Actualizar"))
        
        #Actualización del treeview.
        legajo = list()
        legajo.append('*')
        
        month = list()
        month.append('*')
        
        year = list()
        year.append('*')

        self.actualiza_treeview('remu', legajo, month, year)

        #Eventos.
        self.cmb_legajo.currentIndexChanged.connect(self.on_cmb_click)
        self.cmb_mes.currentIndexChanged.connect(self.on_cmb_click)
        self.cmb_year.currentIndexChanged.connect(self.on_cmb_click)


    def actualiza_treeview(self, tabla: str, legajo: list, month: list, year: list):

        try:
            listado = lect_bbdd_rem_deduc(tabla, legajo, month, year)

            self.tw_empleados.setColumnCount(5)
            self.tw_empleados.setRowCount(0)

            #Definición de las columnas.
            item_legajo = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(0, item_legajo)
            item_ann = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(1, item_ann)
            item_nomap = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(2, item_nomap)
            item_mes = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(3, item_mes)
            item_importe = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(4, item_importe)

            _translate = QtCore.QCoreApplication.translate

            #Titúlos de las columnas del treeview
            item_legajo.setText(_translate("frm_lista_rembruta", "Número de legajo"))
            item_legajo = self.tw_empleados.horizontalHeaderItem(0)
            item_nomap.setText(_translate("frm_lista_rembruta", "Nombre y apellido"))
            item_nomap = self.tw_empleados.horizontalHeaderItem(1)
            item_ann.setText(_translate("frm_lista_rembruta", "Año"))
            item_ann = self.tw_empleados.horizontalHeaderItem(2)
            item_mes.setText(_translate("frm_lista_rembruta", "Mes"))
            item_mes = self.tw_empleados.horizontalHeaderItem(3)
            item_importe.setText(_translate("frm_lista_rembruta", "Importe"))
            item_importe = self.tw_empleados.horizontalHeaderItem(4)

            for lista in listado:
    
                position = self.tw_empleados.rowCount()
                self.tw_empleados.insertRow(position)          
                y = 0
    
                for n in lista:
                    valor = str(n)
                    self.tw_empleados.setItem(position, y, QTableWidgetItem(valor))
                    y += 1  

        except TypeError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en base de datos.")
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
        

    def on_cmb_click(self):
        
        try:
            legajo = list()
            legajo.append(self.cmb_legajo.currentText())
        
            month = list()
            month.append(self.cmb_mes.currentText())
        
            year = list()
            year.append(self.cmb_year.currentText())

            self.actualiza_treeview('remu', legajo, month, year)

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

    def registro_actual(self):

        """
        Obtiene el legajo del widget QTableWidget.
        """
    
        try:
            
            row = self.tw_empleados.currentRow()
            
            legajo = self.tw_empleados.item(row, 0).text()
            year = self.tw_empleados.item(row, 2).text()
            
            return legajo, year
        
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Falta seleccionar un registro.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()


    def ver_rembruta(self):

        """
        Abre un formulario con los datos del legajo seleccionado.
        """
        
        try:
            legajo = self.registro_actual()

            if legajo != None:
                frm_dialog = QDialog()
                VerRemBruta(legajo[0], legajo[1], frm_dialog)
                frm_dialog.exec_()

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