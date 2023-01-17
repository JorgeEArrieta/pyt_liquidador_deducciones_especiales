# Formulario para procesar el calculo de los beneficios correspondientes al primer y segundo párrafo del
# del impuesto a las ganancias.

#Parte de la vista del modelo MVC


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog 
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from peewee import InterfaceError
from errores import MesInicial
from errores import LegajoInicial
from liquidador import legajos_activos
from liquidador import liquida




class Liquidador(object):

    def __init__(self, ventana: QDialog):

        super().__init__()

        #Obtiene la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3.119)
        alto = float(size.height() / 4.21)
        
        self.frm_liquidador = ventana
        self.frm_liquidador.setObjectName("frm_liquidador")
        self.frm_liquidador.resize(ancho, alto)
        self.frm_liquidador.setMinimumSize(ancho, alto)
        self.frm_liquidador.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_liquidador.setWindowIcon(icon) 

        self.gridLayout = QGridLayout(self.frm_liquidador)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_4 = QLabel(self.frm_liquidador)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 0, 0, 1, 1)

        self.cmb_year = QComboBox(self.frm_liquidador)
        self.cmb_year.setObjectName("cmb_year")
        self.gridLayout.addWidget(self.cmb_year, 0, 1, 1, 2)
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')

        self.lbl_0 = QLabel(self.frm_liquidador)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 1, 0, 1, 1)

        self.cmb_mes_desde = QComboBox(self.frm_liquidador)
        self.cmb_mes_desde.setObjectName("cmb_mes_desde")
        self.gridLayout.addWidget(self.cmb_mes_desde, 1, 1, 1, 2)
        
        i = 1
        while i <= 12:
            self.cmb_mes_desde.addItem(str(i))
            i += 1

        self.lbl_1 = QLabel(self.frm_liquidador)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 3, 1, 1)

        self.cmb_mes_hasta = QComboBox(self.frm_liquidador)
        self.cmb_mes_hasta.setObjectName("cmb_mes_hasta")
        self.gridLayout.addWidget(self.cmb_mes_hasta, 1, 4, 1, 1)
        
        i = 1
        while i <= 12:
            self.cmb_mes_hasta.addItem(str(i))
            i += 1

        self.lbl_2 = QLabel(self.frm_liquidador)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 2, 0, 1, 1)

        self.txt_lg_desde = QLineEdit(self.frm_liquidador)
        self.txt_lg_desde.setObjectName("txt_lg_desde")
        self.gridLayout.addWidget(self.txt_lg_desde, 2, 1, 1, 2)
        
        self.lbl_3 = QLabel(self.frm_liquidador)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 2, 3, 1, 1)

        self.txt_lg_hasta = QLineEdit(self.frm_liquidador)
        self.txt_lg_hasta.setObjectName("txt_lg_hasta")
        self.gridLayout.addWidget(self.txt_lg_hasta, 2, 4, 1, 2)

        self.btn_cerrar = QPushButton(self.frm_liquidador)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 3, 4, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_liquidador.close())

        self.btn_procesar = QPushButton(self.frm_liquidador)
        self.btn_procesar.setObjectName("btn_procesar")
        self.gridLayout.addWidget(self.btn_procesar, 3, 5, 1, 1)
        self.btn_procesar.clicked.connect(lambda: self.procesa())

        self.line = QFrame(self.frm_liquidador)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 6)
        self.line.setVisible(False)


        self.lbl_5 = QLabel(self.frm_liquidador)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lbl_5.setFont(font)
        self.lbl_5.setObjectName("lbl_5")
        self.gridLayout.addWidget(self.lbl_5, 5, 0, 1, 2)
        self.lbl_5.setVisible(False)

        self.lbl_6 = QLabel(self.frm_liquidador)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_6.setFont(font)
        self.lbl_6.setObjectName("label")
        self.gridLayout.addWidget(self.lbl_6, 5, 2, 1, 1)
        self.lbl_6.setVisible(False)

        self.progress_bar = QProgressBar(self.frm_liquidador)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progress_bar, 6, 0, 1, 6)
        self.progress_bar.setVisible(False)

        QtCore.QMetaObject.connectSlotsByName(self.frm_liquidador)

        _translate = QtCore.QCoreApplication.translate
        self.frm_liquidador.setWindowTitle(_translate("self.frm_liquidador", "Calculo deducciones incrementadas"))
        self.lbl_4.setText(_translate("self.frm_liquidador", "Año:"))
        self.lbl_0.setText(_translate("self.frm_liquidador", "Mes desde:"))
        self.lbl_1.setText(_translate("self.frm_liquidador", "Mes hasta:"))
        self.lbl_2.setText(_translate("self.frm_liquidador", "Legajo desde:"))
        self.lbl_3.setText(_translate("self.frm_liquidador", "Legajo hasta:"))
        self.btn_cerrar.setText(_translate("self.frm_liquidador", "Cerrar"))
        self.btn_procesar.setText(_translate("self.frm_liquidador", "Procesar"))
        self.lbl_5.setText(_translate("self.frm_liquidador", "Liquidando mes:"))
        self.lbl_6.setText(_translate("self.frm_liquidador", "-"))


    def procesa(self):
        
        try:
        
            #Modifica widgets
            self.lbl_5.setVisible(True)
            self.lbl_6.setVisible(True)
            self.progress_bar.setVisible(True)
            self.line.setVisible(True)
            self.frm_liquidador.setEnabled(False)
    
            #Obtiene datos.
            year = int(self.cmb_year.currentText())
            mes_desde = int(self.cmb_mes_desde.currentText())
            mes_hasta = int(self.cmb_mes_hasta.currentText())
            lg_desde = int(self.txt_lg_desde.text())
            lg_hasta = int(self.txt_lg_hasta.text())
    
            #Valida datos cargados
            if int(mes_desde) > int(mes_hasta):
                raise MesInicial
        
            if int(lg_desde) > int(lg_hasta):
                raise LegajoInicial

            mes = mes_desde

            while mes <= mes_hasta:

                self.lbl_6.setText(str(mes))
            
                lista_empleados = legajos_activos(lg_desde, lg_hasta, year, mes)
            
                largo = 100 / len(lista_empleados)
            
                x = 0

                for empleado in lista_empleados:

                    liquida(empleado, mes, year)

                    x += largo

                    self.progress_bar.setValue(x)

                mes += 1

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Proceso de liquidación finalizado.")
            msg_box.setWindowTitle("Información")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()

            self.frm_liquidador.close()

        except ValueError:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Datos ingresados erroneos.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()

            #Modifica widgets
            self.lbl_5.setVisible(False)
            self.lbl_6.setVisible(False)
            self.progress_bar.setVisible(False)
            self.line.setVisible(False)
            self.frm_liquidador.setEnabled(True)
        
        except InterfaceError:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en conexión a base de datos.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()

            #Modifica widgets
            self.lbl_5.setVisible(False)
            self.lbl_6.setVisible(False)
            self.progress_bar.setVisible(False)
            self.line.setVisible(False)
            self.frm_liquidador.setEnabled(True)

            self.frm_liquidador.close()

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
    
            #Modifica widgets
            self.lbl_5.setVisible(False)
            self.lbl_6.setVisible(False)
            self.progress_bar.setVisible(False)
            self.line.setVisible(False)
            self.frm_liquidador.setEnabled(True)
            
            self.frm_liquidador.close()