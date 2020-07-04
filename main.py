from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import json
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import sys
import os


class Header(QWidget):
    def __init__(self):
        super(Header, self).__init__()
        self.mainUi()

    def mainUi(self):
        uic.loadUi('interface/header.ui', self)


class Menu(QWidget):
    def __init__(self):
        super(Menu, self).__init__()
        self.mainUi()
        self.widget = QWidget()

    def mainUi(self):
        uic.loadUi('interface/chain.ui', self)

    def setLayout(self):
        pass


class Cart(QWidget):
    def __init__(self):
        super(Cart, self).__init__()
        self.mainUi()

    def mainUi(self):
        uic.loadUi('interface/cart.ui', self)


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.menu = Menu()
        self.header = Header()
        self.cart = Cart()
        self.mainUI()
        self.setFixedSize(1350, 800)

    def mainUI(self):
        widget = QWidget()
        self.vlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()

        self.layout()
        self.cards()

        widget.setLayout(self.vlayout)
        self.setCentralWidget(widget)

    def cards(self):
        data = self.dataMenu()
        print(data)

        G_Layout = QGridLayout()

        for row in range(4):
            for col in range(len(data)):
                self.menu.label_3.repaint()
                self.menu.label_4.repaint()
                # image = QPixmap(data[col['images']])
                # self.menu.label.setPixmap(image)
                self.menu.label_3.setText(data[col]['nama_barang'])
                self.menu.label_4.setText(str(data[col]['harga']))
                self.menu.label_5.setText(data[col]['detail'])
                G_Layout.addWidget(self.menu, row, col)

    def layout(self):
        self.vlayout.addWidget(self.header)
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.setStretch(0, 90)
        self.vlayout.setStretch(1, 1000)

        self.hlayout.addWidget(self.menu)
        self.hlayout.addWidget(self.cart)
        self.hlayout.setStretch(0, 700)
        self.hlayout.setStretch(1, 300)

    # def menuLayout(self):
    #     for d in self.dataMenu():
    #         self.menu.v_menu.addWidget(d["images"])

    def dataMenu(self):
        with open('json/cart.json') as f:
            data = json.load(f)

        return data


if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.setWindowTitle("Python Chain App")
    window.show()
    sys.exit(app.exec_())
