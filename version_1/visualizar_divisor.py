from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from ver_divisor import VerDivisor
from crud_bd import lectura_divisor


class ListaDivisor(QDialog):


    def __init__ (self, ventana: QDialog):
        
        #Formulario principal
        super().__init__(ventana)
        frm_lista_divisor = ventana
        frm_lista_divisor.setObjectName("frm_lista_divisor")
        frm_lista_divisor.resize(514, 295)
        frm_lista_divisor.setMinimumSize(514, 295)
        frm_lista_divisor.setMaximumSize(514, 295)
        frm_lista_divisor.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_lista_divisor.setWindowIcon(icon) 

        #Boton que cierra el formulario
        self.btn_cerrar = QPushButton(frm_lista_divisor, clicked = frm_lista_divisor.close)
        self.btn_cerrar.setGeometry(QtCore.QRect(430, 260, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")
        
        #Boton que llama a la función para ver un registro en particular.
        self.btn_ver = QPushButton(frm_lista_divisor, clicked = self.crea_ver_emp)
        self.btn_ver.setGeometry(QtCore.QRect(340, 260, 75, 23))
        self.btn_ver.setObjectName("btn_ver")

        self.btn_visualizar = QPushButton(frm_lista_divisor, clicked = self.actualiza_treeview)
        self.btn_visualizar.setGeometry(QtCore.QRect(260, 260, 75, 23))
        self.btn_visualizar.setObjectName("btn_visualizar")

        #Table widget
        self.tv_empleado = QTableWidget(frm_lista_divisor)
        self.tv_empleado.setGeometry(QtCore.QRect(10, 10, 491, 241))
        self.tv_empleado.setObjectName("tv_empleado")

        #Se establece la tabla como no editable y que no se permita el drag & drop
        self.tv_empleado.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_empleado.setDragDropOverwriteMode(False)

        #Modo de selección de datos.
        self.tv_empleado.setSelectionMode(QAbstractItemView.SingleSelection)

        #Ancho de las columnas.

        #Colores alternados.
        self.tv_empleado.setAlternatingRowColors(True)
         
        QtCore.QMetaObject.connectSlotsByName(frm_lista_divisor)

        _translate = QtCore.QCoreApplication.translate
        frm_lista_divisor.setWindowTitle(_translate("frm_lista_divisor", "Divisor promedio bruto"))
        self.btn_cerrar.setText(_translate("frm_lista_divisor", "Cerrar"))
        self.btn_ver.setText(_translate("frm_lista_divisor", "Ver"))
        self.btn_visualizar.setText(_translate("frm_lista_divisor", "Actualizar"))
        
        #Actualiza el treeview.
        self.actualiza_treeview()


    def registro_actual(self):

        """
        Obiene el campo legajo del widget QTableWidget.
        """
        
        try:
            row = self.tv_empleado.currentRow()
            ident = self.tv_empleado.item(row, 0).text()

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

    def actualiza_treeview(self):
        
        """
        Actualiza la información en el treeview
        """

        try:

            empleados = lectura_divisor()

            #Se define la cantidad de columnas y los nombres.
            self.tv_empleado.setColumnCount(5)
            self.tv_empleado.setRowCount(0)
            
            item_id = QTableWidgetItem()
            self.tv_empleado.setHorizontalHeaderItem(0, item_id)
            item_legajo = QTableWidgetItem()
            self.tv_empleado.setHorizontalHeaderItem(1, item_legajo)
            item_ann = QTableWidgetItem()
            self.tv_empleado.setHorizontalHeaderItem(2, item_ann)
            item_mes = QTableWidgetItem()
            self.tv_empleado.setHorizontalHeaderItem(3, item_mes)
            item_divisor = QTableWidgetItem()
            self.tv_empleado.setHorizontalHeaderItem(4, item_divisor)

            _translate = QtCore.QCoreApplication.translate

            item_id.setText(_translate("MainWindow", "Id"))
            item_id = self.tv_empleado.horizontalHeaderItem(0)
            item_legajo.setText(_translate("MainWindow", "Legajo"))
            item_legajo = self.tv_empleado.horizontalHeaderItem(1)
            item_ann.setText(_translate("MainWindow", "Año"))
            item_ann = self.tv_empleado.horizontalHeaderItem(2)
            item_mes.setText(_translate("MainWindow", "Mes"))
            item_mes = self.tv_empleado.horizontalHeaderItem(3)
            item_divisor.setText(_translate("MainWindow", "Divisor"))
            item_divisor = self.tv_empleado.horizontalHeaderItem(4)

            for empleado in empleados:
                position = self.tv_empleado.rowCount()
                self.tv_empleado.insertRow(position)          
                y = 0
            
                for n in empleado:
                    valor = str(n)
                    self.tv_empleado.setItem(position, y, QTableWidgetItem(valor))
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


    def crea_ver_emp(self, id):

        try:
            id = self.registro_actual()

            if id != None:
                frm_dialog = QDialog()
                VerDivisor(id, frm_dialog)
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
        
        