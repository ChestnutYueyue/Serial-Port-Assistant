# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(740, 536)
        icon = QIcon()
        icon.addFile(u":/Ui/\u4e32\u53e3.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(7)
        self.gridLayout_4.setContentsMargins(0, -1, 0, 0)
        self.textEdit = QPlainTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(437, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 68))

        self.gridLayout_4.addWidget(self.textEdit, 1, 0, 1, 1)

        self.Button2 = QPushButton(Form)
        self.Button2.setObjectName(u"Button2")
        sizePolicy.setHeightForWidth(self.Button2.sizePolicy().hasHeightForWidth())
        self.Button2.setSizePolicy(sizePolicy)
        self.Button2.setMinimumSize(QSize(95, 68))
        self.Button2.setMaximumSize(QSize(16777215, 68))

        self.gridLayout_4.addWidget(self.Button2, 1, 1, 1, 1)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(0, 200))
        self.textBrowser.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 2)

        self.label2 = QLabel(Form)
        self.label2.setObjectName(u"label2")
        sizePolicy.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
        self.label2.setSizePolicy(sizePolicy)
        self.label2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.label2, 2, 1, 1, 1)

        self.label1 = QLabel(Form)
        self.label1.setObjectName(u"label1")
        self.label1.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.label1, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)


        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 10, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stopbits = QComboBox(Form)
        self.stopbits.setObjectName(u"stopbits")

        self.gridLayout.addWidget(self.stopbits, 4, 1, 1, 2)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.bytesize = QComboBox(Form)
        self.bytesize.setObjectName(u"bytesize")

        self.gridLayout.addWidget(self.bytesize, 2, 1, 1, 2)

        self.bps = QComboBox(Form)
        self.bps.setObjectName(u"bps")

        self.gridLayout.addWidget(self.bps, 1, 1, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.com = QComboBox(Form)
        self.com.setObjectName(u"com")

        self.gridLayout.addWidget(self.com, 0, 2, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.parity = QComboBox(Form)
        self.parity.setObjectName(u"parity")

        self.gridLayout.addWidget(self.parity, 3, 1, 1, 2)

        self.Button1 = QPushButton(Form)
        self.Button1.setObjectName(u"Button1")

        self.gridLayout.addWidget(self.Button1, 5, 1, 1, 2)

        self.Button3 = QPushButton(Form)
        self.Button3.setObjectName(u"Button3")
        self.Button3.setMinimumSize(QSize(0, 0))
        self.Button3.setMaximumSize(QSize(40, 60))
        icon1 = QIcon()
        icon1.addFile(u":/Ui/\u5237\u65b0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button3.setIcon(icon1)
        self.Button3.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.Button3, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.ascii = QRadioButton(Form)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.ascii)
        self.ascii.setObjectName(u"ascii")

        self.gridLayout_2.addWidget(self.ascii, 5, 1, 1, 1)

        self.shift = QRadioButton(Form)
        self.buttonGroup.addButton(self.shift)
        self.shift.setObjectName(u"shift")
        self.shift.setCheckable(True)
        self.shift.setChecked(False)

        self.gridLayout_2.addWidget(self.shift, 7, 1, 1, 1)

        self.gb2312 = QRadioButton(Form)
        self.buttonGroup.addButton(self.gb2312)
        self.gb2312.setObjectName(u"gb2312")

        self.gridLayout_2.addWidget(self.gb2312, 6, 1, 1, 1)

        self.hexDisplay = QCheckBox(Form)
        self.buttonGroup2 = QButtonGroup(Form)
        self.buttonGroup2.setObjectName(u"buttonGroup2")
        self.buttonGroup2.setExclusive(False)
        self.buttonGroup2.addButton(self.hexDisplay)
        self.hexDisplay.setObjectName(u"hexDisplay")

        self.gridLayout_2.addWidget(self.hexDisplay, 1, 0, 1, 2)

        self.gbk = QRadioButton(Form)
        self.buttonGroup.addButton(self.gbk)
        self.gbk.setObjectName(u"gbk")
        self.gbk.setChecked(True)

        self.gridLayout_2.addWidget(self.gbk, 7, 0, 1, 1)

        self.big5 = QRadioButton(Form)
        self.buttonGroup.addButton(self.big5)
        self.big5.setObjectName(u"big5")

        self.gridLayout_2.addWidget(self.big5, 5, 0, 1, 1)

        self.utf8 = QRadioButton(Form)
        self.buttonGroup.addButton(self.utf8)
        self.utf8.setObjectName(u"utf8")

        self.gridLayout_2.addWidget(self.utf8, 6, 0, 1, 1)

        self.checkBox_3 = QCheckBox(Form)
        self.buttonGroup2.addButton(self.checkBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 2, 0, 1, 2)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 2)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 2)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 60))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setVerticalSpacing(8)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.checkBox_5 = QCheckBox(Form)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout.addWidget(self.checkBox_5)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(86, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 3, 0, 1, 1)

        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_3.addWidget(self.checkBox_4, 1, 0, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QSize(16777215, 28))

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4e32\u53e3\u901a\u4fe1", None))
        self.Button2.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.label2.setText(QCoreApplication.translate("Form", u"\u63a5\u6536\uff1a0", None))
        self.label1.setText(QCoreApplication.translate("Form", u"\u53d1\u9001\uff1a0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u4e32\u53e3\u64cd\u4f5c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6ce2\u7279\u7387", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u4f4d", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u4f4d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6821\u9a8c\u4f4d", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3", None))
        self.Button1.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u4e32\u53e3", None))
        self.Button3.setText("")
        self.ascii.setText(QCoreApplication.translate("Form", u"ascii", None))
        self.shift.setText(QCoreApplication.translate("Form", u"shift_jis", None))
        self.gb2312.setText(QCoreApplication.translate("Form", u"gb2312", None))
        self.hexDisplay.setText(QCoreApplication.translate("Form", u"\u5341\u516d\u8fdb\u5236\u663e\u793a", None))
        self.gbk.setText(QCoreApplication.translate("Form", u"GBK", None))
        self.big5.setText(QCoreApplication.translate("Form", u"big5", None))
        self.utf8.setText(QCoreApplication.translate("Form", u"UTF-8", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u6682\u505c\u63a5\u6536\u663e\u793a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u5b57\u7b26\u7f16\u7801", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u63a5\u6536\u8bbe\u7f6e", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"\u5b9a\u65f6\u53d1\u9001", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"1", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u6682\u505c\u53d1\u9001", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u5341\u516d\u8fdb\u5236\u53d1\u9001", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u53d1\u9001\u8bbe\u7f6e", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u590d\u4f4d\u8ba1\u6570", None))
    # retranslateUi

