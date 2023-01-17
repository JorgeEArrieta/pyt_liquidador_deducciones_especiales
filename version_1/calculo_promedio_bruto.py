# Formulario para procesar el calculo del promedio para determinar si corresponde el beneficio del primer,
# o segundo párrafo, de ganancias.

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
from liquidador import promedio_bruto
from liquidador import elimina_promedio
from liquidador import guarda_promedio

class PromedioBruto(object):

    def __init__(self, ventana: QDialog):

        super().__init__()

        #Obtiene la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3.119)
        alto = float(size.height() / 4.21)
        
        self.frm_promedio_bruto = ventana
        self.frm_promedio_bruto.setObjectName("self.frm_promedio_bruto")
        self.frm_promedio_bruto.resize(ancho, alto)
        self.frm_promedio_bruto.setMinimumSize(ancho, alto)
        self.frm_promedio_bruto.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_promedio_bruto.setWindowIcon(icon) 

        self.gridLayout = QGridLayout(self.frm_promedio_bruto)
        self.gridLayout.setObjectName("gridLayout")

        self.lbl_4 = QLabel(self.frm_promedio_bruto)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 0, 0, 1, 1)

        self.cmb_year = QComboBox(self.frm_promedio_bruto)
        self.cmb_year.setObjectName("cmb_year")
        self.gridLayout.addWidget(self.cmb_year, 0, 1, 1, 2)
        self.cmb_year.addItem('2021')
        self.cmb_year.addItem('2022')

        self.lbl_0 = QLabel(self.frm_promedio_bruto)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 1, 0, 1, 1)

        self.cmb_mes_desde = QComboBox(self.frm_promedio_bruto)
        self.cmb_mes_desde.setObjectName("cmb_mes_desde")
        self.gridLayout.addWidget(self.cmb_mes_desde, 1, 1, 1, 2)
        
        i = 1
        while i <= 12:
            self.cmb_mes_desde.addItem(str(i))
            i += 1

        self.lbl_1 = QLabel(self.frm_promedio_bruto)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 3, 1, 1)

        self.cmb_mes_hasta = QComboBox(self.frm_promedio_bruto)
        self.cmb_mes_hasta.setObjectName("cmb_mes_hasta")
        self.gridLayout.addWidget(self.cmb_mes_hasta, 1, 4, 1, 1)
        
        i = 1
        while i <= 12:
            self.cmb_mes_hasta.addItem(str(i))
            i += 1

        self.lbl_2 = QLabel(self.frm_promedio_bruto)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 2, 0, 1, 1)

        self.txt_lg_desde = QLineEdit(self.frm_promedio_bruto)
        self.txt_lg_desde.setObjectName("txt_lg_desde")
        self.gridLayout.addWidget(self.txt_lg_desde, 2, 1, 1, 2)
        
        self.lbl_3 = QLabel(self.frm_promedio_bruto)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 2, 3, 1, 1)

        self.txt_lg_hasta = QLineEdit(self.frm_promedio_bruto)
        self.txt_lg_hasta.setObjectName("txt_lg_hasta")
        self.gridLayout.addWidget(self.txt_lg_hasta, 2, 4, 1, 2)

        self.btn_cerrar = QPushButton(self.frm_promedio_bruto)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 3, 4, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_promedio_bruto.close())

        self.btn_procesar = QPushButton(self.frm_promedio_bruto)
        self.btn_procesar.setObjectName("btn_procesar")
        self.gridLayout.addWidget(self.btn_procesar, 3, 5, 1, 1)
        self.btn_procesar.clicked.connect(lambda: self.liquida_bruto())

        self.line = QFrame(self.frm_promedio_bruto)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 6)
        self.line.setVisible(False)

        self.lbl_5 = QLabel(self.frm_promedio_bruto)
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

        self.lbl_6 = QLabel(self.frm_promedio_bruto)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_6.setFont(font)
        self.lbl_6.setObjectName("label")
        self.gridLayout.addWidget(self.lbl_6, 5, 2, 1, 1)
        self.lbl_6.setVisible(False)

        self.progress_bar = QProgressBar(self.frm_promedio_bruto)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progress_bar, 6, 0, 1, 6)
        self.progress_bar.setVisible(False)

        QtCore.QMetaObject.connectSlotsByName(self.frm_promedio_bruto)

        _translate = QtCore.QCoreApplication.translate
        self.frm_promedio_bruto.setWindowTitle(_translate("self.frm_promedio_bruto", "Calculo promedio bruto"))
        self.lbl_4.setText(_translate("self.frm_promedio_bruto", "Año:"))
        self.lbl_0.setText(_translate("self.frm_promedio_bruto", "Mes desde:"))
        self.lbl_1.setText(_translate("self.frm_promedio_bruto", "Mes hasta:"))
        self.lbl_2.setText(_translate("self.frm_promedio_bruto", "Legajo desde:"))
        self.lbl_3.setText(_translate("self.frm_promedio_bruto", "Legajo hasta:"))
        self.btn_cerrar.setText(_translate("self.frm_promedio_bruto", "Cerrar"))
        self.btn_procesar.setText(_translate("self.frm_promedio_bruto", "Procesar"))
        self.lbl_5.setText(_translate("self.frm_promedio_bruto", "Liquidando mes:"))
        self.lbl_6.setText(_translate("self.frm_promedio_bruto", "-"))


    def liquida_bruto(self):

        try:
        
            #Modifica widgets
            self.lbl_5.setVisible(True)
            self.lbl_6.setVisible(True)
            self.progress_bar.setVisible(True)
            self.line.setVisible(True)
            self.frm_promedio_bruto.setEnabled(False)

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

                    resultado = promedio_bruto(year, empleado, mes)

                    elimina_promedio(empleado, year, mes)

                    mensaje = f'{resultado[0]} - {resultado[1]} - {resultado[2]} - {resultado[3]}' 
                    
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setText(str(mensaje))
                    msg_box.setWindowTitle("Información")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    msg_box.setWindowIcon(icon) 
                    
                    guarda_promedio(resultado[0], resultado[1], resultado[2], resultado[3])

                    x += largo
                    
                    self.progress_bar.setValue(x)

                if mes == mes_hasta:
                
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setText("Finalizo el proceso de importación de datos.")
                    msg_box.setWindowTitle("Información")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    msg_box.setWindowIcon(icon) 
                    msg_box.exec()
    
                    self.frm_promedio_bruto.close()

                mes += 1


        except MesInicial:
            
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("El mes de inicio no puede ser menor al de finalización.")
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
            self.frm_promedio_bruto.setEnabled(True)
            

        except LegajoInicial:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("El legajo de inicio no puede ser menor al de finalización.")
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
            self.frm_promedio_bruto.setEnabled(True)
            

        except ValueError:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en los datos ingresados.")
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
            self.frm_promedio_bruto.setEnabled(True)
            

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

            self.frm_promedio_bruto.close()

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
    
            self.frm_promedio_bruto.close()