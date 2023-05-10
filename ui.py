# Form implementation generated from reading ui file 'TranslateMate.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(925, 385)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(925, 385))
        MainWindow.setMaximumSize(QtCore.QSize(925, 385))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("* {\n"
"   background-color: #b8b6b6;\n"
"   font: Fira Sans Condensed;     \n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.inputBox.setGeometry(QtCore.QRect(50, 60, 430, 280))
        self.inputBox.setStyleSheet("border: 1px solid black;\n"
"border-radius: 1% 20% / 10% 40%;\n"
"background: #f4f4f5;\n"
"font-size: 11px;")
        self.inputBox.setObjectName("inputBox")
        self.translateBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.translateBox.setEnabled(True)
        self.translateBox.setGeometry(QtCore.QRect(485, 60, 430, 280))
        self.translateBox.setStyleSheet("border: 1px solid black;\n"
"border-radius: 1% 20% / 10% 40%;\n"
"background: #f4f4f5;\n"
"font-size: 11px;")
        self.translateBox.setReadOnly(True)
        self.translateBox.setObjectName("translateBox")
        self.fromLang = QtWidgets.QComboBox(parent=self.centralwidget)
        self.fromLang.setGeometry(QtCore.QRect(50, 20, 200, 30))
        self.fromLang.setStyleSheet("#fromLang {\n"
"    font: 11pt Fira Sans Condensed;     \n"
"    background-color: #2e2e2e;\n"
"    border-top: 0px solid #3e3e3e;\n"
"    border-left: 0px solid #3e3e3e;\n"
"    border-right: 0px solid #3e3e3e;\n"
"    border-bottom: 2px solid #3e3e3e;\n"
"    padding: 5%;\n"
"    max-height: 30px;\n"
"    min-width: 140px;\n"
"    color: white;\n"
"    selection-background-color: #5e5e5e;\n"
"    border-radius: 2px;\n"
"}\n"
"#fromLang:drop-down {\n"
"    border: none;\n"
"}\n"
"#fromLang:down-arrow {\n"
"    image: url(img/downButton.png);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"    border-width: 0px;\n"
"    padding-right: 10px;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"#fromLang:pressed {\n"
"    position: relative;\n"
"    top: 1px; left: 1px;\n"
"}")
        self.fromLang.setEditable(True)
        self.fromLang.setObjectName("fromLang")
        self.toLang = QtWidgets.QComboBox(parent=self.centralwidget)
        self.toLang.setGeometry(QtCore.QRect(710, 20, 200, 30))
        self.toLang.setStyleSheet("#toLang {\n"
"    font: 11pt Fira Sans Condensed;     \n"
"    background-color: #2e2e2e;\n"
"    border-top: 0px solid #3e3e3e;\n"
"    border-left: 0px solid #3e3e3e;\n"
"    border-right: 0px solid #3e3e3e;\n"
"    border-bottom: 2px solid #3e3e3e;\n"
"    padding: 5%;\n"
"    max-height: 30px;\n"
"    min-width: 140px;\n"
"    color: white;\n"
"    selection-background-color: #5e5e5e;\n"
"    border-radius: 2px;\n"
"}\n"
"#toLang:drop-down {\n"
"    border: none;\n"
"}\n"
"#toLang:down-arrow {\n"
"    image: url(img/downButton.png);\n"
"    width: 25px;\n"
"    height: 25px;\n"
"    border-width: 0px;\n"
"    padding-right: 10px;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"#toLang:pressed {\n"
"    position: relative;\n"
"    top: 1px; left: 1px;\n"
"}")
        self.toLang.setEditable(True)
        self.toLang.setObjectName("toLang")
        self.translateLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.translateLabel.setGeometry(QtCore.QRect(10, 60, 30, 30))
        self.translateLabel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.translateLabel.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.translateLabel.setAutoFillBackground(False)
        self.translateLabel.setStyleSheet("#translateLabel {\n"
"    background-size: 30px;\n"
"    background-repeat: no-repeat;\n"
"     border-radius:  5px;\n"
"    backgournd-color:  none;\n"
"}\n"
"#translateLabel:hover  {\n"
"    background:  #fff6f7;\n"
"}")
        self.translateLabel.setText("")
        self.translateLabel.setPixmap(QtGui.QPixmap("img/translation.png"))
        self.translateLabel.setScaledContents(True)
        self.translateLabel.setObjectName("translateLabel")
        self.reverseTranslate = QtWidgets.QLabel(parent=self.centralwidget)
        self.reverseTranslate.setGeometry(QtCore.QRect(10, 100, 30, 30))
        self.reverseTranslate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.reverseTranslate.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.reverseTranslate.setAutoFillBackground(False)
        self.reverseTranslate.setStyleSheet("#reverseTranslate {\n"
"    background-size: 30px;\n"
"    background-repeat: no-repeat;\n"
"     border-radius:  5px;\n"
"    backgournd-color:  none;\n"
"}\n"
"#reverseTranslate:hover  {\n"
"    background:  #fff6f7;\n"
"}")
        self.reverseTranslate.setText("")
        self.reverseTranslate.setPixmap(QtGui.QPixmap("img/reverseTranslate.png"))
        self.reverseTranslate.setScaledContents(True)
        self.reverseTranslate.setObjectName("reverseTranslate")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(270, 40, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuTranslator = QtWidgets.QMenu(parent=self.menuMenu)
        self.menuTranslator.setObjectName("menuTranslator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGoogle = QtGui.QAction(parent=MainWindow)
        self.actionGoogle.setObjectName("actionGoogle")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuTranslator.addAction(self.actionGoogle)
        self.menuMenu.addAction(self.menuTranslator.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translated mate"))
        self.inputBox.setPlaceholderText(_translate("MainWindow", "Input text"))
        self.translateLabel.setToolTip(_translate("MainWindow", "Translate text"))
        self.reverseTranslate.setToolTip(_translate("MainWindow", "Reverse translate"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuTranslator.setTitle(_translate("MainWindow", "Translator"))
        self.actionGoogle.setText(_translate("MainWindow", "Google"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
