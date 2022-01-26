import re
from sqlite3 import Time
from serial.tools import list_ports
from serial import Serial, STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO, FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS, \
    PARITY_NONE, PARITY_ODD, PARITY_EVEN, PARITY_MARK
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QThread, Signal, QMutex, QWaitCondition, Qt, QSize
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from untitled import Ui_Form


class ReceiveMessage(QThread):
    '''重构QThread'''
    update_date = Signal(object)
    update_count = Signal(object)

    def __init__(self, ser, count):
        super(ReceiveMessage, self).__init__()
        self.ser = ser
        self.stop_flag = False
        self._isPause = False
        self.count = count
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def pause(self):
        '''实现私有的线程休眠'''
        self._isPause = True

    def resume(self):
        '''实现私有的线程启动'''
        self._isPause = False
        self.cond.wakeAll()

    def run(self):
        while True:
            self.mutex.lock()
            if self.ser.in_waiting:
                self.count += 1
                string = self.ser.readline(self.ser.in_waiting)
                self.update_date.emit(string)
                self.update_count.emit(f'接收：{self.count}')
            if self._isPause:
                self.cond.wait(self.mutex)
            if self.stop_flag:
                break
            self.msleep(20)
            self.mutex.unlock()

    def Count(self, count):
        self.count = count

    def stop(self):
        '''实现私有的线程销毁'''
        self.stop_flag = True


