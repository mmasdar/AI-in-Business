from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import pickle
import sklearn
import numpy as np

qtCreatorFile = "Customer_Segmentation.ui" # Enter file here.

DTC_model =pickle.load(open('DTC_interest.sav', 'rb'))
KNN_model =pickle.load(open('KNN_interest.sav', 'rb'))
RF_model =pickle.load(open('RF_interest.sav', 'rb'))
NB_model =pickle.load(open('NB_interest.sav', 'rb'))

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Calculate)

    
    def Calculate(self):
        self.text = self.comboBox.currentText()
        if self.text == "Semester 1" :
            semesteran = 1
        else :
            if self.text == "Semester 2":
                semesteran = 2
            else : 
                if self.text == "Semester 3" :
                    semesteran = 3
                else :
                    if self.text == "Semester 4":
                        semesteran = 4
                    else : 
                        if self.text == "Semester 5" :
                            semesteran = 5
                        else :
                            if self.text == "Semester 6":
                                semesteran = 6
                            else : 
                                if self.text == "Semester 7" :
                                    semesteran = 7
                                else :
                                    if self.text == "Semester 8":
                                        semesteran = 8
                                    else : 
                                        if self.text == "Semester 9" :
                                            semesteran = 9
                                        else :
                                            if self.text == "Semester 10":
                                                semesteran = 10


        self.text2 = self.comboBox_2.currentText()
        if self.text2 == "SOSHUM" :
            bidang = 1
        else :
            if self.text2 == "SAINTEK":
                bidang = 2
            else : 
                if self.text2 == "HUMANIORA dan AGAMA" :
                    bidang = 3


        self.text3 = self.comboBox_3.currentText()
        if self.text3 == "Riset Ilmiah" :
            aktivitas = 1
        else :
            if self.text3 == "Organisasi BEM":
                aktivitas = 4
            else : 
                if self.text3 == "Riset Ilmiah dan BEM" :
                    aktivitas = 3
                else :
                    if self.text3 == "Kuliah Saja":
                        aktivitas = 2


        self.text4 = self.comboBox_4.currentText()
        if self.text4 == "Kota Besar" :
            domisili = 1
        else :
            if self.text4 == "Daerah":
                domisili = 2


        self.text5 = self.comboBox_5.currentText()
        if self.text5 == "Thriller" :
            buku = 1
        else :
            if self.text5 == "Romance/Drama":
                buku = 2
            else : 
                if self.text5 == "Komedi" :
                    buku = 3
                else :
                    if self.text5 == "Misteri":
                        buku = 4
                    else : 
                        if self.text5 == "Science Fiction" :
                            buku = 5
                        else :
                            if self.text5 == "Cartoon":
                                buku = 6
                            else : 
                                if self.text5 == "Action" :
                                    buku = 7
        

        ngitung_DTC = DTC_model.predict([[semesteran, bidang, aktivitas, domisili, buku]])
        ngitung_KNN = KNN_model.predict([[semesteran, bidang, aktivitas, domisili, buku]])
        ngitung_RF = RF_model.predict([[semesteran, bidang, aktivitas, domisili, buku]])
        ngitung_NB = RF_model.predict([[semesteran, bidang, aktivitas, domisili, buku]])

        DTC = str(ngitung_DTC)
        KNN = str(ngitung_KNN)
        RF  = str(ngitung_RF)
        NB  = str(ngitung_NB)

        self.textBrowser.setText(KNN)
        self.textBrowser_3.setText(RF)
        self.textBrowser_4.setText(DTC)
        self.textBrowser_2.setText(NB)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())