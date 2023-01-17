#Formulario visualizar los registros pertenecientes a cargas de familia.
#Parte de la Vista del modelo MVC.

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QMessageBox
from ver_carga_familia import VerCFam
from crud_bd import lista_empleados
from crud_bd import lectura_carfam


class VisualizarCFamilia(QDialog):

    def __init__(self, ventana: QDialog):
        
        #Declararción del formulario.
        super().__init__(ventana)
        frm_lista_cfam = ventana
        frm_lista_cfam.setObjectName("frm_lista_cfam")
        frm_lista_cfam.resize(601, 317)
        frm_lista_cfam.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        frm_lista_cfam.setMinimumSize(601, 317)
        frm_lista_cfam.setMaximumSize(601, 317)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_lista_cfam.setWindowIcon(icon)

        #Labels.
        self.lbl_0 = QLabel(frm_lista_cfam)
        self.lbl_0.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.lbl_0.setObjectName("lbl_0")

        self.lbl_1 = QLabel(frm_lista_cfam)
        self.lbl_1.setGeometry(QtCore.QRect(170, 10, 41, 16))
        self.lbl_1.setObjectName("lbl_1")

        self.lbl_2 = QLabel(frm_lista_cfam)
        self.lbl_2.setGeometry(QtCore.QRect(330, 10, 41, 16))
        self.lbl_2.setObjectName("lbl_2")

        #Combo box.
        self.cmb_legajo = QComboBox(frm_lista_cfam)
        self.cmb_legajo.setGeometry(QtCore.QRect(50, 10, 91, 22))
        self.cmb_legajo.setObjectName("cmb_legajo")
        self.cmb_legajo.addItem('*')
        

        #Obtiene listado de empleados para cargar los datos en el combobox
        try:
            empleados = lista_empleados()

            for empleado in empleados:
                self.cmb_legajo.addItem(str(empleado))

        except:
            pass

        self.cmb_year = QComboBox(frm_lista_cfam)
        self.cmb_year.setGeometry(QtCore.QRect(210, 10, 91, 22))
        self.cmb_year.setObjectName("cmb_year")
        self.cmb_year.addItem('*')
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')
        

        self.cmb_mes = QComboBox(frm_lista_cfam)
        self.cmb_mes.setGeometry(QtCore.QRect(370, 10, 91, 22))
        self.cmb_mes.setObjectName("cmb_mes")
        self.cmb_mes.addItem('*')

        i = 1

        while i <= 12:
            self.cmb_mes.addItem(str(i))
            i +=1
        
        #Declaración del treeview
        self.tw_empleados = QTableWidget(frm_lista_cfam)
        self.tw_empleados.setGeometry(QtCore.QRect(10, 40, 581, 231))
        self.tw_empleados.setObjectName("tw_empleados")
        self.tw_empleados.setColumnCount(10)
        self.tw_empleados.setRowCount(0)

        #Se establece la tabla como no editable y que no se permita el drag & drop
        self.tw_empleados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_empleados.setDragDropOverwriteMode(False)

        #Modo de selección de datos.
        self.tw_empleados.setSelectionMode(QAbstractItemView.SingleSelection)

        #Definición de las columnas.
        #Item legajo
        item_id = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(0, item_id)
        #Item legajo
        item_legajo = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(1, item_legajo)
        #Item legajo
        item_ann = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(2, item_ann)
        #Item cuil empleado
        item_cuilemp = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(3, item_cuilemp)
        #Item documento familiar
        item_docfam = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(4, item_docfam)
        #item apellido familiar
        item_apfam = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(5, item_apfam)
        #Item nombre familiar
        item_nomfam = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(6, item_nomfam)
        #item mes desde
        item_mesdesde = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(7, item_mesdesde)
        #item mes hasta
        item_meshasta = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(8, item_meshasta)
        #item parentesco
        item_parent = QTableWidgetItem()
        self.tw_empleados.setHorizontalHeaderItem(9, item_parent)
                                                 
        #Declaración de los botones del formulario.
        self.btn_cerrar = QPushButton(frm_lista_cfam, clicked= frm_lista_cfam.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(520, 280, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")
        
        self.btn_ver = QPushButton(frm_lista_cfam, clicked = self.ver_cfam)
        self.btn_ver.setGeometry(QtCore.QRect(440, 280, 75, 23))
        self.btn_ver.setObjectName("btn_ver")

        self.btn_actualiza = QPushButton(frm_lista_cfam, clicked = self.on_cmb_change)
        self.btn_actualiza.setGeometry(QtCore.QRect(360, 280, 75, 23))
        self.btn_actualiza.setObjectName("btn_ver")

        
        QtCore.QMetaObject.connectSlotsByName(frm_lista_cfam)

        _translate = QtCore.QCoreApplication.translate
        frm_lista_cfam.setWindowTitle(_translate("frm_lista_rembruta", "Listado de remuneraciones brutas"))
        self.btn_cerrar.setText(_translate("frm_lista_rembruta", "Cerrar"))
        self.btn_ver.setText(_translate("frm_lista_rembruta", "Ver"))
        self.btn_actualiza.setText(_translate("frm_lista_rembruta", "Actualizar"))
        self.lbl_0.setText(_translate("frm_lista_cfamilia", "Legajo:"))
        self.lbl_1.setText(_translate("frm_lista_cfamilia", "Año:"))
        self.lbl_2.setText(_translate("frm_lista_cfamilia", "Mes:"))
        
        #Titúlos de las columnas del treeview
        item_id.setText(_translate("frm_lista_cfam", "Id"))
        item_id = self.tw_empleados.horizontalHeaderItem(0)
        item_legajo.setText(_translate("frm_lista_cfam", "Número de legajo"))
        item_legajo = self.tw_empleados.horizontalHeaderItem(1)
        item_ann.setText(_translate("frm_lista_cfam", "Año"))
        item_ann = self.tw_empleados.horizontalHeaderItem(2)
        item_cuilemp.setText(_translate("frm_lista_cfam", "CUIL"))
        item_cuilemp = self.tw_empleados.horizontalHeaderItem(3)
        item_docfam.setText(_translate("frm_lista_cfam", "N° Doc. familiar"))
        item_docfam = self.tw_empleados.horizontalHeaderItem(4)
        item_apfam.setText(_translate("frm_lista_cfam", "Apeliido"))
        item_apfam = self.tw_empleados.horizontalHeaderItem(5)
        item_nomfam.setText(_translate("frm_lista_cfam", "Nombre"))
        item_nomfam = self.tw_empleados.horizontalHeaderItem(6)
        item_mesdesde.setText(_translate("frm_lista_cfam", "Mes desde"))
        item_mesdesde = self.tw_empleados.horizontalHeaderItem(7)
        item_meshasta.setText(_translate("frm_lista_cfam", "Mes hasta"))
        item_meshasta = self.tw_empleados.horizontalHeaderItem(8)
        item_parent.setText(_translate("frm_lista_cfam", "Parentesco"))
        item_parent = self.tw_empleados.horizontalHeaderItem(9)

        #Inicia los valores el treeview.
        legajo = list()
        legajo.append('*')
        mes = list() 
        mes.append('*')
        year = list()
        year.append('*') 

        self.actualiza_treeview(legajo, year, mes)

        #Eventos.
        self.cmb_legajo.currentTextChanged.connect(self.on_cmb_change)
        self.cmb_year.currentTextChanged.connect(self.on_cmb_change)
        self.cmb_mes.currentTextChanged.connect(self.on_cmb_change)


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

    def ver_cfam(self):
    
        """
        Abre un formulario con los datos del legajo seleccionado.
        """
        try:
            id = self.registro_actual()

            if id != None:
                frm_dialog = QDialog()
                VerCFam(id, frm_dialog)
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

    def actualiza_treeview(self, legajo, mes, year):
        
        try:
            
            listado = lectura_carfam(legajo, mes, year)

            while self.tw_empleados.rowCount() > 0:
                self.tw_empleados.removeRow(0)

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
        

    def on_cmb_change(self):

        try:
        
            legajo = list()
            legajo.append(self.cmb_legajo.currentText())
        
            year = list()
            year.append(self.cmb_year.currentText())
        
            mes = list()
            mes.append(self.cmb_mes.currentText())

            self.actualiza_treeview(legajo, year, mes)

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
