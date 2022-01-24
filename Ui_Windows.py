from PySide2.QtCore import QSize, QRect, QCoreApplication, QMetaObject
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QSizePolicy, QWidget, QFormLayout, QLabel, QComboBox, QPushButton, QPlainTextEdit, \
    QTextBrowser, QFrame


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(621, 422)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(621, 422))
        Form.setMaximumSize(QSize(621, 422))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 11, 158, 173))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.layoutWidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_1)

        self.com = QComboBox(self.layoutWidget)
        self.com.setObjectName(u"com")
        sizePolicy.setHeightForWidth(self.com.sizePolicy().hasHeightForWidth())
        self.com.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.com)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.bps = QComboBox(self.layoutWidget)
        self.bps.setObjectName(u"bps")
        sizePolicy.setHeightForWidth(self.bps.sizePolicy().hasHeightForWidth())
        self.bps.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.bps)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.bytesize = QComboBox(self.layoutWidget)
        self.bytesize.setObjectName(u"bytesize")
        sizePolicy.setHeightForWidth(self.bytesize.sizePolicy().hasHeightForWidth())
        self.bytesize.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.bytesize)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.parity = QComboBox(self.layoutWidget)
        self.parity.setObjectName(u"parity")
        sizePolicy.setHeightForWidth(self.parity.sizePolicy().hasHeightForWidth())
        self.parity.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.parity)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.Button1 = QPushButton(self.layoutWidget)
        self.Button1.setObjectName(u"Button1")
        sizePolicy.setHeightForWidth(self.Button1.sizePolicy().hasHeightForWidth())
        self.Button1.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.Button1)

        self.stopbits = QComboBox(self.layoutWidget)
        self.stopbits.setObjectName(u"stopbits")
        sizePolicy.setHeightForWidth(self.stopbits.sizePolicy().hasHeightForWidth())
        self.stopbits.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.stopbits)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.textEdit = QPlainTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(180, 340, 371, 51))
        self.Button2 = QPushButton(Form)
        self.Button2.setObjectName(u"Button2")
        self.Button2.setGeometry(QRect(560, 340, 51, 51))
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(181, 11, 431, 321))
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setTabletTracking(False)
        self.textBrowser.setOpenExternalLinks(False)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 180, 161, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label1 = QLabel(Form)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(180, 400, 100, 12))
        self.label2 = QLabel(Form)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(510, 400, 100, 12))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4e32\u53e3\u901a\u4fe1", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6ce2\u7279\u7387", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u4f4d", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6821\u9a8c\u4f4d", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u4e32\u53e3\u64cd\u4f5c", None))
        self.Button1.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u4e32\u53e3", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u4f4d", None))
        self.Button2.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.label1.setText(QCoreApplication.translate("Form", u"\u53d1\u9001:0", None))
        self.label2.setText(QCoreApplication.translate("Form", u"\u63a5\u53d7:0", None))
    # retranslateUi