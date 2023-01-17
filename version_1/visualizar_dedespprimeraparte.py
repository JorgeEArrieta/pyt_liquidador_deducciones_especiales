# Fomulario para visualizar los valores correspondientes al cálculo de la primera parte de la deducción especial.
# Parte de la vista del modelo MVC.

from calendar import month
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
from crud_bd import lee_primerparrafo


class VerDeduccionPParte(QDialog):

    def __init__(self, ventana: QDialog):
        
        super().__init__(ventana)
        frm_ver_dedprimparte = ventana
        frm_ver_dedprimparte.setObjectName("frm_ver_dedprimparte")
        frm_ver_dedprimparte.resize(534, 276)
        frm_ver_dedprimparte.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        frm_ver_dedprimparte.setMinimumSize(534, 276)
        frm_ver_dedprimparte.setMaximumSize(534, 276)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_ver_dedprimparte.setWindowIcon(icon)

        #Labels
        self.lbl_0 = QLabel(frm_ver_dedprimparte)
        self.lbl_0.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.lbl_0.setObjectName("lbl_0")
        
        self.lbl_1 = QLabel(frm_ver_dedprimparte)
        self.lbl_1.setGeometry(QtCore.QRect(150, 10, 31, 16))
        self.lbl_1.setObjectName("lbl_1")

        #Combo box
        self.cmb_year = QComboBox(frm_ver_dedprimparte)
        self.cmb_year.setGeometry(QtCore.QRect(50, 10, 81, 22))
        self.cmb_year.setObjectName("cmb_year")
        self.cmb_year.addItem('*')
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')
        
        self.cmb_mes = QComboBox(frm_ver_dedprimparte)
        self.cmb_mes.setGeometry(QtCore.QRect(190, 10, 81, 22))
        self.cmb_mes.setObjectName("cmb_mes")
        self.cmb_mes.addItem('*')

        i = 1

        while i <= 12:
            self.cmb_mes.addItem(str(i))
            i += 1
        
        #Treeview
        self.tv_primeraparte = QTableWidget(frm_ver_dedprimparte)
        self.tv_primeraparte.setGeometry(QtCore.QRect(10, 40, 511, 192))
        self.tv_primeraparte.setObjectName("tv_primeraparte")
        self.tv_primeraparte.setColumnCount(0)
        self.tv_primeraparte.setRowCount(0)

        #Se establece la tabla como no editable y que no se permita el drag & drop
        self.tv_primeraparte.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_primeraparte.setDragDropOverwriteMode(False)
        
        #Modo de selección de datos.
        self.tv_primeraparte.setSelectionMode(QAbstractItemView.SingleSelection)
        
        #Botón
        self.btn_cerrar = QPushButton(frm_ver_dedprimparte, clicked = frm_ver_dedprimparte.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(450, 240, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")

        self.btn_actualizar = QPushButton(frm_ver_dedprimparte)
        self.btn_actualizar.setGeometry(QtCore.QRect(370, 240, 75, 23))
        self.btn_actualizar.setObjectName("btn_actualizar")

        QtCore.QMetaObject.connectSlotsByName(frm_ver_dedprimparte)
    
        _translate = QtCore.QCoreApplication.translate
        frm_ver_dedprimparte.setWindowTitle(_translate("frm_ver_dedprimparte", "Ver Deducción especial primera parte"))
        self.btn_cerrar.setText(_translate("frm_ver_dedprimparte", "Cerrar"))
        self.btn_actualizar.setText(_translate("frm_ver_dedprimparte", "Actualizar"))
        self.lbl_0.setText(_translate("frm_ver_dedprimparte", "Año:"))
        self.lbl_1.setText(_translate("frm_ver_dedprimparte", "Mes:"))

        #Visualiza los datos para el treeview.
        month = list()
        month.append('*')

        year = list()
        year.append('*')

        self.ver_primerparrafo(month, year)

        #Eventos.
        self.cmb_mes.currentTextChanged.connect(self.on_click_cmb)
        self.cmb_year.currentTextChanged.connect(self.on_click_cmb)


    def ver_primerparrafo(self, month, year):

        try:
    
            listado = lee_primerparrafo(month, year)
    
            self.tv_primeraparte.clear()
            self.tv_primeraparte.setColumnCount(9)
            self.tv_primeraparte.setRowCount(0)
    
            #Definición de las columnas.
            #Item legajo
            item_leg = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(0, item_leg)
            item_ann = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(1, item_ann)
            item_mes = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(2, item_mes)  
            item_sbruto = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(3, item_sbruto)
            item_deducciones = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(4, item_deducciones)  
            item_ded_esp = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(5, item_ded_esp) 
            item_min_no_imp = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(6, item_min_no_imp) 
            item_car_fam = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(7, item_car_fam)
            item_ded_p_par = QTableWidgetItem()
            self.tv_primeraparte.setHorizontalHeaderItem(8, item_ded_p_par) 
    
            #Titúlos de las columnas del treeview
            _translate = QtCore.QCoreApplication.translate
            item_leg.setText(_translate("frm_ver_dedprimparte", "Legajo"))
            item_leg = self.tv_primeraparte.horizontalHeaderItem(0)
            item_ann.setText(_translate("frm_ver_dedprimparte", "Año"))
            item_ann = self.tv_primeraparte.horizontalHeaderItem(1)
            item_mes.setText(_translate("frm_ver_dedprimparte", "Mes"))
            item_mes = self.tv_primeraparte.horizontalHeaderItem(2)
            item_sbruto.setText(_translate("frm_ver_dedprimparte", "Salario bruto"))
            item_sbruto = self.tv_primeraparte.horizontalHeaderItem(3)
            item_deducciones.setText(_translate("frm_ver_dedprimparte", "Deducciones"))
            item_deducciones = self.tv_primeraparte.horizontalHeaderItem(4)
            item_ded_esp.setText(_translate("frm_ver_dedprimparte", "Deducción especial"))
            item_ded_esp = self.tv_primeraparte.horizontalHeaderItem(5)
            item_min_no_imp.setText(_translate("frm_ver_dedprimparte", "Ganancias no imponibles"))
            item_min_no_imp = self.tv_primeraparte.horizontalHeaderItem(6)
            item_car_fam.setText(_translate("frm_ver_dedprimparte", "Cargas de familia"))
            item_car_fam = self.tv_primeraparte.horizontalHeaderItem(7)
            item_ded_p_par.setText(_translate("frm_ver_dedprimparte", "Deducción Especial Incrementada Primera parte"))
            item_ded_p_par = self.tv_primeraparte.horizontalHeaderItem(8)
    
    
            for lista in listado:
    
                position = self.tv_primeraparte.rowCount()
                self.tv_primeraparte.insertRow(position)          
    
                y = 0
    
                for n in lista:
                    valor = str(n)
                    self.tv_primeraparte.setItem(position, y, QTableWidgetItem(valor))
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

            self.ver_primerparrafo(month, year)
        
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