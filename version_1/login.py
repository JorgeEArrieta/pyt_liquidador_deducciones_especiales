# Formulario de login.

# Parte de la vista del modelo mvc.

from PyQt5 import QtCore
from PyQt5 import QtGui 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from users import Usuario
from main import MainForm


class Login(object):

    def __init__(self, frm_login):

        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 4.5)
        alto = float(size.height() / 2.5)

        self.intentos = 1

        super().__init__()

        #Formulario
        self.frm_login = frm_login
        self.frm_login.setObjectName("frm_login")
        self.frm_login.resize(ancho, alto)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_login.setWindowIcon(icon)

        #Frame principal y layout.
        self.main_frame = QWidget()
        self.frm_login.setCentralWidget(self.main_frame)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        #Frame para el label marca.
        self.frame = QFrame(frm_login)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.259594 rgba(24, 0, 32, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        
        #Label Payroll tools
        self.lbl_0 = QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_0.setFont(font)
        self.lbl_0.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "")
        self.lbl_0.setFrameShape(QFrame.NoFrame)
        self.lbl_0.setScaledContents(False)
        self.lbl_0.setWordWrap(False)
        self.lbl_0.setOpenExternalLinks(True)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        
        #Label 
        self.lbl_2 = QLabel(frm_login)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_2.setFont(font)
        self.lbl_2.setObjectName("lbl_2")
        self.verticalLayout.addWidget(self.lbl_2)
        
        #Textbox usuario
        self.txt_user = QLineEdit(frm_login)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.txt_user.setFont(font)
        self.txt_user.setObjectName("txt_user")
        self.verticalLayout.addWidget(self.txt_user)
        
        #Label
        self.lbl_3 = QLabel(frm_login)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_3.setFont(font)
        self.lbl_3.setObjectName("lbl_3")
        self.verticalLayout.addWidget(self.lbl_3)
        
        
        self.txt_password = QLineEdit(frm_login)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.txt_password.setFont(font)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.txt_password)
        
        #Label
        self.lbl_4 = QLabel(frm_login)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_4.setFont(font)
        self.lbl_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.lbl_4.setScaledContents(False)
        self.lbl_4.setWordWrap(True)
        self.lbl_4.setOpenExternalLinks(False)
        self.lbl_4.setObjectName("lbl_4")
        self.lbl_4.setVisible(False)
        self.verticalLayout.addWidget(self.lbl_4)
        
        #Botón aceptar
        self.btn_aceptar = QPushButton(frm_login)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.btn_aceptar.setFont(font)
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.verticalLayout.addWidget(self.btn_aceptar)
        self.btn_aceptar.clicked.connect(lambda: self.login())

        #Botón cerrar
        self.btn_cancelar = QPushButton(frm_login)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.verticalLayout.addWidget(self.btn_cancelar)
        self.btn_cancelar.clicked.connect(lambda: self.frm_login.close())

        QtCore.QMetaObject.connectSlotsByName(frm_login)


        _translate = QtCore.QCoreApplication.translate
        self.frm_login.setWindowTitle(_translate("frm_login", "Login"))
        self.lbl_0.setText(_translate("frm_login", "Payroll tools"))
        self.lbl_2.setText(_translate("frm_login", "Usuario"))
        self.lbl_3.setText(_translate("frm_login", "Contraseña"))
        self.lbl_4.setText(_translate("frm_login", "Usuario ya en uso. conctactese con el proovedor."))
        self.btn_aceptar.setText(_translate("frm_login", "Aceptar"))
        self.btn_cancelar.setText(_translate("frm_login", "Cancelar"))

        self.main_frame.setLayout(self.verticalLayout)


    def login(self):

        """
        Función para verificar el usuario y contraseña.
        """
        try:

            user = str(self.txt_user.text())
            password = str(self.txt_password.text())
        
            usuario = Usuario() 

            if self.intentos < 3:

                if usuario.verifica_user(user, password) == True:

                    if usuario.verifica_estado(user, password) == True:

                        usuario.actualiza_estado(user, 'conectado')  
                        usuario.actualiza_ip(user)   
                        usuario.cerrar_conexion()
                        self.frm_login.destroy()
                        frm_main = QMainWindow()
                        frm_main.show()
                        MainForm(ventana = frm_main, usuario = user)

                    else:
                        _translate = QtCore.QCoreApplication.translate
                        self.lbl_4.setText(_translate("frm_login", "Usuario ya conectado. Contactese con el proveedor."))
                        self.lbl_4.setVisible(True)

                else:
                    _translate = QtCore.QCoreApplication.translate
                    self.lbl_4.setText(_translate("frm_login", "Usuario y/o contraseña incorrecta."))
                    self.lbl_4.setVisible(True)
                    self.intentos += 1
    
            else:

                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setText("Número de intentos de logueo excedidos. Se cierra la aplicación.")
                msg_box.setWindowTitle("Error")
                msg_box.setStandardButtons(QMessageBox.Ok)
                #msg_box.buttonClicked.connect(msgButtonClick)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("img/windows/error.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                msg_box.setWindowIcon(icon)
                msg_box.exec()

                usuario.cerrar_conexion()
            
                self.frm_login.destroy()

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