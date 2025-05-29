# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'uv_gui.ui'
# Designed with pyqt designer
# Created by: PyQt5 UI code generator 5.15.9

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("sensordataplotter")
        Form.resize(1125, 716)
        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setGeometry(QtCore.QRect(470, 10, 171, 51))
        self.titleLabel.setOpenExternalLinks(False)
        self.titleLabel.setObjectName("titleLabel")
        self.loadButton = QtWidgets.QPushButton(Form)
        self.loadButton.setGeometry(QtCore.QRect(210, 600, 211, 81))
        self.loadButton.setObjectName("loadButton")
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(670, 600, 211, 81))
        self.saveButton.setObjectName("saveButton")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(50, 50, 1021, 541))
        self.graphicsView.setObjectName("graphicsView")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("sensordataplotter", "sensordataplotter"))
        self.titleLabel.setText(_translate("Form", "DATA MONITORING APPLICATION"))
        self.loadButton.setText(_translate("Form", "UPLOAD CSV FILE AND PLOT THE GRAPH"))
        self.saveButton.setText(_translate("Form", "SAVE AS PDF FILE"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
