# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Mouse Training Game")
        MainWindow.resize(529, 448)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.startBtn = QPushButton(self.centralwidget)
        self.startBtn.setObjectName(u"startBtn")

        self.gridLayout.addWidget(self.startBtn, 1, 2, 1, 1)

        self.colorBtn = QPushButton(self.centralwidget)
        self.colorBtn.setObjectName(u"colorBtn")

        self.gridLayout.addWidget(self.colorBtn, 1, 0, 1, 1)

        self.nameBtn = QPushButton(self.centralwidget)
        self.nameBtn.setObjectName(u"nameBtn")

        self.gridLayout.addWidget(self.nameBtn, 1, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl = QLabel(self.frame)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setGeometry(QRect(130, 150, 91, 16))
        self.lbl.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 529, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.colorBtn.clicked.connect(MainWindow.nameChanged)
        self.nameBtn.clicked.connect(MainWindow.colorChanged)
        self.startBtn.clicked.connect(MainWindow.start)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.colorBtn.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984 \ubcc0\uacbd", None))
        self.nameBtn.setText(QCoreApplication.translate("MainWindow", u"\ubc30\uacbd\uc0c9 \ubcc0\uacbd", None))
        self.lbl.setText(QCoreApplication.translate("MainWindow", u"\ub098\ub97c \ud074\ub9ad\ud574\ubd10~", None))
    # retranslateUi

