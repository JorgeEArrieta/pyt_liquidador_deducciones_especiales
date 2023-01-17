# Formulario que permite parametrizar los valores de la deducciones segunda parte
# Parte de la vista del modelo MVC.



from PyQt5 import QtCore 
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QTableWidgetItem
from crud_bd import lee_dedsegundoparrafo
from ver_dedsparte import VerDedSParte
from carga_masiva import CargaMasiva


class ParametroDedSParte(QDialog):
    
    def __init__ (self, ventana: QDialog):

        #Formulario.
        super().__init__()

        frm_valores_dedsparte = ventana
        frm_valores_dedsparte.setObjectName("frm_valores_dedsparte")
        frm_valores_dedsparte.resize(543, 309)
        frm_valores_dedsparte.setMinimumSize(543, 309)
        frm_valores_dedsparte.setMaximumSize(543, 309)
        frm_valores_dedsparte.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_valores_dedsparte.setWindowIcon(icon) 
        
        self.lbl_0 = QLabel(frm_valores_dedsparte)
        self.lbl_0.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.lbl_0.setObjectName("lbl_0")
        
        self.cmb_resolucion = QComboBox(frm_valores_dedsparte)
        self.cmb_resolucion.setGeometry(QtCore.QRect(80, 10, 151, 22))
        self.cmb_resolucion.setObjectName("cmb_resolucion")
        self.cmb_resolucion.addItem('Resolución 5008/2021')
        self.cmb_resolucion.addItem('Resolución 5076/2021')
        self.cmb_resolucion.addItem('RIPTE_2022')

        #TableWidget
        self.tableWidget = QTableWidget(frm_valores_dedsparte)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 521, 231))
        self.tableWidget.setObjectName("tableWidget")
        
        #Se establece la tabla como no editable y que no se permita el drag & drop
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        #Modo de selección de datos.
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        
        #Botones
        self.btn_cerrar = QPushButton(frm_valores_dedsparte, clicked = frm_valores_dedsparte.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(460, 280, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")
        
        self.btn_ver = QPushButton(frm_valores_dedsparte, clicked = self.ver_dedsparte)
        self.btn_ver.setGeometry(QtCore.QRect(380, 280, 75, 23))
        self.btn_ver.setObjectName("btn_ver")
        
        self.btn_carga = QPushButton(frm_valores_dedsparte, clicked = lambda: self.carga_masiva())
        self.btn_carga.setGeometry(QtCore.QRect(300, 280, 75, 23))
        self.btn_carga.setObjectName("btn_carga")

        self.btn_actualiza = QPushButton(frm_valores_dedsparte, clicked = self.on_cmb_click)
        self.btn_actualiza.setGeometry(QtCore.QRect(220, 280, 75, 23))
        self.btn_actualiza.setObjectName("btn_carga")
        
        QtCore.QMetaObject.connectSlotsByName(frm_valores_dedsparte)

        _translate = QtCore.QCoreApplication.translate
        frm_valores_dedsparte.setWindowTitle(_translate("frm_valores_dedsparte", "Parámetros - Deducción segunda parte"))
        self.lbl_0.setText(_translate("frm_valores_dedsparte", "Resolución:"))
        self.btn_cerrar.setText(_translate("frm_valores_dedsparte", "Cerrar"))
        self.btn_ver.setText(_translate("frm_valores_dedsparte", "Ver"))
        self.btn_carga.setText(_translate("frm_valores_dedsparte", "Carga Masiva"))
        self.btn_actualiza.setText(_translate("frm_valores_dedsparte", "Actualizar"))

        self.actualiza_treeview('RG_5008')

        self.cmb_resolucion.currentTextChanged.connect(self.on_cmb_click)


    def actualiza_treeview(self, resolucion):

        try:

            listado = lee_dedsegundoparrafo(resolucion)

            self.tableWidget.setColumnCount(5)
            self.tableWidget.setRowCount(0)

            #Definición de las columnas.
            item_id = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item_id)
            item_resolucion = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item_resolucion)
            item_val_min = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, item_val_min)
            item_val_max = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(3, item_val_max)
            item_deduccion = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(4, item_deduccion)

            _translate = QtCore.QCoreApplication.translate

            #Titúlos de las columnas del treeview
            item_id.setText(_translate("frm_lista_cfam", "Id"))
            item_id = self.tableWidget.horizontalHeaderItem(0)
            item_resolucion.setText(_translate("frm_lista_cfam", "Resolución"))
            item_resolucion = self.tableWidget.horizontalHeaderItem(1)
            item_val_min.setText(_translate("frm_lista_cfam", "Valor mínimo"))
            item_val_min = self.tableWidget.horizontalHeaderItem(2)
            item_val_max.setText(_translate("frm_lista_cfam", "Valor máximo"))
            item_val_max = self.tableWidget.horizontalHeaderItem(3)
            item_deduccion.setText(_translate("frm_lista_cfam", "Deducción"))
            item_deduccion = self.tableWidget.horizontalHeaderItem(4)
            
            for lista in listado:
            
                position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(position)          
                y = 0
                for n in lista:
                    valor = str(n)
                    self.tableWidget.setItem(position, y, QTableWidgetItem(valor))
                    y += 1
        
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
            datos = self.cmb_resolucion.currentText()

            if datos == 'Resolución 5008/2021':
                resolucion = 'RG_5008'
            elif datos == 'Resolución 5076/2021':
                resolucion = 'RG_5076'
            else:
                resolucion = 'RIPTE_2022'

            self.actualiza_treeview(resolucion)

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
            row = self.tableWidget.currentRow()
            ident = self.tableWidget.item(row, 0).text()
        
            return ident
    
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
        

    def ver_dedsparte(self):
    
        """
        Abre un formulario con los datos del legajo seleccionado.
        """
    
        try:
            id = self.registro_actual()
            if id != None:
                frm_dialog = QDialog()
                VerDedSParte(id, frm_dialog)
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

    
    def carga_masiva(self):

        try:
            frm_dialog = QDialog()
            CargaMasiva(frm_dialog)
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
            