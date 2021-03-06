# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cart.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import chaining_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(393, 517)
        Form.setStyleSheet("background-color: rgb(53, 92, 125);")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 39, 361, 31))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "background-color: rgb(246, 114, 128);\n"
                                        "font: 14pt \"Bebas Neue\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(20, 109, 361, 81))
        self.frame_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(42, 54, 59);\n"
                                   "")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 61, 20))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 18pt \"Bebas Neue\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 61, 20))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 18pt \"Bebas Neue\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(240, 30, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(30, 79, 51, 21))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 18pt \"Bebas Neue\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(300, 80, 61, 20))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 18pt \"Bebas Neue\";")
        self.label_13.setObjectName("label_13")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 10, 371, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 190, 51, 41))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 132, 124);\n"
                                         "image: url(:/newPrefix/images/plus.png);\n"
                                         "border-radius:5px;")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 190, 51, 41))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 132, 124);\n"
                                        "image: url(:/newPrefix/images/minus.png);\n"
                                        "border-radius:5px;")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 190, 231, 41))
        self.pushButton_7.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 14pt \"Bebas Neue\";\n"
                                        "background-color: rgb(246, 114, 128);\n"
                                        "border-radius:\"8px\";\n"
                                        "text-align:left;\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame.raise_()
        self.pushButton_8.raise_()
        self.frame_6.raise_()
        self.label_12.raise_()
        self.label_13.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_8.setText(_translate("Form", "Checkout"))
        self.label_9.setText(_translate("Form", "Value1"))
        self.label_10.setText(_translate("Form", "Value5"))
        self.label_11.setText(_translate("Form", "Value6"))
        self.label_12.setText(_translate("Form", "Total"))
        self.label_13.setText(_translate("Form", "Value4"))
        self.pushButton_7.setText(_translate("Form", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
