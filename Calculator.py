# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc trying 1.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 550)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.Percentbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("%"))
        self.Percentbutton.setGeometry(QtCore.QRect(30, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Percentbutton.setFont(font)
        self.Percentbutton.setObjectName("Percentbutton")
        self.Cbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("C") )
        self.Cbutton.setGeometry(QtCore.QRect(110, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Cbutton.setFont(font)
        self.Cbutton.setObjectName("Cbutton")
        self.Arrowbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.remove_it())
        self.Arrowbutton.setGeometry(QtCore.QRect(190, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Arrowbutton.setFont(font)
        self.Arrowbutton.setObjectName("Arrowbutton")
        self.Minusbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("-"))
        self.Minusbutton.setGeometry(QtCore.QRect(270, 260, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Minusbutton.setFont(font)
        self.Minusbutton.setObjectName("Minusbutton")
        self.Sevenbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("7"))
        self.Sevenbutton.setGeometry(QtCore.QRect(30, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Sevenbutton.setFont(font)
        self.Sevenbutton.setObjectName("Sevenbutton")
        self.Eightbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("8"))
        self.Eightbutton.setGeometry(QtCore.QRect(110, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Eightbutton.setFont(font)
        self.Eightbutton.setObjectName("Eightbutton")
        self.Ninebutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("9"))
        self.Ninebutton.setGeometry(QtCore.QRect(190, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Ninebutton.setFont(font)
        self.Ninebutton.setObjectName("Ninebutton")
        self.Multiplybutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("*"))
        self.Multiplybutton.setGeometry(QtCore.QRect(270, 180, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Multiplybutton.setFont(font)
        self.Multiplybutton.setObjectName("Multiplybutton")
        self.Fourbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("4"))
        self.Fourbutton.setGeometry(QtCore.QRect(30, 260, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Fourbutton.setFont(font)
        self.Fourbutton.setObjectName("Fourbutton")
        self.Fivebutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("5"))
        self.Fivebutton.setGeometry(QtCore.QRect(110, 260, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Fivebutton.setFont(font)
        self.Fivebutton.setObjectName("Fivebutton")
        self.Sixbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("6"))
        self.Sixbutton.setGeometry(QtCore.QRect(190, 260, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Sixbutton.setFont(font)
        self.Sixbutton.setObjectName("Sixbutton")
        self.Dividedbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("/"))
        self.Dividedbutton.setGeometry(QtCore.QRect(270, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Dividedbutton.setFont(font)
        self.Dividedbutton.setObjectName("Dividedbutton")
        self.Onebutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("1"))
        self.Onebutton.setGeometry(QtCore.QRect(30, 340, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Onebutton.setFont(font)
        self.Onebutton.setObjectName("Onebutton")
        self.Plusminusbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.plus_minus_it("") )
        self.Plusminusbutton.setGeometry(QtCore.QRect(30, 420, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Plusminusbutton.setFont(font)
        self.Plusminusbutton.setObjectName("Plusminusbutton")
        self.Twobutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("2"))
        self.Twobutton.setGeometry(QtCore.QRect(110, 340, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Twobutton.setFont(font)
        self.Twobutton.setObjectName("Twobutton")
        self.Zerobutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("0"))
        self.Zerobutton.setGeometry(QtCore.QRect(110, 420, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Zerobutton.setFont(font)
        self.Zerobutton.setObjectName("Zerobutton")
        self.Threebutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("3"))
        self.Threebutton.setGeometry(QtCore.QRect(190, 340, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Threebutton.setFont(font)
        self.Threebutton.setObjectName("Threebutton")
        self.Plusbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.press_it("+"))
        self.Plusbutton.setGeometry(QtCore.QRect(270, 340, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Plusbutton.setFont(font)
        self.Plusbutton.setObjectName("Plusbutton")
        self.Decimalbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.dot_it())
        self.Decimalbutton.setGeometry(QtCore.QRect(190, 420, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Decimalbutton.setFont(font)
        self.Decimalbutton.setObjectName("Decimalbutton")
        self.Equalbutton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.math_it())
        self.Equalbutton.setGeometry(QtCore.QRect(270, 420, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.Equalbutton.setFont(font)
        self.Equalbutton.setObjectName("Equalbutton")
        self.Eightbutton.raise_()
        self.label.raise_()
        self.Percentbutton.raise_()
        self.Cbutton.raise_()
        self.Arrowbutton.raise_()
        self.Minusbutton.raise_()
        self.Sevenbutton.raise_()
        self.Ninebutton.raise_()
        self.Multiplybutton.raise_()
        self.Fourbutton.raise_()
        self.Fivebutton.raise_()
        self.Sixbutton.raise_()
        self.Dividedbutton.raise_()
        self.Onebutton.raise_()
        self.Plusminusbutton.raise_()
        self.Twobutton.raise_()
        self.Zerobutton.raise_()
        self.Threebutton.raise_()
        self.Plusbutton.raise_()
        self.Decimalbutton.raise_()
        self.Equalbutton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #remove character
    def remove_it(self):
        screen = self.output.text()
        #remove last item in list/string
        screen = screen[:-1]
        #Output back to the screen
        self.label.setText(screen)

    #math part
    def math_it(self):
        #Grab what is on the screen
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("Error")    

        

    #change from positive to negative
    def plus_minus_it(self):
        screen = self.label.text()
        if "-" in screen:
            self.label.setText(screen.replace("-",""))
        else:
            self.label.setText(f'-{screen}')



    def dot_it(self):
        screen = self.label.text()
        if screen[-1] == ".":
            pass
        else:
            self.output.setText(f'{screen}.')
    

    def press_it(self, pressed):
        if pressed == "C":
            self.label.setText("0")
        else:
            #check to see if start 0 and delete 0
            if self.label.text() == "0":
                self.label.setText("")
            #concanate the pressed button with what was there already
            self.label.setText(f'{self.label.text()}{pressed}')
       

    





       








    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.label.setText(_translate("Dialog", "0"))
        self.Percentbutton.setText(_translate("Dialog", "%"))
        self.Cbutton.setText(_translate("Dialog", "C"))
        self.Arrowbutton.setText(_translate("Dialog", "<<"))
        self.Minusbutton.setText(_translate("Dialog", "-"))
        self.Sevenbutton.setText(_translate("Dialog", "7"))
        self.Eightbutton.setText(_translate("Dialog", "8"))
        self.Ninebutton.setText(_translate("Dialog", "9"))
        self.Multiplybutton.setText(_translate("Dialog", "x"))
        self.Fourbutton.setText(_translate("Dialog", "4"))
        self.Fivebutton.setText(_translate("Dialog", "5"))
        self.Sixbutton.setText(_translate("Dialog", "6"))
        self.Dividedbutton.setText(_translate("Dialog", "/"))
        self.Onebutton.setText(_translate("Dialog", "1"))
        self.Plusminusbutton.setText(_translate("Dialog", "+/-"))
        self.Twobutton.setText(_translate("Dialog", "2"))
        self.Zerobutton.setText(_translate("Dialog", "0"))
        self.Threebutton.setText(_translate("Dialog", "3"))
        self.Plusbutton.setText(_translate("Dialog", "+"))
        self.Decimalbutton.setText(_translate("Dialog", "."))
        self.Equalbutton.setText(_translate("Dialog", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