class SendMessage(QThread):
    '''重构QThread'''
    update_date = Signal(object)
    update_count = Signal(object)

    def __init__(self, ser, string, time, encodings, count):
        super(SendMessage, self).__init__()
        self.ser = ser
        self.string = string
        self.time = float(time)*1000
        self.encodings = encodings
        self.count = count
        self.stop_flag = False
        self._isPause = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def pause(self):
        '''实现私有的线程休眠'''
        self._isPause = True

    def resume(self):
        '''实现私有的线程启动'''
        self._isPause = False
        self.cond.wakeAll()

    def run(self):

        while True:
            self.mutex.lock()
            self.count += 1
            self.ser.write(self.string.encode(self.encodings))
            self.update_date.emit('>> ' + self.string.replace('\n', ''))
            self.update_count.emit(f'发送：{self.count}')
            if self._isPause:
                self.cond.wait(self.mutex)
            if self.stop_flag:
                break
            self.msleep(int(self.time))
            self.mutex.unlock()

    def Encodings(self, encodings):
        self.encodings = encodings

    def Time(self, time):
        self.time = time

    def signal(self, string):
        self.string = string

    def Count(self, count):
        self.count = count

    def stop(self):
        '''实现私有的线程销毁'''
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
        '''初始化'''
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.textEdit.setPlaceholderText('Enter')
        self.ui.textBrowser.document().setMaximumBlockCount(300)
        self.SendCount = 0
        self.RendCount = 0
        self.encodings = 'GBK'
        self.Reflag = False
        self.Seflag = False

    def Button(self):
        '''按钮设置'''
        self.ui.Button1.clicked.connect(self.switchSerial)
        self.ui.Button2.clicked.connect(self.WriteSerial)
        self.ui.Button3.clicked.connect(self.Combox)
        self.ui.buttonGroup.buttonClicked.connect(self.Encodings)
        self.ui.checkBox_3.clicked.connect(self.pauseMessage)
        self.ui.checkBox_5.clicked.connect(self.TimeWriteSerial)
        self.ui.pushButton_2.clicked.connect(self.ResetCount)
        self.ui.checkBox.clicked.connect(self.PauseSending)

    def Combox(self):
        '''复选框设置'''
        self.ui.com.clear()
        ports = list(list_ports.comports())
        temp = [f'COM{i + 1}' for i, j in enumerate(ports)]
        if len(ports):
            self.ui.com.addItems(temp)

    def Bps(self):
        '''复选框设置'''
        temp = ['600', '1200', '2400', '4800', '9600', '19200', '38400']
        self.ui.bps.addItems(temp)

    def Stopbits(self):
        '''复选框设置'''
        self.stopbits = {'One': STOPBITS_ONE,
                         'OnePointFive': STOPBITS_ONE_POINT_FIVE, 'Two': STOPBITS_TWO}
        for self.Key in self.stopbits:
            self.ui.stopbits.addItem(self.Key)

    def Bytesize(self):
        '''复选框设置'''
        self.bytesize = {'5': FIVEBITS, '6': SIXBITS,
                         '7': SEVENBITS, '8': EIGHTBITS}
        for self.Key in self.bytesize:
            self.ui.bytesize.addItem(self.Key)

    def Parity(self):
        '''复选框设置'''
        self.parity = {'None': PARITY_NONE, 'Odd': PARITY_ODD,
                       'Even': PARITY_EVEN, 'MARK': PARITY_MARK}
        for self.Key in self.parity:
            self.ui.parity.addItem(self.Key)

    def switchSerial(self):
        '''按钮形态切换'''
        if self.ui.Button1.text() == '打开串口':
            self.OpenSerial()
            self.ui.Button1.setText('关闭串口')
        elif self.ui.Button1.text() == '关闭串口':
            self.CloseSerial()
            self.ui.Button1.setText('打开串口')

    def OpenSerial(self):
        '''打开串口，创建线程'''
        self.ui.textBrowser.clear()
        if len(self.ui.textBrowser.toPlainText()):
            self.ui.textBrowser.append('连接成功!')
        try:
            self.ser = Serial(self.ui.com.currentText(),
                              int(self.ui.bps.currentText()),
                              self.bytesize[self.ui.bytesize.currentText()],
                              self.parity[self.ui.parity.currentText()],
                              self.stopbits[self.ui.stopbits.currentText()])
            if self.ser.is_open:
                self.Reflag = True
                self.th = ReceiveMessage(self.ser, self.RendCount)
                self.th.update_date.connect(self.handleDisplay)
                self.th.update_count.connect(self.label2Display)
                self.th.start()
        except:
            self.ui.textBrowser.append('连接失败!')
            self.ui.textBrowser.ensureCursorVisible()

    def CloseSerial(self):
        '''关闭串口，销毁线程'''
        if len(self.ui.textBrowser.toPlainText()):
            self.ui.textBrowser.clear()
        self.ser.close()
        self.th.stop()

    def pauseMessage(self):
        '''暂停接收线程'''
        if self.ui.checkBox_3.isChecked() and self.Reflag:
            self.th.pause()
        elif self.ui.checkBox_3.isChecked() == False and self.Reflag:
            self.th.resume()

    def PauseSending(self):
        '''暂停发送线程'''
        if self.Seflag and self.ui.checkBox.isChecked():
            self.thse.pause()
        elif self.ui.checkBox.isChecked() == False and self.Seflag:
            self.thse.resume()

    def ResetCount(self):
        '''槽方法，复位计数'''
        self.SendCount = 0
        self.RendCount = 0
        if self.Seflag:
            self.thse.Count(self.SendCount)
        if self.Reflag:
            self.th.Count(self.RendCount)
        Send_Count = f'发送：{self.SendCount}'
        Rend_Count = f'发送：{self.RendCount}'
        self.ui.label1.setText(Send_Count)
        self.ui.label2.setText(Rend_Count)

    def WriteSerial(self):
        '''槽方法，发送消息'''
        if self.Reflag:
            Text = self.ui.textEdit.toPlainText() + '\n'
            self.ser.write(Text.encode(self.encodings))
            self.ui.textBrowser.append('>> ' + self.ui.textEdit.toPlainText())
            self.SendCount += 1
            Text = f'发送：{self.SendCount}'
            self.ui.label1.setText(Text)

    def TimeWriteSerial(self):
        '''槽方法，创建一个循环发送消息的线程'''
        if self.Reflag and self.ui.checkBox_5.isChecked():
            self.Seflag = True
            Text = self.ui.textEdit.toPlainText() + '\n'
            self.thse = SendMessage(
                self.ser, Text, self.ui.lineEdit.text(), self.encodings, self.SendCount)
            self.thse.update_date.connect(self.DisplayWriteSerial)
            self.thse.update_count.connect(self.label1Display)
            self.thse.start()
        elif self.ui.checkBox_5.isChecked() == False and self.Seflag:
            self.thse.stop()

    def DisplayWriteSerial(self, string):
        '''槽方法，显示发送的文本'''
        Text = self.ui.textEdit.toPlainText()+'\n'
        if self.ui.checkBox_4.isChecked():
            Text = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", Text.encode(
                self.encodings).hex().upper()) + '\n'
        Time = float(self.ui.lineEdit.text())*1000
        self.thse.Encodings(self.encodings)
        self.thse.Time(int(Time))
        self.thse.signal(Text)
        self.ui.textBrowser.append(string)

    def label1Display(self, count):
        '''槽方法，显示发送的数量'''
        self.SendCount += 1
        self.thse.Count(self.SendCount)
        self.ui.label1.setText(count)

    def Encodings(self):
        '''槽方法，设置字符编码'''
        self.encodings = self.ui.buttonGroup.checkedButton().text()

    def label2Display(self, count):
        '''槽方法，显示收到的数量'''
        self.RendCount += 1
        self.th.Count(self.RendCount)
        self.ui.label2.setText(count)

    def handleDisplay(self, string):
        '''槽方法，显示收到的文本'''
        string = string.decode(self.encodings)
        if self.ui.hexDisplay.isChecked():
            string = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", string.encode(
                self.encodings).hex().upper())
        self.ui.textBrowser.append('<< '+string)


app = QApplication([])
MainWindow = MainWindow()
MainWindow.show()
app.exec_()
