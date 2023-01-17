#Formulario principal.
#Parte de la vista del modelo MVC.

import webbrowser
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QAbstractScrollArea
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from importacion import BaseDatos
from visualizar_empleados import ListaEmpleado
from visualizar_rembruta import VisualizarRemBruta
from visualizar_deducciones import VisualizarDeduc
from visualizar_cargas_familia import VisualizarCFamilia
from visualizar_otros_empleos import VisualizaOEmp
from visualizar_dedespprimeraparte import VerDeduccionPParte
from visualizar_dedespsegparte import VerDeduccionSParte
from visualizar_promediobruto import VerPromedioBruto
from visualizar_divisor import ListaDivisor
from importar_empleados import ImportarEmpleados
from importar_sueldo_bruto import ImportaSalBruto
from importar_deducciones import ImportaDeducciones
from importar_familiares import ImportarCFamilia
from importar_otros_empleos import ImportaOE
from importar_divisor import ImportarDivisor
from calculo_promedio_bruto import PromedioBruto
from beneficio_ganancias import Liquidador
from config_deducciones import ConfigDeducciones
from config_dedsparte import ParametroDedSParte
from config_gananoe import ConfigGananOE
from reportes import Reportes
from borrado_bbdd import BorrarTabla
from acerca import Acerca
from users import Usuario
from crud_bd import lee_promediobruto
from crud_bd import lee_primerparrafo
from crud_bd import lee_segundoparrafo


