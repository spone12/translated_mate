# Translated mate v0.1
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(885, 385)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(885, 385))
        MainWindow.setMaximumSize(QtCore.QSize(885, 385))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #b8b6b6;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.inputBox.setGeometry(QtCore.QRect(10, 60, 420, 280))
        self.inputBox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(245, 245, 247);\n"
"border-radius: 5% 20% / 10% 40%;")
        self.inputBox.setObjectName("inputBox")
        self.translateBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.translateBox.setEnabled(False)
        self.translateBox.setGeometry(QtCore.QRect(450, 60, 420, 280))
        self.translateBox.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-radius: 5% 20% / 10% 40%;\n"
"background-color: rgb(245, 245, 247);")
        self.translateBox.setObjectName("translateBox")
        self.fromLang = QtWidgets.QComboBox(parent=self.centralwidget)
        self.fromLang.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.fromLang.setStyleSheet("border-radius: 10px;\n"
"background: white;")
        self.fromLang.setObjectName("fromLang")
        self.fromLang.addItem("")
        self.fromLang.addItem("")
        self.toLang = QtWidgets.QComboBox(parent=self.centralwidget)
        self.toLang.setGeometry(QtCore.QRect(670, 10, 200, 30))
        self.toLang.setStyleSheet("border-radius: 10px;\n"
"background: white;")
        self.toLang.setObjectName("toLang")
        self.toLang.addItem("")
        self.toLang.addItem("")
        self.translateLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.translateLabel.setGeometry(QtCore.QRect(430, 20, 30, 30))
        self.translateLabel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.translateLabel.setAutoFillBackground(False)
        self.translateLabel.setStyleSheet("\n"
"background-size: 30px;\n"
"background-repeat: no-repeat;")
        self.translateLabel.setText("")
        self.translateLabel.setPixmap(QtGui.QPixmap("img/translation.png"))
        self.translateLabel.setScaledContents(True)
        self.translateLabel.setObjectName("translateLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 23))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translated mate"))
        self.inputBox.setPlaceholderText(_translate("MainWindow", "Input text"))
        self.fromLang.setItemText(0, _translate("MainWindow", "Русский"))
        self.fromLang.setItemText(1, _translate("MainWindow", "English"))
        self.toLang.setItemText(0, _translate("MainWindow", "Русский"))
        self.toLang.setItemText(1, _translate("MainWindow", "English"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
