# -*- coding: utf-8 -*-
import style
# Form implementation generated from reading ui file 'trueMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 301, 721))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setContentsMargins(25, 30, 25, 30)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../pythonProject/icons/scan.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.widget_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pythonProject/icons/accueil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.compare_btn_2 = QtWidgets.QPushButton(self.widget_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../pythonProject/icons/plagiat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.compare_btn_2.setIcon(icon1)
        self.compare_btn_2.setCheckable(True)
        self.compare_btn_2.setAutoExclusive(True)
        self.compare_btn_2.setObjectName("compare_btn_2")
        self.verticalLayout_2.addWidget(self.compare_btn_2)
        self.online_btn_2 = QtWidgets.QPushButton(self.widget_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../pythonProject/icons/online-survey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.online_btn_2.setIcon(icon2)
        self.online_btn_2.setCheckable(True)
        self.online_btn_2.setAutoExclusive(True)
        self.online_btn_2.setObjectName("online_btn_2")
        self.verticalLayout_2.addWidget(self.online_btn_2)
        self.maybe_btn_2 = QtWidgets.QPushButton(self.widget_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../pythonProject/icons/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maybe_btn_2.setIcon(icon3)
        self.maybe_btn_2.setCheckable(True)
        self.maybe_btn_2.setAutoExclusive(True)
        self.maybe_btn_2.setObjectName("maybe_btn_2")
        self.verticalLayout_2.addWidget(self.maybe_btn_2)
        self.setting_btn_2 = QtWidgets.QPushButton(self.widget_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../pythonProject/icons/parametres.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_btn_2.setIcon(icon4)
        self.setting_btn_2.setCheckable(True)
        self.setting_btn_2.setAutoExclusive(True)
        self.setting_btn_2.setObjectName("setting_btn_2")
        self.verticalLayout_2.addWidget(self.setting_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 155, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.help_btn_2 = QtWidgets.QPushButton(self.widget_4)
        self.help_btn_2.setObjectName("help_btn_2")
        self.verticalLayout_4.addWidget(self.help_btn_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(300, 40, 991, 721))
        self.widget_3.setObjectName("widget_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 30, 991, 641))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(480, 240, 55, 16))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_4 = QtWidgets.QLabel(self.page_8)
        self.label_4.setGeometry(QtCore.QRect(530, 240, 55, 16))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_8)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(480, 260, 55, 16))
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page_2)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_11 = QtWidgets.QLabel(self.page_9)
        self.label_11.setGeometry(QtCore.QRect(410, 280, 55, 16))
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_12 = QtWidgets.QLabel(self.page_10)
        self.label_12.setGeometry(QtCore.QRect(520, 220, 55, 16))
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.page_10)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(300, 0, 991, 61))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 30, 0)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_17.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../pythonProject/icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_3.addWidget(self.pushButton_17)
        spacerItem5 = QtWidgets.QSpacerItem(316, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.mode_btn_2 = QtWidgets.QPushButton(self.widget_2)
        self.mode_btn_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../pythonProject/icons/dark-mode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mode_btn_2.setIcon(icon6)
        self.mode_btn_2.setObjectName("mode_btn_2")
        self.horizontalLayout_3.addWidget(self.mode_btn_2)
        self.language_btn_2 = QtWidgets.QPushButton(self.widget_2)
        self.language_btn_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../pythonProject/icons/languages.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.language_btn_2.setIcon(icon7)
        self.language_btn_2.setObjectName("language_btn_2")
        self.horizontalLayout_3.addWidget(self.language_btn_2)
        self.info_btn_2 = QtWidgets.QPushButton(self.widget_2)
        self.info_btn_2.setText("")
        self.info_btn_2.setIcon(icon3)
        self.info_btn_2.setObjectName("info_btn_2")
        self.horizontalLayout_3.addWidget(self.info_btn_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.compare_btn_2.setText(_translate("MainWindow", "Comparer deux fichiers"))
        self.online_btn_2.setText(_translate("MainWindow", "Plagiat en ligne"))
        self.maybe_btn_2.setText(_translate("MainWindow", "???"))
        self.setting_btn_2.setText(_translate("MainWindow", "paramètre"))
        self.help_btn_2.setText(_translate("MainWindow", "kjhgfg"))
        self.label_3.setText(_translate("MainWindow", "hooome"))
        self.label_4.setText(_translate("MainWindow", "22222"))
        self.label_10.setText(_translate("MainWindow", "onlineee"))
        self.label_11.setText(_translate("MainWindow", "whaaaaaaaat"))
        self.label_12.setText(_translate("MainWindow", "parametre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # loading css
    with open("style.qss", "r") as style_file:
        style_str = style.file.read()
    app.setStyleSheet(style_str)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())