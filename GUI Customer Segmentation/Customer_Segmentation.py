# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Customer_Segmentation.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 541, 51))
        self.frame.setStyleSheet("background-color: rgb(42,42,42);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 531, 31))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 541, 31))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 191, 311))
        self.frame_2.setStyleSheet("background-color: rgb(42,42,42);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 171, 31))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 171, 22))
        self.comboBox.setStyleSheet("border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px;    \n"
"background-color: rgb(52, 59, 72);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 157, 230);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 90, 171, 22))
        self.comboBox_2.setStyleSheet("border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px;    \n"
"background-color: rgb(52, 59, 72);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 157, 230);\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 171, 31))
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 150, 171, 22))
        self.comboBox_3.setStyleSheet("border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px;    \n"
"background-color: rgb(52, 59, 72);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 157, 230);\n"
"")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 171, 31))
        self.label_9.setObjectName("label_9")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 210, 171, 22))
        self.comboBox_4.setStyleSheet("border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px;    \n"
"background-color: rgb(52, 59, 72);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 157, 230);\n"
"")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 180, 151, 31))
        self.label_10.setObjectName("label_10")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 270, 171, 22))
        self.comboBox_5.setStyleSheet("border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px;    \n"
"background-color: rgb(52, 59, 72);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 157, 230);\n"
"")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 240, 151, 31))
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 390, 191, 41))
        self.pushButton.setStyleSheet("background-color: rgb(61,61,61);\n"
"border-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 157, 230);")
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(220, 80, 151, 141))
        self.frame_3.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser.setGeometry(QtCore.QRect(30, 60, 91, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(75,75,75);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(30, 30, 91, 20))
        self.label_12.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(380, 80, 151, 141))
        self.frame_4.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 60, 91, 51))
        self.textBrowser_2.setStyleSheet("background-color: rgb(75,75,75);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(30, 30, 91, 20))
        self.label_13.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(220, 230, 151, 141))
        self.frame_5.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser_4.setGeometry(QtCore.QRect(30, 60, 91, 51))
        self.textBrowser_4.setStyleSheet("background-color: rgb(75,75,75);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(0, 30, 151, 20))
        self.label_15.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(380, 230, 151, 141))
        self.frame_6.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_6)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 60, 91, 51))
        self.textBrowser_3.setStyleSheet("background-color: rgb(75,75,75);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setGeometry(QtCore.QRect(0, 30, 151, 20))
        self.label_14.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(160, 390, 381, 41))
        self.frame_7.setStyleSheet("background-color: rgb(42,42,42);\n"
"border-radius: 20px;\n"
"color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame_7)
        self.textBrowser_5.setGeometry(QtCore.QRect(70, 10, 281, 21))
        self.textBrowser_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(205, 71, 341, 311))
        self.graphicsView.setStyleSheet("background-color: rgb(42,42,42);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 561, 441))
        self.frame_8.setStyleSheet("background-color: rgb(21,21,21);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.raise_()
        self.graphicsView.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Customer Segmentation</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Muhammad Masdar Mahasin</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Kuliah semester berapa?"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Semester 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Semester 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Semester 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Semester 4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Semester 5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Semester 6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Semester 7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Semester 8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Semester 9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Semester 10"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "SOSHUM"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "SAINTEK"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "HUMANIORA dan AGAMA"))
        self.label_8.setText(_translate("MainWindow", "Kuliah di bidang apa?"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Riset Ilmiah"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Organisasi BEM"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Riset Ilmiah dan BEM"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Kuliah Saja"))
        self.label_9.setText(_translate("MainWindow", "Aktivitas di kampus?"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Kota Besar"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Daerah"))
        self.label_10.setText(_translate("MainWindow", "Domisili asal?"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Thriller"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Romance/Drama"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Komedi"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Misteri"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Science Fiction"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "Cartoon"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "Action"))
        self.label_11.setText(_translate("MainWindow", "Genre Buku/Film Favorit apa?"))
        self.pushButton.setText(_translate("MainWindow", "RUN!"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">KNN</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SVM</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Decision Tree</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Random Forest</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
