# Formulario para configurar cuales son los items que se toman, de otros empleadores, a la hora de calcular el
# promedio bruto y las deducción especial incrementada primera parte. 

# Parte de la vista del modelo MVC.


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGridLayout
from importacion import lee_par_gananoe
from importacion import actualiza_par_gananoe


class ConfigGananOE(QDialog):
    
    def __init__(self, ventana: QDialog):
        
        #Obtiene la resolución de pantalla
        screen = QApplication.primaryScreen()
        size = screen.size()
        ancho = float(size.width() / 3.177)
        alto = float(size.height() / 3.63)

        #Configuración del formulario.
        super().__init__()

        self.frm_config_gananoe = ventana
        self.frm_config_gananoe.setObjectName("frm_config_gananoe")
        self.frm_config_gananoe.resize(ancho, alto)
        self.frm_config_gananoe.setMinimumSize(ancho, alto)
        self.frm_config_gananoe.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_config_gananoe.setWindowIcon(icon)

        self.gridLayout = QGridLayout(self.frm_config_gananoe)
        self.gridLayout.setObjectName("gridLayout")

        self.chk_ganbruta = QCheckBox(self.frm_config_gananoe)
        self.chk_ganbruta.setChecked(True)
        self.chk_ganbruta.setObjectName("chk_ganbruta")
        self.gridLayout.addWidget(self.chk_ganbruta, 0, 0, 1, 1)
        
        self.chk_sac = QCheckBox(self.frm_config_gananoe)
        self.chk_sac.setObjectName("chk_sac")
        self.gridLayout.addWidget(self.chk_sac, 0, 1, 1, 1)

        self.chk_gannohab = QCheckBox(self.frm_config_gananoe)
        self.chk_gannohab.setObjectName("chk_gannohab")
        self.gridLayout.addWidget(self.chk_gannohab, 1, 0, 1, 1)

        self.chk_hsextgrav = QCheckBox(self.frm_config_gananoe)
        self.chk_hsextgrav.setObjectName("chk_hsextgrav")
        self.gridLayout.addWidget(self.chk_hsextgrav, 1, 1, 1, 2)

        self.chk_retganan = QCheckBox(self.frm_config_gananoe)
        self.chk_retganan.setObjectName("chk_retganan")
        self.gridLayout.addWidget(self.chk_retganan, 2, 0, 1, 1)

        self.chk_hsextex = QCheckBox(self.frm_config_gananoe)
        self.chk_hsextex.setObjectName("chk_hsextex")
        self.gridLayout.addWidget(self.chk_hsextex, 2, 1, 1, 2)

        self.chk_ajuste = QCheckBox(self.frm_config_gananoe)
        self.chk_ajuste.setObjectName("chk_ajuste")
        self.gridLayout.addWidget(self.chk_ajuste, 3, 0, 1, 1)

        self.chk_matdid = QCheckBox(self.frm_config_gananoe)
        self.chk_matdid.setObjectName("chk_matdid")
        self.gridLayout.addWidget(self.chk_matdid, 3, 1, 1, 2)

        self.chk_remuexen = QCheckBox(self.frm_config_gananoe)
        self.chk_remuexen.setObjectName("chk_remuexen")
        self.gridLayout.addWidget(self.chk_remuexen, 4, 0, 1, 1)

        self.chk_gastmov = QCheckBox(self.frm_config_gananoe)
        self.chk_gastmov.setChecked(True)
        self.chk_gastmov.setTristate(False)
        self.chk_gastmov.setObjectName("chk_gastmov")
        self.gridLayout.addWidget(self.chk_gastmov, 4, 1, 1, 2)

        self.btn_cerrar = QPushButton(self.frm_config_gananoe)
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.gridLayout.addWidget(self.btn_cerrar, 5, 1, 1, 1)
        self.btn_cerrar.clicked.connect(lambda: self.frm_config_gananoe.close())

        self.btn_guardar = QPushButton(self.frm_config_gananoe)
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout.addWidget(self.btn_guardar, 5, 2, 1, 1)
        self.btn_guardar.clicked.connect(lambda: self.lee_chkbox())

        self.act_chkbox()

        QtCore.QMetaObject.connectSlotsByName(self.frm_config_gananoe)

        _translate = QtCore.QCoreApplication.translate
        self.frm_config_gananoe.setWindowTitle(_translate("self.frm_config_gananoe", "Configuración ganancias otros empleadores"))
        self.chk_ganbruta.setText(_translate("self.frm_config_gananoe", "Ganancia bruta"))
        self.chk_sac.setText(_translate("self.frm_config_gananoe", "SAC"))
        self.chk_gannohab.setText(_translate("self.frm_config_gananoe", "Ganancias no habituales"))
        self.chk_hsextgrav.setText(_translate("self.frm_config_gananoe", "Hs. Extras gravadas"))
        self.chk_retganan.setText(_translate("self.frm_config_gananoe", "Retención ganancias"))
        self.chk_hsextex.setText(_translate("self.frm_config_gananoe", "Hs. Extras exentas"))
        self.chk_ajuste.setText(_translate("self.frm_config_gananoe", "Ajuste"))
        self.chk_matdid.setText(_translate("self.frm_config_gananoe", "Material didáctico"))
        self.chk_remuexen.setText(_translate("self.frm_config_gananoe", "Remuneración exenta / No alcanzada"))
        self.chk_gastmov.setText(_translate("self.frm_config_gananoe", "Gastos movilidad / viaticos"))
        self.btn_cerrar.setText(_translate("self.frm_config_gananoe", "Cerrar"))
        self.btn_guardar.setText(_translate("self.frm_config_gananoe", "Guardar"))



    def act_chkbox(self):
        
        """
        Verifica en la tabla el valor de los parametros de ganancias y actualiza los checkbox a partir de ellos.
        """

        try:

            #Ganancia bruta
            if lee_par_gananoe('gan_brut') == 1:
                self.chk_ganbruta.setChecked(True)
            else:
                self.chk_ganbruta.setChecked(False)

            #Retención ganancias
            if lee_par_gananoe('ret_gan') == 1:
                self.chk_retganan.setChecked(True)
            else:
                self.chk_retganan.setChecked(False)

            #Retribuciones no habituales
            if lee_par_gananoe('retrib_nohab') == 1:
                self.chk_gannohab.setChecked(True)
            else:
                self.chk_gannohab.setChecked(False)

            #Ajuste
            if lee_par_gananoe('ajuste') == 1:
                self.chk_ajuste.setChecked(True)
            else:
                self.chk_ajuste.setChecked(False) 

            #Remuneración exenta
            if lee_par_gananoe('exe_noalc') == 1:
                self.chk_remuexen.setChecked(True)
            else:
                self.chk_remuexen.setChecked(False) 

            #SAC
            if lee_par_gananoe('sac') == 1:
                self.chk_sac.setChecked(True)
            else:
                self.chk_sac.setChecked(False)

            #Horas extras exentas.
            if lee_par_gananoe('horas_extex') == 1:
                self.chk_hsextex.setChecked(True)
            else:
                self.chk_hsextex.setChecked(False) 

            #Horas extras gravadas.
            if lee_par_gananoe('horas_extgr') == 1:
                self.chk_hsextgrav.setChecked(True)
            else:
                self.chk_hsextgrav.setChecked(False) 

            #Material didactico
            if lee_par_gananoe('mat_did') == 1:
                self.chk_matdid.setChecked(True)
            else:
                self.chk_matdid.setChecked(False) 
        
            #Material didactico
            if lee_par_gananoe('gastos_movviat') == 1:
                self.chk_gastmov.setChecked(True)
            else:
                self.chk_gastmov.setChecked(False)

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
         

    def lee_chkbox(self):
        
        """
        Actualiza la tabla parametrosgananciasoe, en base a los valores de los checkboxs.
        """
        try:

            #Ganancia bruta
            if self.chk_ganbruta.isChecked() == True:
                actualiza_par_gananoe('gan_brut', 1)
            else:
                actualiza_par_gananoe('gan_brut', 0)

            #Retención ganancia
            if self.chk_retganan.isChecked() == True:
                actualiza_par_gananoe('ret_gan', 1)
            else:
                actualiza_par_gananoe('ret_gan', 0)

            #Retribuciones no habituales
            if self.chk_gannohab.isChecked() == True:
                actualiza_par_gananoe('retrib_nohab', 1)
            else:
                actualiza_par_gananoe('retrib_nohab', 0)

            #Ajuste
            if self.chk_ajuste.isChecked() == True:
                actualiza_par_gananoe('ajuste', 1)
            else:
                actualiza_par_gananoe('ajuste', 0)

            #Remuneración exenta
            if self.chk_remuexen.isChecked() == True:
                actualiza_par_gananoe('exe_noalc', 1)
            else:
                actualiza_par_gananoe('exe_noalc', 0)

            #SAC
            if self.chk_sac.isChecked() == True:
                actualiza_par_gananoe('sac', 1)
            else:
                actualiza_par_gananoe('sac', 0)

            #Horas extras gravadas
            if self.chk_hsextgrav.isChecked() == True:
                actualiza_par_gananoe('horas_extgr', 1)
            else:
                actualiza_par_gananoe('horas_extgr', 0)

            #Horas extras exentas
            if self.chk_hsextex.isChecked() == True:
                actualiza_par_gananoe('horas_extex', 1)
            else:
                actualiza_par_gananoe('horas_extex', 0)

            #Material didáctico
            if self.chk_matdid.isChecked() == True:
                actualiza_par_gananoe('mat_did', 1)
            else:
                actualiza_par_gananoe('mat_did', 0)

            #Gastos movilidad
            if self.chk_gastmov.isChecked() == True:
                actualiza_par_gananoe('gastos_movviat', 1)
            else:
                actualiza_par_gananoe('gastos_movviat', 0)

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Se actualizaron los datos correctamente")
            msg_box.setWindowTitle("Información")
            msg_box.setStandardButtons(QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/windows/information.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg_box.setWindowIcon(icon) 
            msg_box.exec()

            self.frm_config_gananoe.close()

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
        