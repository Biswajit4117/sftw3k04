# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerdialog.ui'
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
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_registerDialog(object):
    def setupUi(self, registerDialog):
        if not registerDialog.objectName():
            registerDialog.setObjectName(u"registerDialog")
        registerDialog.resize(256, 120)
        self.formLayout = QFormLayout(registerDialog)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(registerDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.userName = QLineEdit(registerDialog)
        self.userName.setObjectName(u"userName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.userName)

        self.label_2 = QLabel(registerDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.newPassword = QLineEdit(registerDialog)
        self.newPassword.setObjectName(u"newPassword")
        self.newPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.newPassword)

        self.label_3 = QLabel(registerDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.repeatPassword = QLineEdit(registerDialog)
        self.repeatPassword.setObjectName(u"repeatPassword")
        self.repeatPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.repeatPassword)

        self.buttonBox = QDialogButtonBox(registerDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.buttonBox)


        self.retranslateUi(registerDialog)
        self.buttonBox.accepted.connect(registerDialog.accept)
        self.buttonBox.rejected.connect(registerDialog.reject)

        QMetaObject.connectSlotsByName(registerDialog)
    # setupUi

    def retranslateUi(self, registerDialog):
        registerDialog.setWindowTitle(QCoreApplication.translate("registerDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("registerDialog", u"New Username:", None))
        self.label_2.setText(QCoreApplication.translate("registerDialog", u"New password:", None))
        self.label_3.setText(QCoreApplication.translate("registerDialog", u"Repeat password:", None))
    # retranslateUi

