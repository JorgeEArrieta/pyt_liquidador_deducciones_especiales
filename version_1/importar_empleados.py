#Formulario para importar familiares desde archivo ".xlsx".
#Parte del modulo vista del MVC.

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from peewee import InterfaceError
from importacion import lee_empleados
from importacion import guarda_empleado


class ImportarEmpleados(object):

    def __init__(self, ventana: QDialog):

        #Formulario
        super().__init__()

        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 4)
        alto = float(size.height() / 8)

        self.frm_imp_empleado = ventana
        self.frm_imp_empleado.setObjectName("frm_imp_empleado")
        self.frm_imp_empleado.setWindowModality(QtCore.Qt.NonModal)
        self.frm_imp_empleado.resize(ancho, alto)
        self.frm_imp_empleado.setMinimumSize(ancho, alto)
        self.frm_imp_empleado.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_imp_empleado.setWindowIcon(icon)
        
        #Declaración del QGridLayout.
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        #Label
        self.lbl_0 = QLabel(self.frm_imp_empleado)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)
        
        #Caja de texto dirección 
        self.txt_direccion = QLineEdit(self.frm_imp_empleado)
        self.txt_direccion.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.txt_direccion, 1, 0, 1, 3)

        #Tool Button
        self.btn_directorio = QToolButton(self.frm_imp_empleado)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/file-excel-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_directorio.setIcon(icon)
        self.btn_directorio.setObjectName("toolButton")
        self.gridLayout.addWidget(self.btn_directorio, 1, 3, 1, 1)
        self.btn_directorio.clicked.connect(lambda: self.abrir_filedialog())
        
        #Button cerrar
        self.btn_cerrar = QPushButton(self.frm_imp_empleado)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 2, 1, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_imp_empleado.close())

        #Button importar
        self.btn_importar = QPushButton(self.frm_imp_empleado)
        self.btn_importar.setObjectName("btn_importar")
        self.gridLayout.addWidget(self.btn_importar, 2, 2, 1, 1)
        self.btn_importar.clicked.connect(lambda: self.procesa_datos(str(self.txt_direccion.text())))
        

        #Frame
        
        self.frame = QFrame(self.frm_imp_empleado)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        self.progress_bar = QProgressBar(self.frame)
        self.progress_bar.setGeometry(QtCore.QRect(0, 4, (ancho - 20), 20))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 4)
        self.frame.setVisible(False)

        QtCore.QMetaObject.connectSlotsByName(self.frm_imp_empleado)

        _translate = QtCore.QCoreApplication.translate
        self.frm_imp_empleado.setWindowTitle(_translate("frm_imp_empleado", "Importar empleados"))
        self.lbl_0.setText(_translate("frm_imp_empleado", "Archivo a importar:"))
        self.btn_directorio.setText(_translate("frm_imp_empleado", "..."))
        self.btn_cerrar.setText(_translate("frm_imp_empleado", "Cerrar"))
        self.btn_importar.setText(_translate("frm_imp_empleado", "Procesar"))

        self.frm_imp_empleado.setLayout(self.gridLayout)


    def abrir_filedialog(self):

        """
        Abre un widget QfileDialog para que el usuario seleccione el archivo ".xlsx" correspondiente.
        """

        opcion = QFileDialog.Options()
        
        file_name = QFileDialog.getOpenFileName(self.frm_imp_empleado,"Seleccionar archivo", "",
                                                "Archivos excel (*xlsx);; All Files (*)", options = opcion)

        self.txt_direccion.clear()
        self.txt_direccion.insert(file_name[0])


    def procesa_datos(self, archivo):

        try:
            screen = QApplication.primaryScreen()
            size = screen.size()
            ancho = float(size.width() / 4)
            alto = float(size.height() / 5)

            self.frame.setVisible(True)
            self.frm_imp_empleado.setEnabled(False)
            self.frm_imp_empleado.resize(ancho, alto)
            self.frm_imp_empleado.setMinimumSize(ancho, alto)
            self.frm_imp_empleado.setMaximumSize(ancho, alto)

            x = 0

            registros = lee_empleados(archivo)

            largo = 100 / len(registros.index)

            count = 1
         
            for registro in registros.values:

                guarda_empleado(registro[0], registro[1], registro[2], registro[3])
 
                x += largo
                count += 1
     
                self.progress_bar.setValue(x)
     
                if count == len(registros.index) + 1:
                    
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setText("Finalizo el proceso de importación de datos.")
                    msg_box.setWindowTitle("Información")
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    msg_box.setWindowIcon(icon) 
                    msg_box.exec()

                    self.frm_imp_empleado.close()

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

            self.frm_imp_empleado.close()

        
        except AttributeError:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en la ejecución.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()
    
            self.frm_imp_empleado.close()
        
        
        except FileNotFoundError:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Falta seleccionar el archivo a procesar.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()

            self.frame.setVisible(False)
            self.frm_imp_empleado.setEnabled(True)

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