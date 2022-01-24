from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QApplication, QWidget
from serial import Serial, STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO, FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS, \
    PARITY_NONE, PARITY_ODD, PARITY_EVEN, PARITY_MARK
from serial.tools import list_ports

from Ui_Windows import Ui_Form


class MyThread(QThread):
    update_date = Signal(str)
    update_count = Signal(str)

    def __init__(self, ser):
        super(MyThread, self).__init__()
        self.ser = ser
        self.stop_flag = False

    def run(self):
        count = 0
        while True:
            if self.ser.in_waiting:
                count += 1
                string = self.ser.read(self.ser.in_waiting).decode("gbk")
                self.update_date.emit(string)
                self.update_count.emit(f'接收：{count}')
            if self.stop_flag:
                break

    def stop(self):
        self.stop_flag = True


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.Button()
        self.Combox()
        self.Bps()
        self.Bytesize()
        self.Parity()
        self.Stopbits()

    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.textEdit.setPlaceholderText('Enter')
        self.ui.textBrowser.document().setMaximumBlockCount(100)

    def Button(self):
        self.ui.Button1.clicked.connect(self.switchSerial)

    def Combox(self):
        ports = list(list_ports.comports())
        temp = [f'COM{i + 1}' for i, j in enumerate(ports)]
        if len(ports):
            self.ui.com.addItems(temp)

    def Bps(self):
        temp = ['600', '1200', '2400', '4800', '9600', '19200', '38400']
        self.ui.bps.addItems(temp)

    def Stopbits(self):
        self.stopbits = {'One': STOPBITS_ONE, 'OnePointFive': STOPBITS_ONE_POINT_FIVE, 'Two': STOPBITS_TWO}
        for Key in self.stopbits:
            self.ui.stopbits.addItem(Key)

    def Bytesize(self):
        self.bytesize = {'5': FIVEBITS, '6': SIXBITS, '7': SEVENBITS, '8': EIGHTBITS}
        for Key in self.bytesize:
            self.ui.bytesize.addItem(Key)

    def Parity(self):
        self.parity = {'None': PARITY_NONE, 'Odd': PARITY_ODD, 'Even': PARITY_EVEN, 'MARK': PARITY_MARK}
        for Key in self.parity:
            self.ui.parity.addItem(Key)

    def switchSerial(self):
        if self.ui.Button1.text() == '打开串口':
            self.OpenSerial()
            self.ui.Button1.setText('关闭串口')
        elif self.ui.Button1.text() == '关闭串口':
            self.CloseSerial()
            self.ui.Button1.setText('打开串口')

    def OpenSerial(self):
        if len(self.ui.textBrowser.toPlainText()):
            self.ui.textBrowser.append('连接成功！')
            self.ui.textBrowser.clear()
        try:
            self.ser = Serial(self.ui.com.currentText(),
                              int(self.ui.bps.currentText()),
                              self.bytesize[self.ui.bytesize.currentText()],
                              self.parity[self.ui.parity.currentText()],
                              self.stopbits[self.ui.stopbits.currentText()])
            self.flag = self.ser.is_open
            if self.flag:
                self.th = MyThread(self.ser)
                self.th.update_date.connect(self.handleDisplay)
                self.th.update_count.connect(self.labelDisplay)
                self.th.start()
        except:
            self.ui.textBrowser.append('读取失败')
            self.ui.textBrowser.ensureCursorVisible()

    def CloseSerial(self):
        if len(self.ui.textBrowser.toPlainText()):
            self.ui.textBrowser.clear()
        self.ser.close()
        self.th.stop()

    def labelDisplay(self, count):
        self.ui.label2.setText(count)

    def handleDisplay(self, string):
        self.ui.textBrowser.append(string)


app = QApplication([])
MainWindow = MainWindow()
MainWindow.show()
app.exec_()
