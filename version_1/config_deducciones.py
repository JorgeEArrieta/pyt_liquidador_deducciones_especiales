# Formulario para configurar las deduciones que se incluyen en el calculo del primer párrafo.
# Parte de la vista del modelo MVC.   


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from crud_bd import carga_ded_personales
from crud_bd import actualizar_ded_personales


class ConfigDeducciones(object):
    
    def __init__(self, ventana: QDialog):
        
        listado = list()
        listado = carga_ded_personales('2021')
        
        #Obtiene la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3.909)
        alto = float(size.height() / 3.805)

        #Formulario
        super().__init__()

        self.frm_deducciones = ventana
        self.frm_deducciones.setObjectName("frm_deducciones")
        self.frm_deducciones.resize(ancho, alto)
        self.frm_deducciones.setMinimumSize(ancho, alto)
        self.frm_deducciones.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_deducciones.setWindowIcon(icon) 

        self.gridLayout = QGridLayout(self.frm_deducciones)
        self.gridLayout.setObjectName("gridLayout")


        self.lbl_0 = QLabel(self.frm_deducciones)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)

        #Combo box año
        self.comboBox = QComboBox(self.frm_deducciones)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox.addItem('2021')
        self.comboBox.addItem('2022')

        self.comboBox.currentTextChanged.connect(lambda: self.visualiza_valores())

        self.lbl_1 = QLabel(self.frm_deducciones)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 0, 1, 3)
        
        self.txt_conyuge = QLineEdit(self.frm_deducciones)
        self.txt_conyuge.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.txt_conyuge, 1, 3, 1, 2)

        self.lbl_2 = QLabel(self.frm_deducciones)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 2, 0, 1, 1)

        self.txt_hijo = QLineEdit(self.frm_deducciones)
        self.txt_hijo.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.txt_hijo, 2, 3, 1, 2)

        self.lbl_3 = QLabel(self.frm_deducciones)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 3, 0, 1, 3)

        self.txt_hijoinca = QLineEdit(self.frm_deducciones)
        self.txt_hijoinca.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.txt_hijoinca, 3, 3, 1, 2)

        self.lbl_4 = QLabel(self.frm_deducciones)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 4, 0, 1, 2)

        self.txt_noimp = QLineEdit(self.frm_deducciones)
        self.txt_noimp.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.txt_noimp, 4, 3, 1, 2)

        self.lbl_5 = QLabel(self.frm_deducciones)
        self.lbl_5.setObjectName("lbl_5")
        self.gridLayout.addWidget(self.lbl_5, 5, 0, 1, 2)

        self.txt_dedesp = QLineEdit(self.frm_deducciones)
        self.txt_dedesp.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.txt_dedesp, 5, 3, 1, 2)

        try:
            self.txt_conyuge.insert(str(listado[1]))
            self.txt_hijo.insert(str(listado[2]))
            self.txt_hijoinca.insert(str(listado[3]))
            self.txt_noimp.insert(str(listado[0]))
            self.txt_dedesp.insert(str(listado[4]))

        except:
            pass

        self.btn_cerrar = QPushButton(self.frm_deducciones)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 6, 3, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_deducciones.close())

        self.btn_guardar = QPushButton(self.frm_deducciones)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout.addWidget(self.btn_guardar, 6, 4, 1, 1)
        self.btn_guardar.clicked.connect(lambda: self.actualiza_valores())

        QtCore.QMetaObject.connectSlotsByName(self.frm_deducciones)

        _translate = QtCore.QCoreApplication.translate
        self.frm_deducciones.setWindowTitle(_translate("self.frm_deducciones", "Deducciones personales"))
        self.lbl_0.setText(_translate("self.frm_deducciones", "Año:"))
        self.lbl_1.setText(_translate("self.frm_deducciones", "Cónyuge / Unión convivencial:"))
        self.lbl_2.setText(_translate("self.frm_deducciones", "Hijo:"))
        self.lbl_3.setText(_translate("self.frm_deducciones", "Hijo incapacitado para el trabajo:"))
        self.lbl_4.setText(_translate("self.frm_deducciones", "Ganancias no imponibles:"))
        self.lbl_5.setText(_translate("self.frm_deducciones", "Deducción Especial:"))
        self.btn_cerrar.setText(_translate("self.frm_deducciones", "Cerrar"))
        self.btn_guardar.setText(_translate("self.frm_deducciones", "Guardar"))


    def visualiza_valores(self):

        try:

            if self.comboBox.currentText() == '2021':
                listado = list()
                listado = carga_ded_personales('2021')

                self.txt_conyuge.clear()
                self.txt_hijo.clear()
                self.txt_hijoinca.clear()
                self.txt_noimp.clear()
                self.txt_dedesp.clear()

                self.txt_conyuge.insert(str(listado[1]))
                self.txt_hijo.insert(str(listado[2]))
                self.txt_hijoinca.insert(str(listado[3]))
                self.txt_noimp.insert(str(listado[0]))
                self.txt_dedesp.insert(str(listado[4]))

            else:
                listado = list()
                listado = carga_ded_personales('2022')
                self.txt_conyuge.clear()
                self.txt_hijo.clear()
                self.txt_hijoinca.clear()
                self.txt_noimp.clear()
                self.txt_dedesp.clear()
            
                self.txt_conyuge.insert(str(listado[1]))
                self.txt_hijo.insert(str(listado[2]))
                self.txt_hijoinca.insert(str(listado[3]))
                self.txt_noimp.insert(str(listado[0]))
                self.txt_dedesp.insert(str(listado[4]))

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

            
    def actualiza_valores(self):
        
        """
        Actualiza los valores de la tabla deduccionespersonales, del esquema config, obtenidos del
        formulario. Utiliza la función actualizar_ded_personales, del modulo crud_db, para hacerlo.
        """
        
        try:
            ganan_no_imp = float(self.txt_noimp.text())
            conyuge = float(self.txt_conyuge.text())
            hijo = float(self.txt_hijo.text())
            hijo_inca = float(self.txt_hijoinca.text())
            ded_esp = float(self.txt_dedesp.text())

            if self.comboBox.currentText() == '2021':
                actualizar_ded_personales('2021', 'ganan_no_imp', ganan_no_imp)
                actualizar_ded_personales('2021', 'conyuge', conyuge)
                actualizar_ded_personales('2021', 'hijo', hijo)
                actualizar_ded_personales('2021', 'hijo_inca', hijo_inca)
                actualizar_ded_personales('2021', 'ded_esp', ded_esp)

            else:
                actualizar_ded_personales('2022', 'ganan_no_imp', ganan_no_imp)
                actualizar_ded_personales('2022', 'conyuge', conyuge)
                actualizar_ded_personales('2022', 'hijo', hijo)
                actualizar_ded_personales('2022', 'hijo_inca', hijo_inca)
                actualizar_ded_personales('2022', 'ded_esp', ded_esp)

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Se actualizaron los registros de la base de datos.")
            msg_box.setWindowTitle("Información")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon)   
            msg_box.exec()
            
        except ValueError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Se ingresaron datos con formato erroneo. No se actualizan los datos.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
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
