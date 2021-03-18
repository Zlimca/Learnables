import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from view.mainwindow2 import Ui_MainWindow
from controller.controller import Controller


def close(controller: Controller):
    controller.dbh.close_connection()
    app.exec_()


if __name__ == "__main__":
    controller = Controller()
    #controller.on_startup()

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, controller)
    MainWindow.show()

    sys.exit(close(controller))
