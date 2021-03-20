import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from view.main_window import UiMainWindow
from controller.controller import Controller


def close(controller: Controller):
    controller.dbh.close_connection()
    app.exec_()


if __name__ == "__main__":
    controller = Controller()

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow, controller)
    MainWindow.show()

    sys.exit(close(controller))
