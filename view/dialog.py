# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from controller.controller import Controller
from model.parts import DeckRadioButton


class SelectionDialog(QDialog):
    def __init__(self, decks: list, controller: Controller):
        super(SelectionDialog, self).__init__()
        self.setup_ui(decks)
        self.controller = controller

        self.exec_()

    def setup_ui(self, decks: list):
        self.setObjectName("deck_selection")
        self.resize(240, 320)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10, 270, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")


        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 217, 257))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Creating the radio buttons to choose the deck
        radio_buttons = [DeckRadioButton(deck.name, deck) for deck in decks]
        vbox = QtWidgets.QVBoxLayout()
        self.btn_group = QtWidgets.QButtonGroup()
        for button_index in range(len(radio_buttons)):
            self.btn_group.addButton(radio_buttons[button_index], button_index)
            vbox.addWidget(radio_buttons[button_index])

        self.scrollAreaWidgetContents.setLayout(vbox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.re_translate_ui()
        self.buttonBox.accepted.connect(self.accept)
        self.accepted.connect(self.checked)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Choose Deck", "Deckauswahl"))

    def checked(self):
        if selected_button := self.btn_group.checkedButton():
            self.controller.selected_deck = selected_button.deck
