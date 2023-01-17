# Formulario para generar reportes.

# Parte de la vista del modelo MVC.


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from crud_bd import lista_empleados
from modelo import xlsx_empleados
from modelo import xlsx_remuneraciones
from modelo import xlsx_deducciones
from modelo import xlsx_cargasfam
from modelo import xlsx_gananciasoe
from modelo import xlsx_promediobruto
from modelo import xlsx_dedpparte
from modelo import xlsx_dedsparte


class Reportes(object):

    def __init__(self, ventana: QDialog):

        #Resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 4)
        alto = float(size.height() / 6.09)

        #Formulario
        super().__init__()

        self.frm_reportes = ventana
        self.frm_reportes.setObjectName("frm_reportes")
        self.frm_reportes.resize(ancho, alto)
        self.frm_reportes.setMinimumSize(ancho, alto)
        self.frm_reportes.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_reportes.setWindowIcon(icon)
        

        self.gridLayout = QGridLayout(self.frm_reportes)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_0 = QLabel(self.frm_reportes)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)

        self.cmb_deduccion = QComboBox(self.frm_reportes)
        self.cmb_deduccion.setObjectName("cmb_deduccion")
        self.gridLayout.addWidget(self.cmb_deduccion, 0, 1, 1, 3)
        self.cmb_deduccion.addItem('Empleados')
        self.cmb_deduccion.addItem('Remuneraciones')
        self.cmb_deduccion.addItem('Deducciones')
        self.cmb_deduccion.addItem('Cargas de familia')
        self.cmb_deduccion.addItem('Ganancias otros empleadores')
        self.cmb_deduccion.addItem('Promedio bruto')
        self.cmb_deduccion.addItem('Ded. Esp. Inc. Primera parte')
        self.cmb_deduccion.addItem('Ded. Esp. Inc. Segunda parte')

        self.cmb_deduccion.currentTextChanged.connect(self.on_cmb_click)
        
        self.lbl_1 = QLabel(self.frm_reportes)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 0, 1, 1)

        self.cmb_legajo = QComboBox(self.frm_reportes)
        self.cmb_legajo.setObjectName("cmb_legajo")
        self.gridLayout.addWidget(self.cmb_legajo, 1, 1, 1, 1)
        self.cmb_legajo.addItem("*")

        try:
            empleados = lista_empleados()
            
            for empleado in empleados:
                self.cmb_legajo.addItem(str(empleado))

        except:
            pass

        self.lbl_2 = QLabel(self.frm_reportes)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 1, 2, 1, 1)

        self.cmb_mes = QComboBox(self.frm_reportes)
        self.cmb_mes.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.cmb_mes, 1, 3, 1, 1)
        self.cmb_mes.addItem('*')
        
        i = 1
            
        while i <= 12:
            self.cmb_mes.addItem(str(i))
            i += 1

        self.lbl_3 = QLabel(self.frm_reportes)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 2, 0, 1, 1)

        self.cmb_ann = QComboBox(self.frm_reportes)
        self.cmb_ann.setObjectName("cmb_legajo_2")
        self.gridLayout.addWidget(self.cmb_ann, 2, 1, 1, 1)
        self.cmb_ann.addItem('*')
        self.cmb_ann.addItem('2021')
        self.cmb_ann.addItem('2022')

        self.btn_cerrar = QPushButton(self.frm_reportes)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 3, 3, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_reportes.close())

        self.btn_procesar = QPushButton(self.frm_reportes)
        self.btn_procesar.setObjectName("btn_procesar")
        self.gridLayout.addWidget(self.btn_procesar, 3, 4, 1, 1)
        self.btn_procesar.clicked.connect(lambda: self.generar_xlsx())

        
        QtCore.QMetaObject.connectSlotsByName(self.frm_reportes)

        _translate = QtCore.QCoreApplication.translate
        self.frm_reportes.setWindowTitle(_translate("self.frm_reportes", "Reporte deducciones"))
        self.lbl_0.setText(_translate("self.frm_reportes", "Deducción:"))
        self.lbl_1.setText(_translate("self.frm_reportes", "Legajo:"))
        self.lbl_2.setText(_translate("self.frm_reportes", "Mes:"))
        self.lbl_3.setText(_translate("self.frm_reportes", "Año:"))
        self.btn_cerrar.setText(_translate("self.frm_reportes", "Cerrar"))
        self.btn_procesar.setText(_translate("self.frm_reportes", "Generar"))

    def on_cmb_click(self):
        
        try:
            if self.cmb_deduccion.currentText() == 'Empleados':
                self.cmb_legajo.setEnabled(False)
                self.cmb_ann.setEnabled(False)
                self.cmb_mes.setEnabled(False)

            elif self.cmb_deduccion.currentText() == 'Promedio bruto':
                self.cmb_legajo.setEnabled(False)

            elif self.cmb_deduccion.currentText() == 'Ded. Esp. Inc. Primera parte':
                self.cmb_legajo.setEnabled(False)

            elif self.cmb_deduccion.currentText() == 'Ded. Esp. Inc. Segunda parte':
                self.cmb_legajo.setEnabled(False)

            else:
                self.cmb_legajo.setEnabled(True)
                self.cmb_ann.setEnabled(True)
                self.cmb_mes.setEnabled(True)

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


    def generar_xlsx(self):
        
        try:
            resultado = False

            legajo = list()
            legajo.append(self.cmb_legajo.currentText())

            month = list()
            month.append(self.cmb_mes.currentText())

            year = list()
            year.append(self.cmb_ann.currentText())

            options = QFileDialog.Options()
            file_name = QFileDialog.getSaveFileName(self.frm_reportes, "Guardar reporte","","Libro de Excel (*.xlsx);;Todos los archivos (*)", 
                                                    options=options)

            if file_name[0] != '':

                if self.cmb_deduccion.currentText() == 'Empleados':
                    resultado = xlsx_empleados(file_name[0])
                elif self.cmb_deduccion.currentText() == 'Remuneraciones':
                    resultado = xlsx_remuneraciones(legajo, month, year, file_name[0])
                elif self.cmb_deduccion.currentText() == 'Deducciones':
                    resultado = xlsx_deducciones(legajo, month, year, file_name[0])
                elif self.cmb_deduccion.currentText() == 'Cargas de familia':
                    resultado = xlsx_cargasfam(legajo = legajo, month = month, year = year, archivo = file_name[0])
                elif self.cmb_deduccion.currentText() == 'Ganancias otros empleadores':
                    resultado = xlsx_gananciasoe(legajo = legajo, month = month, year = year, archivo = file_name[0])
                elif self.cmb_deduccion.currentText() == 'Promedio bruto':
                    resultado = xlsx_promediobruto(month = month, year = year, archivo = file_name[0])
                elif self.cmb_deduccion.currentText() == 'Ded. Esp. Inc. Primera parte':
                    resultado = xlsx_dedpparte(month = month, year = year, archivo = file_name[0])
                else:
                    resultado = xlsx_dedsparte(month = month, year = year, archivo = file_name[0])
            
            if resultado == True:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Se genero el archivo correctamente.")
                msg_box.setWindowTitle("Información")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                msg_box.exec()

            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Error en proceso de generación del archivo. Verifique conexión a base de datos.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon) 
                msg_box.exec()
    
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en proceso de generación del archivo. Verifique conexión a base de datos.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()