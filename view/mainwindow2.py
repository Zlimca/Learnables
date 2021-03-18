# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel

from controller.controller import Controller


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, controller):
        self.controller = controller

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.verticalStackedWidget.setGeometry(QtCore.QRect(10, 10, 451, 571))
        self.verticalStackedWidget.setObjectName("verticalStackedWidget")

        # Start Page
        self.verticalStackedWidgetPage1 = QtWidgets.QWidget()
        self.verticalStackedWidgetPage1.setObjectName("verticalStackedWidgetPage1")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalStackedWidgetPage1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.btn_cards = QtWidgets.QPushButton(self.verticalStackedWidgetPage1,
                                               clicked=self.open_cards)
        self.btn_cards.setObjectName("button_cards")

        self.verticalLayout.addWidget(self.btn_cards)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)

        self.btn_decks = QtWidgets.QPushButton(self.verticalStackedWidgetPage1,
                                               clicked=lambda: self.verticalStackedWidget.setCurrentIndex(2))
        self.btn_decks.setObjectName("buttoin_decks")
        self.verticalLayout.addWidget(self.btn_decks)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)

        self.btn_learn = QtWidgets.QPushButton(self.verticalStackedWidgetPage1,
                                               clicked=lambda: self.verticalStackedWidget.setCurrentIndex(3))
        self.btn_learn.setObjectName("button_learn")
        self.verticalLayout.addWidget(self.btn_learn)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)

        self.btn_settings_5 = QtWidgets.QPushButton(self.verticalStackedWidgetPage1)
        self.btn_settings_5.setObjectName("btn_settings_5")
        self.verticalLayout.addWidget(self.btn_settings_5)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        self.verticalStackedWidget.addWidget(self.verticalStackedWidgetPage1)

        # Cards Page
        self.verticalStackedWidgetPage2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalStackedWidgetPage2.sizePolicy().hasHeightForWidth())
        self.verticalStackedWidgetPage2.setSizePolicy(sizePolicy)
        self.verticalStackedWidgetPage2.setObjectName("verticalStackedWidgetPage2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.verticalStackedWidgetPage2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea_5.setWidgetResizable(False)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 447, 507))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_11.addWidget(self.scrollArea_5)
        self.btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_11.addWidget(self.btn_add)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_main_menu = QtWidgets.QPushButton(self.verticalLayoutWidget,
                                                   clicked=lambda: self.verticalStackedWidget.setCurrentIndex(0))
        self.btn_main_menu.setObjectName("btn_main_menu")
        self.horizontalLayout.addWidget(self.btn_main_menu)
        self.btn_settings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout.addWidget(self.btn_settings)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.verticalStackedWidget.addWidget(self.verticalStackedWidgetPage2)

        # Decks Page
        self.verticalStackedWidgetPage3 = QtWidgets.QWidget()
        self.verticalStackedWidgetPage3.setObjectName("vertivalStackedWidgetPage3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.verticalStackedWidgetPage3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 451, 571))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.verticalLayoutWidget_4)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 447, 507))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_16.addWidget(self.scrollArea_8)
        self.btn_add_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_add_4.setObjectName("btn_add_4")
        self.verticalLayout_16.addWidget(self.btn_add_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_main_menu_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4,
                                                     clicked=lambda: self.verticalStackedWidget.setCurrentIndex(0))
        self.btn_main_menu_4.setObjectName("btn_main_menu_4")
        self.horizontalLayout_8.addWidget(self.btn_main_menu_4)
        self.btn_settings_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_settings_4.setObjectName("btn_settings_4")
        self.horizontalLayout_8.addWidget(self.btn_settings_4)
        self.verticalLayout_16.addLayout(self.horizontalLayout_8)
        self.verticalStackedWidget.addWidget(self.verticalStackedWidgetPage3)

        # Learn Page
        self.verticalStackedWidgetPage4 = QtWidgets.QWidget()
        self.verticalStackedWidgetPage4.setObjectName("verticalStackedWidgetPage4")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.verticalStackedWidgetPage4)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 451, 571))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label.setObjectName("label")
        self.verticalLayout_17.addWidget(self.label)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_back = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_back.setObjectName("pushButton_4")
        self.horizontalLayout_9.addWidget(self.btn_back)
        self.btn_check = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_check.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.btn_check)
        self.btn_failed = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_failed.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.btn_failed)
        self.btn_next = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_next.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.btn_next)
        self.verticalLayout_18.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_main_menu_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_5,
                                                     clicked=lambda: self.verticalStackedWidget.setCurrentIndex(0))
        self.btn_main_menu_5.setObjectName("btn_main_menu_5")
        self.horizontalLayout_10.addWidget(self.btn_main_menu_5)
        self.btn_settings_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_settings_6.setObjectName("btn_settings_6")
        self.horizontalLayout_10.addWidget(self.btn_settings_6)
        self.verticalLayout_18.addLayout(self.horizontalLayout_10)
        self.verticalLayout_17.addLayout(self.verticalLayout_18)
        self.verticalStackedWidget.addWidget(self.verticalStackedWidgetPage4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.re_translate_ui(MainWindow)
        self.verticalStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def re_translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_cards.setText(_translate("MainWindow", "Karten"))
        self.btn_decks.setText(_translate("MainWindow", "Decks"))
        self.btn_learn.setText(_translate("MainWindow", "Lernen"))
        self.btn_settings_5.setText(_translate("MainWindow", "Einstellungen"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_main_menu.setText(_translate("MainWindow", "Startseite"))
        self.btn_settings.setText(_translate("MainWindow", "Einstellungen"))
        self.btn_add_4.setText(_translate("MainWindow", "+"))
        self.btn_main_menu_4.setText(_translate("MainWindow", "Startseite"))
        self.btn_settings_4.setText(_translate("MainWindow", "Einstellungen"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btn_back.setText(_translate("MainWindow", "←"))
        self.btn_check.setText(_translate("MainWindow", "✔"))
        self.btn_failed.setText(_translate("MainWindow", "✘"))
        self.btn_next.setText(_translate("MainWindow", "→"))
        self.btn_main_menu_5.setText(_translate("MainWindow", "Startseite"))
        self.btn_settings_6.setText(_translate("MainWindow", "Einstellungen"))

    def open_cards(self):
        self.verticalStackedWidget.setCurrentIndex(1)
        cards = self.controller.get_cards()
        vbox = QtWidgets.QVBoxLayout()
        # for card in cards:
        #     vbox.addWidget(card)

        self.scrollAreaWidgetContents.setLayout(vbox)

    def set_btn_actions(self):
        # self.btn_settings
        # self.btn_settings_4
        # self.btn_settings_5
        # self.btn_settings_6

        # self.btn_add
        # self.btn_back
        # self.btn_next
        # self.btn_check
        # self.btn_failed
        pass