class MainForm(object):

    def __init__(self, ventana: QMainWindow, usuario):
        
        super().__init__()
        
        #Formulario principal
        self.user = usuario
        self.frm_main = ventana
        self.frm_main.setObjectName("frm_main")
        self.frm_main.resize(698, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/windows/main.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frm_main.setWindowIcon(icon)

        #Tree view
        self.centralwidget = QWidget(self.frm_main)
        self.centralwidget.setObjectName("centralwidget")
        self.frm_main.setCentralWidget(self.centralwidget)

        verticalLayout = QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")

        self.tv_datos = QTableWidget(self.centralwidget)
        self.tv_datos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tv_datos.setObjectName("tv_datos")
        verticalLayout.addWidget(self.tv_datos)
        
        #Menú bar
        self.menubar = QMenuBar(self.frm_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName("menubar")

        #Menú archivo
        self.mnu_archivo = QMenu(self.menubar)
        self.mnu_archivo.setObjectName("mnu_archivo")

        self.act_nuevo = QAction(self.frm_main)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/menu/archivo/mnu_new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_nuevo.setIcon(icon1)
        self.act_nuevo.setObjectName("act_nuevo")
        self.act_nuevo.triggered.connect(lambda: self.nueva_bbdd())
        
        self.act_abrir = QAction(self.frm_main)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/menu/archivo/mnu_open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_abrir.setIcon(icon2)
        self.act_abrir.setObjectName("act_abrir")
        self.act_abrir.triggered.connect(lambda: self.abrir_bbdd())
        
        self.act_salir = QAction(self.frm_main)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/menu/archivo/mnu_exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_salir.setIcon(icon5)
        self.act_salir.setObjectName("act_salir")
        self.act_salir.triggered.connect(lambda: self.frm_main.close())

        #Menú ver
        self.mnu_ver = QMenu(self.menubar)
        self.mnu_ver.setObjectName("mnu_ver")

        self.act_ver_empleado = QAction(self.frm_main)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_empleado.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_empleado.setIcon(icon6)
        self.act_ver_empleado.setObjectName("act_ver_empleado")
        self.act_ver_empleado.triggered.connect(lambda: self.ver_empleado())

        self.act_ver_remu = QAction(self.frm_main)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_remuneraciones.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_remu.setIcon(icon7)
        self.act_ver_remu.setObjectName("act_ver_remu")
        self.act_ver_remu.triggered.connect(lambda: self.ver_rembruta())
        
        self.act_ver_deduc = QAction(self.frm_main)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_deducciones.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_deduc.setIcon(icon8)
        self.act_ver_deduc.setObjectName("act_ver_deduc")
        self.act_ver_deduc.triggered.connect(lambda: self.ver_deducciones())

        self.act_ver_cargfam = QAction(self.frm_main)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_cargasfamilia.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_cargfam.setIcon(icon9)
        self.act_ver_cargfam.setObjectName("act_ver_cargfam")
        self.act_ver_cargfam.triggered.connect(lambda: self.ver_cfam())
        
        self.act_ver_gananoe = QAction(self.frm_main)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_gananciasoe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_gananoe.setIcon(icon10)
        self.act_ver_gananoe.setObjectName("act_ver_gananoe")
        self.act_ver_gananoe.triggered.connect(lambda: self.ver_gananoe())

        self.act_ver_prombrut = QAction(self.frm_main)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_prombruto.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_prombrut.setIcon(icon23)
        self.act_ver_prombrut.setObjectName("act_ver_prombrut")
        self.act_ver_prombrut.triggered.connect(lambda: self.ver_prmbruto())

        self.act_ver_dedprim = QAction(self.frm_main)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_primerpar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_dedprim.setIcon(icon24)
        self.act_ver_dedprim.setObjectName("act_ver_dedprim")
        self.act_ver_dedprim.triggered.connect(lambda: self.ver_dedpparte())

        self.act_ver_dedseg = QAction(self.frm_main)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_segundopar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_dedseg.setIcon(icon25)
        self.act_ver_dedseg.setObjectName("ver_act_dedseg")
        self.act_ver_dedseg.triggered.connect(lambda: self.ver_dedsparte())

        self.act_ver_divisor = QAction(self.frm_main)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("img/menu/ver/mnu_divisor.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ver_divisor.setIcon(icon28)
        self.act_ver_divisor.setObjectName("act_ver_divisor")
        self.act_ver_divisor.triggered.connect(lambda: self.ver_divisor())

        #Menú importar
        self.mnu_importar = QMenu(self.menubar)
        self.mnu_importar.setObjectName("mnu_importar")

        self.act_imp_empleado = QAction(self.frm_main)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("img/menu/importar/mnu_employee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_imp_empleado.setIcon(icon11)
        self.act_imp_empleado.setObjectName("act_imp_empleado")
        self.act_imp_empleado.triggered.connect(lambda: self.importa_empleados())
        
        self.act_imp_remu = QAction(self.frm_main)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("img/menu/importar/mnu_remu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_imp_remu.setIcon(icon12)
        self.act_imp_remu.setObjectName("act_imp_remu")
        self.act_imp_remu.triggered.connect(lambda: self.importa_remuneraciones())


        self.act_imp_deduc = QAction(self.frm_main)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("img/menu/importar/mnu_deduc.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_imp_deduc.setIcon(icon13)
        self.act_imp_deduc.setObjectName("act_imp_deduc")
        self.act_imp_deduc.triggered.connect(lambda: self.importa_deducciones())

        self.act_imp_cargfam = QAction(self.frm_main)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("img/menu/importar/mnu_familia.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_imp_cargfam.setIcon(icon14)
        self.act_imp_cargfam.setObjectName("act_imp_cargfam")
        self.act_imp_cargfam.triggered.connect(lambda: self.importa_cfam())

        self.act_imp_gananoe = QAction(self.frm_main)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("img/menu/importar/mnu_gan_oe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_imp_gananoe.setIcon(icon15)
        self.act_imp_gananoe.setObjectName("act_imp_gananoe")
        self.act_imp_gananoe.triggered.connect(lambda: self.importa_gan_oe())

        self.act_imp_divisor = QAction(self.frm_main)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("img/menu/importar/mnu_divisor.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_imp_divisor.setIcon(icon27)
        self.act_imp_divisor.setObjectName("act_imp_divisor")
        self.act_imp_divisor.triggered.connect(lambda: self.importa_divisor())

        #Menú ejecutar
        self.mnu_ejecutar = QMenu(self.menubar)
        self.mnu_ejecutar.setObjectName("mnu_ejecutar")

        self.act_promedio = QAction(self.frm_main)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("img/menu/ejecutar/mnu_promedio.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_promedio.setIcon(icon16)
        self.act_promedio.setObjectName("act_promedio")
        self.act_promedio.triggered.connect(lambda: self.liq_pbruto())

        self.act_liquidador = QAction(self.frm_main)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("img/menu/ejecutar/mnu_deducciones.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_liquidador.setIcon(icon17)
        self.act_liquidador.setObjectName("act_liquidador")
        self.act_liquidador.triggered.connect(lambda: self.liq_deduc())

        self.act_ejec_borrar = QAction(self.frm_main)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("img/menu/ejecutar/mnu_borrar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ejec_borrar.setIcon(icon26)
        self.act_ejec_borrar.setObjectName("act_ejec_borrar")
        self.act_ejec_borrar.triggered.connect(lambda: self.borra_tabla())

        #Menú reporte
        self.mnu_reporte = QMenu(self.menubar)
        self.mnu_reporte.setObjectName("mnu_reporte")
        
        self.act_rep_deduc = QAction(self.frm_main)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("img/menu/reportes/mnu_deduccion.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_rep_deduc.setIcon(icon19)
        self.act_rep_deduc.setObjectName("act_rep_deduc")
        self.act_rep_deduc.triggered.connect(lambda: self.reportes())

        #Menú configuración
        self.mnu_config = QMenu(self.menubar)
        self.mnu_config.setObjectName("mnu_config")

        self.act_ded_personales = QAction(self.frm_main)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("img/menu/config/mnu_configuracion.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ded_personales.setIcon(icon20)
        self.act_ded_personales.setObjectName("act_ded_personales")
        self.act_ded_personales.triggered.connect(lambda: self.config_dedper())

        self.act_ded_sparrafo = QAction(self.frm_main)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("img/menu/config/mnu_segundoparrafo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_ded_sparrafo.setIcon(icon21)
        self.act_ded_sparrafo.setObjectName("act_ded_sparrafo")
        self.act_ded_sparrafo.triggered.connect(lambda: self.config_dedsparte())

        self.act_config_gananoe = QAction(self.frm_main)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("img/menu/config/mnu_config_gananoe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_config_gananoe.setIcon(icon22)
        self.act_config_gananoe.setObjectName("act_config_gananoe")
        self.act_config_gananoe.triggered.connect(lambda: self.config_gananoe())

        #Menú ayuda
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")

        self.act_documentacion = QAction(self.frm_main)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("img/menu/ayuda/mnu_documentacion.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_documentacion.setIcon(icon21)
        self.act_documentacion.setObjectName("act_documentacion")
        self.act_documentacion.triggered.connect(lambda: webbrowser.open('documentation\index.html', new=2, autoraise=True))

        self.actionAcerca_de = QAction(self.frm_main)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("img/menu/ayuda/mnu_acerca.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAcerca_de.setIcon(icon22)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionAcerca_de.triggered.connect(lambda: self.acercade())

        #Barra de estado
        self.frm_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self.frm_main)
        self.statusbar.setObjectName("statusbar")
        self.frm_main.setStatusBar(self.statusbar)
        
        #Barra de herramientas
        self.toolBar = QToolBar(self.frm_main)
        self.toolBar.setObjectName("toolBar")
        self.frm_main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.act_tool_prombruto = QAction(self.frm_main)
        self.act_tool_prombruto.setIcon(icon23)
        self.act_tool_prombruto.setObjectName("act_tool_prombruto")
        self.act_tool_prombruto.triggered.connect(self.ver_promedio_bruto)
        
        self.act_tool_dedprim = QAction(self.frm_main)
        self.act_tool_dedprim.setIcon(icon24)
        self.act_tool_dedprim.setObjectName("act_tool_dedprim")
        self.act_tool_dedprim.triggered.connect(self.ver_primerparrafo)
        
        self.act_tool_dedsegun = QAction(self.frm_main)
        self.act_tool_dedsegun.setIcon(icon25)
        self.act_tool_dedsegun.setObjectName("act_tool_dedsegun")
        self.act_tool_dedsegun.triggered.connect(self.ver_segparrafo)
        
        #Configuración del menú
        self.mnu_archivo.addAction(self.act_nuevo)
        self.mnu_archivo.addAction(self.act_abrir)
        self.mnu_archivo.addSeparator()
        self.mnu_archivo.addAction(self.act_salir)
        self.mnu_ver.addAction(self.act_ver_empleado)
        self.mnu_ver.addAction(self.act_ver_remu)
        self.mnu_ver.addAction(self.act_ver_deduc)
        self.mnu_ver.addAction(self.act_ver_cargfam)
        self.mnu_ver.addAction(self.act_ver_gananoe)
        self.mnu_ver.addSeparator()
        self.mnu_ver.addAction(self.act_ver_divisor)
        self.mnu_ver.addSeparator()
        self.mnu_ver.addAction(self.act_ver_prombrut)
        self.mnu_ver.addAction(self.act_ver_dedprim)
        self.mnu_ver.addAction(self.act_ver_dedseg)
        self.mnu_importar.addAction(self.act_imp_empleado)
        self.mnu_importar.addAction(self.act_imp_remu)
        self.mnu_importar.addAction(self.act_imp_deduc)
        self.mnu_importar.addAction(self.act_imp_cargfam)
        self.mnu_importar.addAction(self.act_imp_gananoe)
        self.mnu_importar.addSeparator()
        self.mnu_importar.addAction(self.act_imp_divisor)
        self.mnu_ejecutar.addAction(self.act_promedio)
        self.mnu_ejecutar.addAction(self.act_liquidador)
        self.mnu_ejecutar.addSeparator()
        self.mnu_ejecutar.addAction(self.act_ejec_borrar)
        self.mnu_reporte.addAction(self.act_rep_deduc)
        self.mnu_config.addAction(self.act_ded_personales)
        self.mnu_config.addAction(self.act_ded_sparrafo)
        self.mnu_config.addSeparator()
        self.mnu_config.addAction(self.act_config_gananoe)
        self.menuAyuda.addAction(self.act_documentacion)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.mnu_archivo.menuAction())
        self.menubar.addAction(self.mnu_ver.menuAction())
        self.menubar.addAction(self.mnu_importar.menuAction())
        self.menubar.addAction(self.mnu_ejecutar.menuAction())
        self.menubar.addAction(self.mnu_reporte.menuAction())
        self.menubar.addAction(self.mnu_config.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.act_nuevo)
        self.toolBar.addAction(self.act_abrir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_imp_empleado)
        self.toolBar.addAction(self.act_imp_remu)
        self.toolBar.addAction(self.act_imp_deduc)
        self.toolBar.addAction(self.act_imp_cargfam)
        self.toolBar.addAction(self.act_imp_gananoe)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_promedio)
        self.toolBar.addAction(self.act_liquidador)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_tool_prombruto)
        self.toolBar.addAction(self.act_tool_dedprim)
        self.toolBar.addAction(self.act_tool_dedsegun)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_ded_personales)

        QtCore.QMetaObject.connectSlotsByName(self.frm_main)

        _translate = QtCore.QCoreApplication.translate
        self.frm_main.setWindowTitle(_translate("frm_main", "PayroolTools - Deducción especial incrementada primera y segunda parte"))
        self.mnu_archivo.setTitle(_translate("frm_main", "Archivo"))
        self.mnu_ver.setTitle(_translate("frm_main", "Ver"))
        self.mnu_importar.setTitle(_translate("frm_main", "Importar"))
        self.mnu_ejecutar.setTitle(_translate("frm_main", "Ejecutar"))
        self.mnu_reporte.setTitle(_translate("frm_main", "Reportes"))
        self.mnu_config.setTitle(_translate("frm_main", "Configuración"))
        self.menuAyuda.setTitle(_translate("frm_main", "Ayuda"))
        self.toolBar.setWindowTitle(_translate("frm_main", "toolBar"))
        self.act_nuevo.setText(_translate("frm_main", "Nueva BBDD"))
        self.act_abrir.setText(_translate("frm_main", "Abrir BBDD"))
        self.act_salir.setText(_translate("frm_main", "Salir"))
        self.act_ver_empleado.setText(_translate("frm_main", "Empleados"))
        self.act_ver_remu.setText(_translate("frm_main", "Remuneraciones"))
        self.act_ver_deduc.setText(_translate("frm_main", "Deducciones"))
        self.act_ver_cargfam.setText(_translate("frm_main", "Cargas de familia"))
        self.act_ver_gananoe.setText(_translate("frm_main", "Ganancias OE"))
        self.act_ver_divisor.setText(_translate("frm_main", "Divisor promedio bruto"))
        self.act_imp_empleado.setText(_translate("frm_main", "Empleados"))
        self.act_imp_remu.setText(_translate("frm_main", "Remuneraciones"))
        self.act_imp_deduc.setText(_translate("frm_main", "Deducciones"))
        self.act_imp_cargfam.setText(_translate("frm_main", "Cargas de familia"))
        self.act_imp_gananoe.setText(_translate("frm_main", "Ganancias OE"))
        self.act_imp_divisor.setText(_translate("frm_main", "Divisor promedio bruto"))
        self.act_promedio.setText(_translate("frm_main", "Promedio bruto"))
        self.act_liquidador.setText(_translate("frm_main", "Calculo de deducciones"))
        self.act_rep_deduc.setText(_translate("frm_main", "Reportes"))
        self.act_ded_personales.setText(_translate("frm_main", "Deducciones personales"))
        self.act_ded_sparrafo.setText(_translate("frm_main", "Deducciones segunda parte"))
        self.act_config_gananoe.setText(_translate("frm_main", "Configurar ganancias OE"))
        self.act_documentacion.setText(_translate("frm_main", "Documentación"))
        self.actionAcerca_de.setText(_translate("frm_main", "Acerca de..."))
        self.act_ver_prombrut.setText(_translate("frm_main", "Promedios remuneración bruta"))
        self.act_ver_dedprim.setText(_translate("frm_main", "Deducciones primer párrafo"))
        self.act_ver_dedseg.setText(_translate("frm_main", "Deducciones segundo párrafo"))
        self.act_tool_prombruto.setText(_translate("frm_main", "Promedio bruto"))
        self.act_tool_dedprim.setText(_translate("frm_main", "Deducciones primer párrafo"))
        self.act_tool_dedsegun.setText(_translate("frm_main", "Deducciones segundo párrafo"))
        self.act_ejec_borrar.setText(_translate("frm_main", "Borrar registros BBDD"))


        #Layout
        self.centralwidget.setLayout(verticalLayout)

        #Evento cierre
        self.frm_main.closeEvent = self.closeEvent
        

    def abrir_bbdd(self):
        options = QFileDialog.Options()
        file_name = QFileDialog.getOpenFileName(self.frm_main, "Abrir base de datos","","Base de datos (*.db);;Todos los archivos (*)", 
                                                options=options)
        if file_name[0] != '':
            base = BaseDatos(file_name[0])
            base.nueva_bbdd()


    def nueva_bbdd(self):
        options = QFileDialog.Options()
        file_name = QFileDialog.getSaveFileName(self.frm_main, "Nueva base de datos","","Base de datos (*.db);;Todos los archivos (*)", 
                                                options=options)
        if file_name[0] != '':
            base = BaseDatos(file_name[0])
            base.nueva_bbdd()


    def importa_empleados(self):

        try:
            frm_dialog = QDialog()
            ImportarEmpleados(frm_dialog)
            frm_dialog.exec_()

        except Exception as error:
            
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def importa_remuneraciones(self):
        
        try:
            frm_dialog = QDialog()
            ImportaSalBruto(frm_dialog)
            frm_dialog.exec_()
            
        except Exception as error:
        
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def importa_deducciones(self):
    
        try:
            frm_dialog = QDialog()
            ImportaDeducciones(frm_dialog)
            frm_dialog.exec_()
        
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec() 


    def importa_cfam(self):
    
        try:
            frm_dialog = QDialog()
            ImportarCFamilia(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def importa_gan_oe(self):
    
        try:
            frm_dialog = QDialog()
            ImportaOE(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def importa_divisor(self):
    
        try:
            frm_dialog = QDialog()
            ImportarDivisor(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def ver_empleado(self):
    
        try:
            frm_dialog = QDialog()
            ListaEmpleado(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def ver_rembruta(self):
    
        try:
            frm_dialog = QDialog()
            VisualizarRemBruta(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  


    def ver_deducciones(self):
    
        try:
            frm_dialog = QDialog()
            VisualizarDeduc(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def ver_cfam(self):
    
        try:
            frm_dialog = QDialog()
            VisualizarCFamilia(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  


    def ver_gananoe(self):
    
        try:
            frm_dialog = QDialog()
            VisualizaOEmp(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def ver_divisor(self):
    
        try:
            frm_dialog = QDialog()
            ListaDivisor(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def ver_prmbruto(self):
    
        try:
            frm_dialog = QDialog()
            VerPromedioBruto(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def ver_dedpparte(self):
    
        try:
            frm_dialog = QDialog()
            VerDeduccionPParte(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def ver_dedsparte(self):
    
        try:
            frm_dialog = QDialog()
            VerDeduccionSParte(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  

    def liq_pbruto(self):
    
        try:
            frm_dialog = QDialog()
            PromedioBruto(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def liq_deduc(self):
    
        try:
            frm_dialog = QDialog()
            Liquidador(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def borra_tabla(self):
    
        try:
            frm_dialog = QDialog()
            BorrarTabla(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def reportes(self):
    
        try:
            frm_dialog = QDialog()
            Reportes(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def config_dedper(self):
    
        try:
            frm_dialog = QDialog()
            ConfigDeducciones(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def config_dedsparte(self):
    
        try:
            frm_dialog = QDialog()
            ParametroDedSParte(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def config_gananoe(self):
    
        try:
            frm_dialog = QDialog()
            ConfigGananOE(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  

    def acercade(self):
    
        try:
            frm_dialog = QDialog()
            Acerca(frm_dialog)
            frm_dialog.exec_()
    
        except Exception as error:
    
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(str(error))
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonCl
            msg_box.exec()  


    def ver_promedio_bruto(self):

        try:
            
            listado = lee_promediobruto(['*'], ['*'])
        
            self.tv_datos.clear()

            self.tv_datos.setColumnCount(4)
            self.tv_datos.setRowCount(0)

            #Definición de las columnas.
            #Item legajo
            item_leg = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(0, item_leg)
            item_ann = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(1, item_ann)
            item_mes = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(2, item_mes)
            item_importe = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(3, item_importe)

            #Titúlos de las columnas del treeview
            _translate = QtCore.QCoreApplication.translate
            item_leg.setText(_translate("self.frm_main", "Legajo"))
            item_leg = self.tv_datos.horizontalHeaderItem(0)
            item_ann.setText(_translate("self.frm_main", "Año"))
            item_ann = self.tv_datos.horizontalHeaderItem(1)
            item_mes.setText(_translate("self.frm_main", "Mes"))
            item_mes = self.tv_datos.horizontalHeaderItem(2)
            item_importe.setText(_translate("self.frm_main", "Importe"))
            item_importe = self.tv_datos.horizontalHeaderItem(3)

            for lista in listado:
            
                position = self.tv_datos.rowCount()
                self.tv_datos.insertRow(position)          
            
                y = 0
            
                for n in lista:
                    valor = str(n)
                    self.tv_datos.setItem(position, y, QTableWidgetItem(valor))
                    y += 1

        except TypeError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en base de datos.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def ver_primerparrafo(self):

        try:
    
            listado = lee_primerparrafo(['*'], ['*'])
    
            self.tv_datos.clear()
            self.tv_datos.setColumnCount(9)
            self.tv_datos.setRowCount(0)
        
            #Definición de las columnas.
            #Item legajo
            item_leg = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(0, item_leg)
            item_ann = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(1, item_ann)
            item_mes = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(2, item_mes)  
            item_sbruto = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(3, item_sbruto)
            item_deducciones = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(4, item_deducciones)  
            item_ded_esp = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(5, item_ded_esp) 
            item_min_no_imp = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(6, item_min_no_imp) 
            item_car_fam = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(7, item_car_fam)
            item_ded_p_par = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(8, item_ded_p_par) 
        
            #Titúlos de las columnas del treeview
            _translate = QtCore.QCoreApplication.translate
            item_leg.setText(_translate("self.frm_main", "Legajo"))
            item_leg = self.tv_datos.horizontalHeaderItem(0)
            item_ann.setText(_translate("self.frm_main", "Año"))
            item_ann = self.tv_datos.horizontalHeaderItem(1)
            item_mes.setText(_translate("self.frm_main", "Mes"))
            item_mes = self.tv_datos.horizontalHeaderItem(2)
            item_sbruto.setText(_translate("self.frm_main", "Salario bruto"))
            item_sbruto = self.tv_datos.horizontalHeaderItem(3)
            item_deducciones.setText(_translate("self.frm_main", "Deducciones"))
            item_deducciones = self.tv_datos.horizontalHeaderItem(4)
            item_ded_esp.setText(_translate("self.frm_main", "Deducción especial"))
            item_ded_esp = self.tv_datos.horizontalHeaderItem(5)
            item_min_no_imp.setText(_translate("self.frm_main", "Ganancias no imponibles"))
            item_min_no_imp = self.tv_datos.horizontalHeaderItem(6)
            item_car_fam.setText(_translate("self.frm_main", "Cargas de familia"))
            item_car_fam = self.tv_datos.horizontalHeaderItem(7)
            item_ded_p_par.setText(_translate("self.frm_main", "Deducción Especial Incrementada Primera parte"))
            item_ded_p_par = self.tv_datos.horizontalHeaderItem(8)
        
        
            for lista in listado:
        
                position = self.tv_datos.rowCount()
                self.tv_datos.insertRow(position)          
        
                y = 0
        
                for n in lista:
                    valor = str(n)
                    self.tv_datos.setItem(position, y, QTableWidgetItem(valor))
                    y += 1

        except TypeError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en base de datos.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  


    def ver_segparrafo(self):
        
        try:
            listado = lee_segundoparrafo(['*'], ['*'])
    
            self.tv_datos.clear()
            self.tv_datos.setColumnCount(4)
            self.tv_datos.setRowCount(0)
    
            #Definición de las columnas.
            #Item legajo
            item_leg = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(0, item_leg)
            item_ann = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(1, item_ann)
            item_mes = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(2, item_mes)
            item_importe = QTableWidgetItem()
            self.tv_datos.setHorizontalHeaderItem(3, item_importe)
        
            #Titúlos de las columnas del treeview
            _translate = QtCore.QCoreApplication.translate
            item_leg.setText(_translate("self.frm_main", "Legajo"))
            item_leg = self.tv_datos.horizontalHeaderItem(0)
            item_ann.setText(_translate("self.frm_main", "Año"))
            item_ann = self.tv_datos.horizontalHeaderItem(1)
            item_mes.setText(_translate("self.frm_main", "Mes"))
            item_mes = self.tv_datos.horizontalHeaderItem(2)
            item_importe.setText(_translate("self.frm_main", "Deducción Especial Incrementada Segunda parte"))
            item_importe = self.tv_datos.horizontalHeaderItem(3)
        
            for lista in listado:
        
                position = self.tv_datos.rowCount()
                self.tv_datos.insertRow(position)          
        
                y = 0
        
                for n in lista:
                    valor = str(n)
                    self.tv_datos.setItem(position, y, QTableWidgetItem(valor))
                    y += 1
        
        except TypeError:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Error en base de datos.")
            msg_box.setWindowTitle("Error")
            msg_box.setStandardButtons(QMessageBox.Ok)
            #msg_box.buttonClicked.connect(msgButtonClick)
            msg_box.exec()  

    def closeEvent(self, event):

        mensaje = QMessageBox.question(self.frm_main, 'Pregunta', 'Se procede con el cierre del programa. ¿Desea continuar?',
                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if mensaje == QMessageBox.Yes:
            
            usuario = Usuario()
            usuario.actualiza_estado(str(self.user), 'desconectado')
            usuario.cerrar_conexion()
            event.accept()
            QApplication.exit()
            
        else: 
            event.ignore()