# Fomulario para visualizar los valores correspondientes al cálculo de la primera parte de la deducción especial.
# Parte de la vista del modelo MVC.


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QAbstractItemView
from crud_bd import lee_segundoparrafo

class VerDeduccionSParte(QDialog):

    def __init__(self, ventana: QDialog):
        
        #Formulario.
        super().__init__(ventana)
        frm_ver_segparte = ventana
        frm_ver_segparte.setObjectName("frm_ver_segparte")
        frm_ver_segparte.resize(534, 278)
        frm_ver_segparte.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        frm_ver_segparte.setMinimumSize(534, 278)
        frm_ver_segparte.setMaximumSize(534, 278)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_ver_segparte.setWindowIcon(icon)
        
        #Labels.
        self.lbl_0 = QLabel(frm_ver_segparte)
        self.lbl_0.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.lbl_0.setObjectName("lbl_0")

        self.lbl_1 = QLabel(frm_ver_segparte)
        self.lbl_1.setGeometry(QtCore.QRect(150, 10, 31, 16))
        self.lbl_1.setObjectName("lbl_1")

        #ComboBox.
        self.cmb_year = QComboBox(frm_ver_segparte)
        self.cmb_year.setGeometry(QtCore.QRect(50, 10, 81, 22))
        self.cmb_year.setObjectName("cmb_year")
        self.cmb_year.addItem('*')
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')

        self.cmb_mes = QComboBox(frm_ver_segparte)
        self.cmb_mes.setGeometry(QtCore.QRect(190, 10, 81, 22))
        self.cmb_mes.setObjectName("cmb_mes")
        self.cmb_mes.addItem('*')

        i = 1

        while i <= 12:
            self.cmb_mes.addItem(str(i))
            i += 1

        #Treeview.
        self.tv_segundaparte = QTableWidget(frm_ver_segparte)
        self.tv_segundaparte.setGeometry(QtCore.QRect(10, 40, 511, 192))
        self.tv_segundaparte.setObjectName("tv_segundaparte")
        self.tv_segundaparte.setColumnCount(0)
        self.tv_segundaparte.setRowCount(0)

        #Se establece la tabla como no editable y que no se permita el drag & drop
        self.tv_segundaparte.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_segundaparte.setDragDropOverwriteMode(False)
        
        #Modo de selección de datos.
        self.tv_segundaparte.setSelectionMode(QAbstractItemView.SingleSelection)
        
        #Botones.
        self.btn_cerrar = QPushButton(frm_ver_segparte, clicked = frm_ver_segparte.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(450, 240, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")

        self.btn_actualiza = QPushButton(frm_ver_segparte, clicked = self.on_click_cmb)
        self.btn_actualiza.setGeometry(QtCore.QRect(370, 240, 75, 23))
        self.btn_actualiza.setObjectName("btn_actualiza")

        QtCore.QMetaObject.connectSlotsByName(frm_ver_segparte)

        _translate = QtCore.QCoreApplication.translate
        frm_ver_segparte.setWindowTitle(_translate("frm_ver_segparte", "Ver Deducción especial segunda parte"))
        self.lbl_0.setText(_translate("frm_ver_segparte", "Año:"))
        self.lbl_1.setText(_translate("frm_ver_segparte", "Mes:"))
        self.btn_cerrar.setText(_translate("frm_ver_segparte", "Cerrar"))
        self.btn_actualiza.setText(_translate("frm_ver_segparte", "Actualizar"))

        #Actualiza treeview al inicar el formulario.

        #Visualiza los datos para el treeview.
        month = list()
        month.append('*')
        
        year = list()
        year.append('*')

        self.ver_segparrafo(month, year)

        #Eventos.
        self.cmb_mes.currentTextChanged.connect(self.on_click_cmb)
        self.cmb_year.currentTextChanged.connect(self.on_click_cmb)


    def ver_segparrafo(self, month, year):
        
        try:
            listado = lee_segundoparrafo(month, year)
    
            self.tv_segundaparte.clear()
            self.tv_segundaparte.setColumnCount(4)
            self.tv_segundaparte.setRowCount(0)
    
            #Definición de las columnas.
            #Item legajo
            item_leg = QTableWidgetItem()
            self.tv_segundaparte.setHorizontalHeaderItem(0, item_leg)
            item_ann = QTableWidgetItem()
            self.tv_segundaparte.setHorizontalHeaderItem(1, item_ann)
            item_mes = QTableWidgetItem()
            self.tv_segundaparte.setHorizontalHeaderItem(2, item_mes)
            item_importe = QTableWidgetItem()
            self.tv_segundaparte.setHorizontalHeaderItem(3, item_importe)
    
            #Titúlos de las columnas del treeview
            _translate = QtCore.QCoreApplication.translate
            item_leg.setText(_translate("frm_ver_segparte", "Legajo"))
            item_leg = self.tv_segundaparte.horizontalHeaderItem(0)
            item_ann.setText(_translate("frm_ver_segparte", "Año"))
            item_ann = self.tv_segundaparte.horizontalHeaderItem(1)
            item_mes.setText(_translate("frm_ver_segparte", "Mes"))
            item_mes = self.tv_segundaparte.horizontalHeaderItem(2)
            item_importe.setText(_translate("frm_ver_segparte", "Ded. Esp. Inc. Segunda parte"))
            item_importe = self.tv_segundaparte.horizontalHeaderItem(3)
    
            for lista in listado:
    
                position = self.tv_segundaparte.rowCount()
                self.tv_segundaparte.insertRow(position)          
    
                y = 0

                for n in lista:
                    valor = str(n)
                    self.tv_segundaparte.setItem(position, y, QTableWidgetItem(valor))
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
        

    def on_click_cmb(self):
        
        try:

            month = list()
            month.append(self.cmb_mes.currentText())
        
            year = list()
            year.append(self.cmb_year.currentText())
        
            self.ver_segparrafo(month, year)
        
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