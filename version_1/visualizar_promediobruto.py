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
from crud_bd import lee_promediobruto


class VerPromedioBruto(QDialog):

    def __init__(self, ventana: QDialog):

        super().__init__(ventana)
        frm_ver_prombruto = ventana
        frm_ver_prombruto.setObjectName("frm_ver_prombruto")
        frm_ver_prombruto.resize(534, 270)
        frm_ver_prombruto.setMinimumSize(534, 270)
        frm_ver_prombruto.setMaximumSize(534, 270)
        frm_ver_prombruto.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_ver_prombruto.setWindowIcon(icon)

        #Labels.
        self.lbl_0 = QLabel(frm_ver_prombruto)
        self.lbl_0.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.lbl_0.setObjectName("lbl_0")

        self.lbl_1 = QLabel(frm_ver_prombruto)
        self.lbl_1.setGeometry(QtCore.QRect(170, 10, 41, 16))
        self.lbl_1.setObjectName("lbl_1")

        #Combo box.
        self.cmb_year = QComboBox(frm_ver_prombruto)
        self.cmb_year.setGeometry(QtCore.QRect(50, 10, 91, 22))
        self.cmb_year.setObjectName("cmb_year")
        self.cmb_year.addItem('*')
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')
        
        self.cmb_mes = QComboBox(frm_ver_prombruto)
        self.cmb_mes.setGeometry(QtCore.QRect(210, 10, 91, 22))
        self.cmb_mes.setObjectName("cmb_mes")
        self.cmb_mes.addItem('*')

        i = 1 

        while i <= 12:
            self.cmb_mes.addItem(str(i))
            i += 1

        #Treeview
        self.tv_promediobruto = QTableWidget(frm_ver_prombruto)
        self.tv_promediobruto.setGeometry(QtCore.QRect(10, 40, 511, 192))
        self.tv_promediobruto.setObjectName("tv_promediobruto")
        self.tv_promediobruto.setColumnCount(0)
        self.tv_promediobruto.setRowCount(0)

        #Se establece la tabla como no editable y que no se permita el drag & drop
        self.tv_promediobruto.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_promediobruto.setDragDropOverwriteMode(False)
        
        #Modo de selección de datos.
        self.tv_promediobruto.setSelectionMode(QAbstractItemView.SingleSelection)

        #Botones.
        self.btn_cerrar = QPushButton(frm_ver_prombruto, clicked = frm_ver_prombruto.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(450, 240, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")

        self.btn_actualizar = QPushButton(frm_ver_prombruto, clicked = self.on_cmb_click)
        self.btn_actualizar.setGeometry(QtCore.QRect(370, 240, 75, 23))
        self.btn_actualizar.setObjectName("btn_actualizar")

        QtCore.QMetaObject.connectSlotsByName(frm_ver_prombruto)

        _translate = QtCore.QCoreApplication.translate
        frm_ver_prombruto.setWindowTitle(_translate("frm_ver_prombruto", "Ver promedios brutos"))
        self.lbl_0.setText(_translate("frm_ver_prombruto", "Año:"))
        self.lbl_1.setText(_translate("frm_ver_prombruto", "Mes:"))
        self.btn_cerrar.setText(_translate("frm_ver_prombruto", "Cerrar"))
        self.btn_actualizar.setText(_translate("frm_ver_prombruto", "Actualizar"))
        
        #Actualiza treeview.
        month = list()
        month.append('*')
        
        year = list()
        year.append('*')
        
        self.ver_promedio_bruto(month, year)

        #Eventos.
        self.cmb_mes.currentTextChanged.connect(self.on_cmb_click)
        self.cmb_year.currentTextChanged.connect(self.on_cmb_click)


    def ver_promedio_bruto(self, month, year):
        
        try:
    
            listado = lee_promediobruto(month, year)
    
            self.tv_promediobruto.clear()
            self.tv_promediobruto.setColumnCount(4)
            self.tv_promediobruto.setRowCount(0)
            
            #Definición de las columnas.
            #Item legajo
            item_leg = QTableWidgetItem()
            self.tv_promediobruto.setHorizontalHeaderItem(0, item_leg)
            item_ann = QTableWidgetItem()
            self.tv_promediobruto.setHorizontalHeaderItem(1, item_ann)
            item_mes = QTableWidgetItem()
            self.tv_promediobruto.setHorizontalHeaderItem(2, item_mes)
            item_importe = QTableWidgetItem()
            self.tv_promediobruto.setHorizontalHeaderItem(3, item_importe)
    
            #Titúlos de las columnas del treeview
            _translate = QtCore.QCoreApplication.translate
            item_leg.setText(_translate("frm_ver_prombruto", "Legajo"))
            item_leg = self.tv_promediobruto.horizontalHeaderItem(0)
            item_ann.setText(_translate("frm_ver_prombruto", "Año"))
            item_ann = self.tv_promediobruto.horizontalHeaderItem(1)
            item_mes.setText(_translate("frm_ver_prombruto", "Mes"))
            item_mes = self.tv_promediobruto.horizontalHeaderItem(2)
            item_importe.setText(_translate("frm_ver_prombruto", "Importe"))
            item_importe = self.tv_promediobruto.horizontalHeaderItem(3)
    
            for lista in listado:
        
                position = self.tv_promediobruto.rowCount()
                self.tv_promediobruto.insertRow(position)          
        
                y = 0
        
                for n in lista:
            
                    valor = str(n)
                    self.tv_promediobruto.setItem(position, y, QTableWidgetItem(valor))
                    y += 1

        except TypeError:
            
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en base de datos.")
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

    def on_cmb_click(self):
        
        try:
            month = list()
            month.append(self.cmb_mes.currentText())
        
            year = list()
            year.append(self.cmb_year.currentText())
        
            self.ver_promedio_bruto(month, year)

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