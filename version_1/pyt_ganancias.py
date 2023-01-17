import sys
from login import Login
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class Controlador():

    def __init__(self):
        formulario = QMainWindow()
        Login(formulario)
        formulario.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Controlador()
    sys.exit(app.exec_())