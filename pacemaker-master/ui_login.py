# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(445, 247)
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.userName = QLineEdit(Login)
        self.userName.setObjectName(u"userName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.userName)

        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.password = QLineEdit(Login)
        self.password.setObjectName(u"password")
        self.password.setMaxLength(32767)
        self.password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.password)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.formLayout)

        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.registerButton = QPushButton(self.widget)
        self.registerButton.setObjectName(u"registerButton")

        self.gridLayout.addWidget(self.registerButton, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Login)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Login)
        self.buttonBox.accepted.connect(Login.accept)
        self.buttonBox.rejected.connect(Login.reject)
        self.registerButton.clicked.connect(Login.register)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText(QCoreApplication.translate("Login", u"UserName", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"<center><h1>Register</h1><p>Don't have an account?</p></center>", None))
        self.registerButton.setText(QCoreApplication.translate("Login", u"Register", None))
    # retranslateUi

