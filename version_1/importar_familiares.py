#Módulo que contiene el formulario para importar datos relacionados a deducciones de cargas de fámilia.
#La importación se podra realizar desde un archivo ".xlsx" o, mismo, desde los propios formularios 572.
# Parte de la vista del modelo MVC.


from peewee import InterfaceError
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from importacion import leer_directorio
from importacion import lee_familiares_xml
from importacion import lee_familiares_xlsx
from importacion import guarda_familiar
from importacion import obtiene_fecha


class ImportarCFamilia(object):

    def __init__(self, ventana: QDialog):

        super().__init__()

        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3)
        alto = float(size.height() / 7)

        #Formulario
        self.frm_importa_familiares = ventana
        self.frm_importa_familiares.setObjectName("frm_importa_familiares")
        self.frm_importa_familiares.resize(ancho, alto)
        self.frm_importa_familiares.setMinimumSize(ancho, alto)
        self.frm_importa_familiares.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_importa_familiares.setWindowIcon(icon) 

        
        #Layout
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        #Label
        self.lbl_0 = QLabel(self.frm_importa_familiares)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)
        
        #ComboBox
        self.cmb_opciones = QComboBox(self.frm_importa_familiares)
        self.cmb_opciones.setObjectName("comboBox")
        self.gridLayout.addWidget(self.cmb_opciones, 0, 1, 1, 3)
        self.cmb_opciones.addItem('Desde formulario 572')
        self.cmb_opciones.addItem('Desde archivo .xlsx')
        self.cmb_opciones.currentTextChanged.connect(lambda: self.on_cmb_changed())

        #Label
        self.lbl_1 = QLabel(self.frm_importa_familiares)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 1, 0, 1, 1)
        
        #Caja de texto.
        self.txt_direccion = QLineEdit(self.frm_importa_familiares)
        self.txt_direccion.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.txt_direccion, 1, 1, 1, 2)

        #Tool button
        self.btn_abrarc = QToolButton(self.frm_importa_familiares)
        self.btn_abrarc.setObjectName("toolButton")
        icon_excel = QtGui.QIcon()
        icon_excel.addPixmap(QtGui.QPixmap("img/file-excel-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_abrarc.setIcon(icon_excel)
        self.gridLayout.addWidget(self.btn_abrarc, 1, 3, 1, 1)
        self.btn_abrarc.clicked.connect(lambda: self.abrir_arc_dialog())
        self.btn_abrarc.setVisible(False)

        #Tool button
        self.btn_abrdir = QToolButton(self.frm_importa_familiares)
        self.btn_abrdir.setObjectName("toolButton")
        icon_dir = QtGui.QIcon()
        icon_dir.addPixmap(QtGui.QPixmap("img/archive-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_abrdir.setIcon(icon_dir)
        self.gridLayout.addWidget(self.btn_abrdir, 1, 3, 1, 1)
        self.btn_abrdir.clicked.connect(lambda: self.abrir_dir_dialog())
        
        #Botón cerrar.
        self.btn_cerrar = QPushButton(self.frm_importa_familiares)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 2, 1, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_importa_familiares.close())
        
        #Boton importar
        self.btn_importar = QPushButton(self.frm_importa_familiares)
        self.btn_importar.setObjectName("btn_importar")
        self.gridLayout.addWidget(self.btn_importar, 2, 2, 1, 1)
        self.btn_importar.clicked.connect(lambda: self.procesar_datos())
        
        #Frame y progress bar
        self.frame = QFrame(self.frm_importa_familiares)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.progress_bar = QProgressBar(self.frame)
        self.progress_bar.setGeometry(QtCore.QRect(10, 0, (ancho - 22), 23))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 4)
        self.frame.setVisible(False)

        QtCore.QMetaObject.connectSlotsByName(self.frm_importa_familiares)

        _translate = QtCore.QCoreApplication.translate
        self.frm_importa_familiares.setWindowTitle(_translate("frm_importa_familiares", "Importa familiares"))
        self.lbl_0.setText(_translate("frm_importa_familiares", "Importar desde:"))
        self.lbl_1.setText(_translate("frm_importa_familiares", "Seleccionar archivo:"))
        self.btn_abrarc.setText(_translate("frm_importa_familiares", "..."))
        self.btn_cerrar.setText(_translate("frm_importa_familiares", "Cerrar"))
        self.btn_importar.setText(_translate("frm_importa_familiares", "Importar"))

        self.frm_importa_familiares.setLayout(self.gridLayout)


    def on_cmb_changed(self):

        """
        Realiza modificaciones en el formulario a partir de los datos obtenidos del combo box.
        """

        if self.cmb_opciones.currentText() == 'Desde archivo .xlsx':
            _translate = QtCore.QCoreApplication.translate
            self.lbl_1.setText(_translate("frm_importa_familiares", "Seleccionar archivo:"))
            self.btn_abrarc.setVisible(True)
            self.btn_abrdir.setVisible(False)
            
        elif self.cmb_opciones.currentText() == 'Desde formulario 572':
            _translate = QtCore.QCoreApplication.translate
            self.lbl_1.setText(_translate("frm_importa_familiares", "Seleccionar directorio:"))
            self.btn_abrarc.setVisible(False)
            self.btn_abrdir.setVisible(True)
        
            
    def abrir_arc_dialog(self):

        """
        Abre un widget QFileDialog que permite seleccionar al usuario un archivo.
        """

        opcion = QFileDialog.Options()
        archivo = QFileDialog.getOpenFileName(self.frm_importa_familiares,"Seleccionar archivo", "",
                                              "Archivos excel (*xlsx);; All Files (*)", options = opcion)

        self.txt_direccion.clear()
        self.txt_direccion.insert(archivo[0])


    def abrir_dir_dialog(self):

        """
        Abre un widget QFileDialog que permite seleccionar al usuario un directorio.
        """

        opcion = QFileDialog.Options()
        directorio = QFileDialog.getExistingDirectory(self.frm_importa_familiares,"Seleccionar directorio","",
                                                      opcion)
        
        self.txt_direccion.clear()
        self.txt_direccion.insert(directorio)


    def procesa_datos_xml(self, directorio):
        
        try:
            screen = QApplication.primaryScreen()
            size = screen.size()
            ancho = float(size.width() / 3)
            alto = float(size.height() / 6)
            
            self.frm_importa_familiares.resize(ancho, alto)
            self.frm_importa_familiares.setMinimumSize(ancho, alto)
            self.frm_importa_familiares.setMaximumSize(ancho, alto)
            self.frame.setVisible(True)
            self.frm_importa_familiares.setEnabled(False)
        
            x = 0
            count = 1
 
            registros = leer_directorio(directorio)
        
            largo = 100 / len(registros)
     
            for registro in registros:
                
                try:  
        
                    datos_familiar = lee_familiares_xml(registro)

                    for i in datos_familiar:
                        guarda_familiar(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
            
                    x += largo
                    count +=1
 
                    self.progress_bar.setValue(x)
 
                    if count == len(registros) + 1:
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setText("Finalizo el proceso de importación de datos.")
                        msg_box.setWindowTitle("Información")
                        msg_box.setStandardButtons(QMessageBox.Ok)
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        msg_box.setWindowIcon(icon) 
                        msg_box.exec()

                        self.frm_importa_familiares.close()

                        break
            
                except IndexError:
    
                    x += largo
                
                    hora = obtiene_fecha()

                    txt = open(f'logs/insert_cargasfam {hora}.txt', 'a')
                    txt.write(f'Error en la lectura del xml {i[0]}. Revisar que exista un legajo asociado para el número de cuil.\n')
                    self.frm_importa_familiares.close()

                    if count == len(registros) + 1:
                    
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setText("Finalizo el proceso de importación de datos.")
                        msg_box.setWindowTitle("Información")
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        msg_box.setWindowIcon(icon) 
                        msg_box.setStandardButtons(QMessageBox.Ok)
                        
                        msg_box.exec()

                        self.frm_importa_familiares.close()

                        break
        
        except InterfaceError:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en conexión a base de datos.")
            msg_box.setWindowTitle("Error")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()

            self.frm_importa_familiares.close()

        except FileNotFoundError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en lectura del archivo seleccionado.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()
    
            self.frame.setVisible(False)
            self.frm_importa_familiares.setEnabled(True)

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
    
            self.frm_importa_familiares.close()

            
    def procesa_datos_xlsx(self, archivo):

        try:

            screen = QApplication.primaryScreen()
            size = screen.size()
            ancho = float(size.width() / 3)
            alto = float(size.height() / 6)
            
            self.frm_importa_familiares.resize(ancho, alto)
            self.frm_importa_familiares.setMinimumSize(ancho, alto)
            self.frm_importa_familiares.setMaximumSize(ancho, alto)
            self.frame.setVisible(True)
            self.frm_importa_familiares.setEnabled(False)
              
            x = 0
            count = 1

            registros = lee_familiares_xlsx(archivo)
            largo = 100 / len(registros.index)

            for i in registros.values:
            
                try:
                
                    guarda_familiar(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
                
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

                        self.frm_importa_familiares.close()

                        break

                except IndexError:
    
                    x += largo
                
                    hora = obtiene_fecha()

                    txt = open(f'logs/insert_cargasfam {hora}.txt', 'a')
                    txt.write(f'Error en la lectura del xml {i[0]}. Revisar que exista un legajo asociado para el número de cuil.\n')
                    self.frm_importa_familiares.close()

                    if count == len(registros.index) + 1:
                    
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setText("Se crearon los registros en la base de datos.")
                        msg_box.setWindowTitle("Información")
                        msg_box.setStandardButtons(QMessageBox.Ok)
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        msg_box.setWindowIcon(icon) 
                        msg_box.exec()

                        self.frm_importa_familiares.close()

                        break

        except InterfaceError:

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en conexión a base de datos.")
            msg_box.setWindowTitle("Información")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()
            
            self.frm_importa_familiares.close()

        except AttributeError:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en la ejecución. Revisar conexión a base de datos o log de importación.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()
    
            self.frm_importa_familiares.close()

        except FileNotFoundError:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en lectura del archivo seleccionado.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()

            self.frame.setVisible(False)

            self.frm_importa_familiares.setEnabled(True)

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
            
            self.frm_importa_familiares.close()
            

    def procesar_datos(self):

        """
        Llama a la opción correspondiente de procesamiento de datos, según la opción elegida por el usuario.
        """

        try:

            if self.cmb_opciones.currentText() == 'Desde archivo .xlsx':
                self.procesa_datos_xlsx(self.txt_direccion.text())
            
            else:
                self.procesa_datos_xml(self.txt_direccion.text())

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
    
            self.frm_importa_familiares.close()