#Formulario visualizar los registros pertenecientes a ganancias de otros empleos
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
from ver_ganancias_oe import VerGananOE
from crud_bd import lista_empleados
from crud_bd import lectura_remoe

class VisualizaOEmp(QDialog):

    def __init__(self, ventana: QDialog):
        
        #Declararción del formulario.
        super().__init__(ventana)
        frm_lista_remoe = ventana
        frm_lista_remoe.setObjectName("frm_lista_remoe")
        frm_lista_remoe.resize(601, 326)
        frm_lista_remoe.setMinimumSize(601, 326)
        frm_lista_remoe.setMaximumSize(601, 326)
        frm_lista_remoe.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_lista_remoe.setWindowIcon(icon) 
        
        #Labels.
        self.lbl_0 = QLabel(frm_lista_remoe)
        self.lbl_0.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.lbl_0.setObjectName("lbl_0")

        self.lbl_1 = QLabel(frm_lista_remoe)
        self.lbl_1.setGeometry(QtCore.QRect(170, 10, 41, 16))
        self.lbl_1.setObjectName("lbl_1")

        self.lbl_2 = QLabel(frm_lista_remoe)
        self.lbl_2.setGeometry(QtCore.QRect(320, 10, 41, 16))
        self.lbl_2.setObjectName("lbl_2")

        #Combo Box.
        self.cmb_legajo = QComboBox(frm_lista_remoe)
        self.cmb_legajo.setGeometry(QtCore.QRect(60, 10, 81, 22))
        self.cmb_legajo.setObjectName("cmb_legajo")
        self.cmb_legajo.addItem('*')

        try:
            empleados = lista_empleados()

            for empleado in empleados:
                self.cmb_legajo.addItem(str(empleado))

        except:
            pass

        self.cmb_year = QComboBox(frm_lista_remoe)
        self.cmb_year.setGeometry(QtCore.QRect(210, 10, 81, 22))
        self.cmb_year.setObjectName("cmb_year")
        self.cmb_year.addItem('*')
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')

        self.cmb_mes = QComboBox(frm_lista_remoe)
        self.cmb_mes.setGeometry(QtCore.QRect(360, 10, 81, 22))
        self.cmb_mes.setObjectName("cmb_mes")
        self.cmb_mes.addItem('*')

        i = 1

        while i <= 12:
            self.cmb_mes.addItem(str(i))
            i += 1

        #Declaración del treeview
        self.tw_empleados = QTableWidget(frm_lista_remoe)
        self.tw_empleados.setGeometry(QtCore.QRect(10, 50, 581, 231))
        self.tw_empleados.setObjectName("tw_empleados")
        self.tw_empleados.setColumnCount(16)
        self.tw_empleados.setRowCount(0)

        #Se establece la tabla como no editable y que no se permita el drag & drop
        self.tw_empleados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_empleados.setDragDropOverwriteMode(False)

        #Modo de selección de datos.
        self.tw_empleados.setSelectionMode(QAbstractItemView.SingleSelection)
                                                                        
        #Declaración de los botones del formulario.
        self.btn_cerrar = QPushButton(frm_lista_remoe, clicked= frm_lista_remoe.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(520, 290, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")
        
        self.btn_ver = QPushButton(frm_lista_remoe, clicked = self.ver_gananoe)
        self.btn_ver.setGeometry(QtCore.QRect(440, 290, 75, 23))
        self.btn_ver.setObjectName("btn_ver")

        self.btn_visualiza = QPushButton(frm_lista_remoe, clicked = self.on_cmb_click)
        self.btn_visualiza.setGeometry(QtCore.QRect(360, 290, 75, 23))
        self.btn_visualiza.setObjectName("btn_visualiza")

        
        QtCore.QMetaObject.connectSlotsByName(frm_lista_remoe)

        _translate = QtCore.QCoreApplication.translate
        frm_lista_remoe.setWindowTitle(_translate("frm_lista_rembruta", "Listado de remuneraciones brutas"))
        self.lbl_0.setText(_translate("frm_lista_remoe", "Legajo:"))
        self.lbl_1.setText(_translate("frm_lista_remoe", "Año:"))
        self.lbl_2.setText(_translate("frm_lista_remoe", "Mes:"))
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

        self.actualiza_treeview(legajo, month, year)

        #Eventos.
        self.cmb_legajo.currentTextChanged.connect(self.on_cmb_click)
        self.cmb_mes.currentTextChanged.connect(self.on_cmb_click)
        self.cmb_year.currentTextChanged.connect(self.on_cmb_click)


    def registro_actual(self):
    
        """
        Obtiene el legajo del widget QTableWidget.
        """
    
        try:
            row = self.tw_empleados.currentRow()
            ident = self.tw_empleados.item(row, 0).text()
        
            return ident
    
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
    
    def actualiza_treeview(self, legajo: list, month: list, year: list):

        """
        Actualiza el treeview.
        """

        try:
            listado = lectura_remoe(legajo, month, year)
            self.tw_empleados.setColumnCount(17)
            self.tw_empleados.setRowCount(0)

            #Definición de las columnas.
            #Item id
            item_id = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(0, item_id)   
            #Item legajo
            item_legajo = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(1, item_legajo)
            #Item año
            item_ann = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(2, item_ann)
            #Item cuil empleado
            item_cuilemp = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(3, item_cuilemp)
            #Item denominación
            item_denom = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(4, item_denom)
            #item mes
            item_mes = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(5, item_mes)
            #item ganancia bruta
            item_gananbr = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(6, item_gananbr)
            #item retribuciones no habituales
            item_retnohab = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(7, item_retnohab)
            #item ajuste
            item_ajus = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(8, item_ajus)
            #item remuneraciones exentas
            item_exnoalc = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(9, item_exnoalc)
            #item horas extras gravadas
            item_hegrav = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(10, item_hegrav)
            #item horas extras exentas
            item_heexe = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(11, item_heexe)
            #item material didactico
            item_matdic = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(12, item_matdic)
            #item gastos movilidad
            item_gasmov = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(13, item_gasmov)
            #item obra social
            item_os = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(14, item_os)
            #item seguridad social
            item_jub = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(15, item_jub)    
            #item sindicato
            item_sind = QTableWidgetItem()
            self.tw_empleados.setHorizontalHeaderItem(16, item_sind) 

            _translate = QtCore.QCoreApplication.translate

            #Titúlos de las columnas del treeview
            item_id.setText(_translate("frm_lista_cfam", "Id"))
            item_id = self.tw_empleados.horizontalHeaderItem(0)
            item_legajo.setText(_translate("frm_lista_cfam", "Número de legajo"))
            item_legajo = self.tw_empleados.horizontalHeaderItem(1)
            item_ann.setText(_translate("frm_lista_cfam", "Año"))
            item_ann = self.tw_empleados.horizontalHeaderItem(2)
            item_cuilemp.setText(_translate("frm_lista_cfam", "CUIL"))
            item_cuilemp = self.tw_empleados.horizontalHeaderItem(3)
            item_denom.setText(_translate("frm_lista_cfam", "Denominación"))
            item_denom = self.tw_empleados.horizontalHeaderItem(4)
            item_mes.setText(_translate("frm_lista_cfam", "Mes"))
            item_mes = self.tw_empleados.horizontalHeaderItem(5)
            item_gananbr.setText(_translate("frm_lista_cfam", "Ganancia bruta"))
            item_gananbr = self.tw_empleados.horizontalHeaderItem(6)
            item_retnohab.setText(_translate("frm_lista_cfam", "Retribuciones no habituales"))
            item_retnohab = self.tw_empleados.horizontalHeaderItem(7)
            item_ajus.setText(_translate("frm_lista_cfam", "Ajuste"))
            item_ajus = self.tw_empleados.horizontalHeaderItem(8)
            item_exnoalc.setText(_translate("frm_lista_cfam", "Remuneración exenta"))
            item_exnoalc = self.tw_empleados.horizontalHeaderItem(9)
            item_hegrav.setText(_translate("frm_lista_cfam", "Hs. extras gravadas"))
            item_hegrav = self.tw_empleados.horizontalHeaderItem(10)
            item_heexe.setText(_translate("frm_lista_cfam", "Hs. extras exentas"))
            item_heexe = self.tw_empleados.horizontalHeaderItem(11)
            item_matdic.setText(_translate("frm_lista_cfam", "Material didactico"))
            item_matdic = self.tw_empleados.horizontalHeaderItem(12)
            item_gasmov.setText(_translate("frm_lista_cfam", "Gastos movilidad"))
            item_gasmov = self.tw_empleados.horizontalHeaderItem(13)
            item_os.setText(_translate("frm_lista_cfam", "Obra social"))
            item_os = self.tw_empleados.horizontalHeaderItem(14)
            item_jub.setText(_translate("frm_lista_cfam", "Jubilación"))
            item_jub = self.tw_empleados.horizontalHeaderItem(15)
            item_sind.setText(_translate("frm_lista_cfam", "Sindicato"))
            item_sind = self.tw_empleados.horizontalHeaderItem(16)

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

            self.actualiza_treeview(legajo, month, year)

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

    def ver_gananoe(self):
    
        """
        Abre un formulario con los datos del legajo seleccionado.
        """
        try:
            legajo = self.registro_actual()
        
            if legajo != None:
                frm_dialog = QDialog()
                VerGananOE(legajo, frm_dialog)
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
        
        