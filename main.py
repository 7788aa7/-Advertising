#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from PySide import QtGui, QtCore
import paho.mqtt.client as mqtt
from index_ui import Ui_MainWindow
from subprocess import Popen
import RPi.GPIO as GPIO
from MachineFactory import MachineFactory, Reply
import time


class Window(QtGui.QWidget, Ui_MainWindow):

    '''
    mode = 0 => 未投幣
    mode = 1 => 投幣
    mode = 2 => 儲值
    mode = 3 => 儲值完成等待
    mode = 4 => 發生卡幣(故障)
    mode = 5 => 卡幣儲值
    mode = 6 => mqtt斷線
    '''

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle('main')
        self.setupUi(self)

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.IN)  # 兌幣
        GPIO.setup(15, GPIO.OUT)  # 第一組馬達
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 50
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 100

        GPIO.output(15, True)

        # 用omxplayer播放影片
        xy = ("0 0 600 338")
        movie1 = ("./Video/C.mp4")
        omxc = Popen(['omxplayer', '--loop', '--win', xy, movie1, '&'])

        self.mode = 0  # 狀態
        self.money = 0  # 金額

        self.connection_status = False  # 連線狀態(預設無連線)
        self.exchange_error = True  # 兌幣功能狀態(預設正常)

        QtGui.QApplication.setOverrideCursor(QtCore.Qt.BlankCursor)  # 隱藏鼠標

        # 偵測投幣計時器
        self.timer_coin = QtCore.QTimer(self)
        self.timer_coin.timeout.connect(self.detection_coin)

        self.factory = MachineFactory()
        self.reply = Reply()
        self.replyList = self.reply.ReplyText()

        # 載入機台設定
        setup_list = list(self.factory.loadAll())
        self.machineId = setup_list[0]
        self.storeName = setup_list[3]
        self.quantity = setup_list[4]
        self.online = setup_list[9]

        # 檢查有無未兌出記錄
        check_list = self.factory.malfunction_check()
        print check_list
        if check_list:
            self.mode = 1
            self.money = check_list[1]
            self.label_2.setText(str(check_list[1]))
            self.label_4.setText(str(check_list[2]))
            self.exchange()
            self.factory.malfunction_update(check_list[0])
        else:
            self.timer_coin.start(125)
            print 'timer_coin_start'

        self.exchange_button.clicked.connect(self.exchange)
        self.gift_button.clicked.connect(self.gift_ask)
        self.cancel_button.clicked.connect(self.cancel)

        if self.online == 1:
            # mqtt執行緒
            self.mqtt = Mqtt()
            self.mqtt.start()
            # 當有訊息送過來時執行指定函式
            self.mqtt.dataReady.connect(
                self.analysis, QtCore.Qt.QueuedConnection)
            self.mqtt.connection_status.connect(
                self.analysis, QtCore.Qt.QueuedConnection)
            self.message1.setText(u"儲值功能暫停使用")

            # 測試按鈕
            self.pushButton1 = QtGui.QPushButton(self)
            self.pushButton1.setGeometry(QtCore.QRect(0, 500, 50, 50))
            self.pushButton1.setText(u"#123")
            self.pushButton1.clicked.connect(self.mqtt.test)
        else:
            self.gift_button.close()

        # 時鐘
        '''
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updtTime)
        timer.start(1)
        '''

        # 退出
        quitAction = QtGui.QAction(self, shortcut="ESC", triggered=self.close)
        self.addAction(quitAction)
        quitAction.triggered.connect(self.closevideo)

    # 更新時鐘
    def updtTime(self):
        '''
        currentTime = QtCore.QDateTime.currentDateTime().toString('hh:mm:ss')
        self.clock.setText(currentTime)
        '''

    # 讀取投幣訊號
    def detection_coin(self):
        inputValue1 = GPIO.input(18)
        inputValue2 = GPIO.input(22)
        if inputValue1 == False:
            self.Put_in(u'50')
        if inputValue2 == False:
            self.Put_in(u'100')

    # 關閉omxplayer
    def closevideo(self):
        os.system('killall omxplayer.bin')
        GPIO.cleanup()

    # mqtt內容判斷
    def analysis(self, string):
        if string[0] == '#':
            if self.mode == 1:
                self.mode = 2
            elif self.mode == 4:
                self.mode = 5
            self.key = string
            self.gift_show1()
        elif string == 'success':
            text = "#123"
            image_url = './UI/member.png'
            self.Dialog_box(text, image_url)
            self.gift_end()
        elif string == 'connrct success':
            self.connection_status = True
            self.returnmain()
        elif string == 'disconnection':
            self.connection_status = False
            self.returnmain()
        else:
            pass

    # 完成動作初始
    def returnmain(self):
        print 'returnmain'
        if self.online == 1:
            if self.connection_status:
                self.message1.setText(u"")
                if not self.exchange_error:
                    self.message1.setText(u"兌幣功能暫停使用")
            else:
                self.message1.setText(u"儲值功能暫停使用")
                if not self.exchange_error:
                    self.message1.setText(u"機台暫停使用")
        else:
            if not self.exchange_error:
                self.message1.setText(u"機台暫停使用")
        # 卡幣發生
        if self.mode == 4:
            if self.connection_status:
                # self.gift_button.setStyleSheet("background: #FF3333;")
                self.money = str(self.money_remainder)
            # self.cancel_button.setStyleSheet("background: #FF3333;")
        # 正常
        elif self.mode == 3:
            print '正常'
            self.money = 0
            self.mode = 0
            try:
                self.timer1.stop()
                self.timer_coin.start(150)
                print 'timer_coin.start'
            except:
                pass
            finally:
                self.timer_coin.start(150)
                print 'timer_coin.start'
                self.line_1.setText('')
                self.line_2.setText('')
                self.line_3.setText('')
                self.line_4.setText('')
                self.portrait_1.setStyleSheet("background: transparent;")
                self.portrait_2.setStyleSheet("background: transparent;")
                self.portrait_3.setStyleSheet("background: transparent;")
                self.portrait_4.setStyleSheet("background: transparent;")
                self.linebg_1.setStyleSheet("background: transparent;")
                self.linebg_2.setStyleSheet("background: transparent;")
                self.linebg_3.setStyleSheet("background: transparent;")
                self.linebg_4.setStyleSheet("background: transparent;")
                # self.exchange_button.setStyleSheet("background: #C0C0C0;")
                # self.gift_button.setStyleSheet("background: #C0C0C0;")
                # self.cancel_button.setStyleSheet("background: #C0C0C0;")

    # 投幣顯示金額
    def Put_in(self, money):
        if self.connection_status or self.exchange_error:
            self.money = int(money)
            self.label_2.setText(money)
            self.label_4.setText(u'0')
            self.line_1.setText('')
            self.linebg_1.setStyleSheet("background: transparent;")
            self.portrait_1.setStyleSheet("background: transparent;")
            self.portrait_2.setStyleSheet("background: transparent;")
            self.portrait_3.setStyleSheet("background: transparent;")
            self.portrait_4.setStyleSheet("background: transparent;")
            if self.connection_status:
                if self.exchange_error:
                    self.mode = 1
                    # self.exchange_button.setStyleSheet("background: #FF3333;")
                    # self.gift_button.setStyleSheet("background: #FF3333;")
                else:
                    self.mode = 4
                    # self.gift_button.setStyleSheet("background: #FF3333;")
            else:
                self.mode = 6
                # self.exchange_button.setStyleSheet("background: #FF3333;")

    # 兌幣按鈕動作
    def exchange(self):
        if self.mode == 1 or self.mode == 6:
            # self.exchange_button.setStyleSheet("background: #C0C0C0;")
            # self.gift_button.setStyleSheet("background: #C0C0C0;")

            self.money_coin = self.money
            self.coin = 0

            self.timer_coin.stop()

            self.error_con = 0

            self.timer_detection = QtCore.QTimer(self)
            self.timer_detection.timeout.connect(self.sensor)

            self.timer_error = QtCore.QTimer(self)
            self.timer_error.timeout.connect(self.counter)

            self.motor_action()

        elif self.mode == 2 or self.mode == 3 or self.mode == 4:
            pass
        else:
            statements = self.replyList[0]
            self.portrait_1.setStyleSheet(
                "background-image:url(./UI/member1.png);")
            self.line_1.setText(statements)
            self.linebg_1.setStyleSheet(
                "background-image:url(./UI/dialog.png);")

    # 讀取兌幣訊號
    def detection(self):
        # inputValue = GPIO.input(12)
        # if inputValue == False:
        self.conuter_num = 4
        self.coinexchange()
        if self.money_coin == 0:
            try:
                # self.timer_detection.stop()
                self.timer_error.stop()
            except:
                pass
            self.coinexchange()

    # 退幣馬達動作
    def motor_action(self):
        GPIO.output(15, False)
        self.conuter_num = 4
        self.a = 0
        # self.timer_detection.start(1)
        self.timer_error.start(1000)
        while self.money_coin > 0:
            inputValue = GPIO.input(12)
            if inputValue == True:
                self.a += 1
                print self.a
                self.detection()

    def sensor(self):
        if GPIO.event_detected(12):
            print 'event_detected'
            self.detection()

    # 計數馬達啟動次數
    def counter(self):
        self.conuter_num -= 1
        print self.conuter_num
        print self.error_con
        print ''
        if self.conuter_num == 0:
            self.error_con += 1
            self.detection_error()

    # 兌幣動作及記錄
    def coinexchange(self):
        if self.money_coin == 0:
            GPIO.output(15, True)
            preset_quantity = self.factory.loadData()
            self.factory.insert("CM_0000001", self.money, 0, self.coin)
            preset_quantity = preset_quantity - (self.money / 10)
            self.factory.update(preset_quantity)
            if preset_quantity < 10:
                self.exchange_error = False
            if self.mode != 4:
                self.mode = 3
            self.returnmain()
        else:
            self.money_coin -= 10
            self.coin += 1
            self.label_2.setText(str(self.money_coin))
            self.label_4.setText(str(self.coin))

    # 偵測卡幣或無幣
    def detection_error(self):
        self.timer_error.stop()
        # self.timer_detection.stop()
        if self.money_coin == 0:
            pass
        elif self.error_con >= 3:
            self.mode = 4
            self.exchange_error = False
            text = self.replyList[5]
            image_url = './UI/member1.png'
            self.Dialog_box(text, image_url)

            text = self.replyList[6]
            image_url = './UI/member1.png'
            self.Dialog_box(text, image_url)

            self.malfunction()
        else:
            GPIO.output(15, True)
            time.sleep(2)
            self.motor_action()

    # 卡幣,無幣或故障
    def malfunction(self):
        self.money_remainder = self.money_coin
        self.money = self.money - self.money_coin
        self.money_coin = 0
        self.message1.setText(u"兌幣功能暫停使用")
        # self.factory.malfunction(self.money_remainder, self.coin)
        self.coinexchange()

    # 向server傳送金額及要求序號(儲值按鈕動作)
    def gift_ask(self):
        if self.mode == 1 or self.mode == 4:
            self.mqtt.number(self.machineId, str(self.money))
        elif self.mode == 3 or self.mode == 6:
            pass
        else:
            statements = self.replyList[0]
            self.portrait_1.setStyleSheet(
                "background-image:url(./UI/member1.png);")
            self.line_1.setText(statements)
            self.linebg_1.setStyleSheet(
                "background-image:url(./UI/dialog.png);")

    # 取得序號顯示
    def gift_show1(self):
        # self.exchange_button.setStyleSheet("background: #C0C0C0;")
        # self.gift_button.setStyleSheet("background: #C0C0C0;")
        # self.cancel_button.setStyleSheet("background: #FF3333;")

        statements = self.replyList[1]
        statements_1 = self.replyList[2]

        if self.mode == 2 or self.mode == 5:
            text = statements.strip() + self.key + statements_1
            image_url = './UI/member1.png'
            self.Dialog_box(text, image_url)

            self.timer1 = QtCore.QTimer(self)
            self.timer1.timeout.connect(self.cancel)
            self.timer1.start(30000)  # 單位ms

    # 收到序號正確
    def gift_end(self):
        text = self.replyList[3]
        image_url = './UI/member1.png'
        self.Dialog_box(text, image_url)

        self.mode = 3
        # self.cancel_button.setStyleSheet("background: #C0C0C0;")

        self.timer1 = QtCore.QTimer(self)
        self.timer1.timeout.connect(self.returnmain)
        self.timer1.start(5000)  # 單位ms

    # 取消按鈕動作
    def cancel(self):
        if self.mode == 2 or self.mode == 5:
            try:
                self.timer1.stop()
            except:
                pass
            finally:
                text = self.replyList[4]
                image_url = './UI/member1.png'
                self.Dialog_box(text, image_url)

            if self.mode == 2:
                self.mode = 1
                # self.exchange_button.setStyleSheet("background: #FF3333;")
                # self.cancel_button.setStyleSheet("background: #C0C0C0;")
            else:
                self.mode = 4
            self.mqtt.cancel(self.machineId, self.key)
            # self.gift_button.setStyleSheet("background: #FF3333")
        elif self.mode == 4:
            self.mode = 3
            self.returnmain()

    # 對話窗
    def Dialog_box(self, string, image):
        text = string
        image_url = "background-image:url(" + image + ");"
        if self.line_1.text() == '':
            self.portrait_1.setStyleSheet(image_url)
            self.linebg_1.setStyleSheet(
                "background-image:url(./UI/dialog.png);")
            self.line_1.setText(text)
        elif self.line_2.text() == '':
            self.portrait_2.setStyleSheet(image_url)
            self.linebg_2.setStyleSheet(
                "background-image:url(./UI/dialog.png);")
            self.line_2.setText(text)
        elif self.line_3.text() == '':
            self.portrait_3.setStyleSheet(image_url)
            self.linebg_3.setStyleSheet(
                "background-image:url(./UI/dialog.png);")
            self.line_3.setText(text)
        elif self.line_4.text() == '':
            self.portrait_4.setStyleSheet(image_url)
            self.linebg_4.setStyleSheet(
                "background-image:url(./UI/dialog.png);")
            self.line_4.setText(text)
        else:
            text2 = self.line_2.text()
            text3 = self.line_3.text()
            text4 = self.line_4.text()
            self.line_1.setText(text2)
            self.line_2.setText(text3)
            self.line_3.setText(text4)
            styleSheet2 = self.portrait_2.styleSheet()
            styleSheet3 = self.portrait_3.styleSheet()
            styleSheet4 = self.portrait_4.styleSheet()
            self.portrait_1.setStyleSheet(styleSheet2)
            self.portrait_2.setStyleSheet(styleSheet3)
            self.portrait_3.setStyleSheet(styleSheet4)
            self.portrait_4.setStyleSheet(image_url)
            self.line_4.setText(text)


class Mqtt(QtCore.QThread):
    # mqtt執行緒
    """docstring for Mqtt"""
    dataReady = QtCore.Signal(object)
    connection_status = QtCore.Signal(object)

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        # mqtt 設定
        self.broker = "192.168.0.129"  # IP 106.104.5.195
        client_id = "python_123"  # 機台號碼
        clean_session = True
        userdata = None
        protocol = "MQTTv311"
        transport = "tcp"
        self.topic_pub = 'ABC'     # 要送出的版 ABC
        self.topic_sub = 'ABC'     # 要訂閱的版 ABC
        self.client = mqtt.Client(
            client_id, clean_session, userdata, protocol, transport)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def run(self):
        while 1:
            try:
                self.client.connect(self.broker, 1883, 60)  # 連接
                self.client.loop_forever()
                break
            except:
                self.client.disconnect()

    # 訂閱
    def on_connect(self, client, userdata, rc, topic_sub):
        # print('\n' + "Connected with result code " + str(rc))
        self.client.subscribe(self.topic_sub)
        self.connection_status.emit(u'connrct success')

    # 收訊
    def on_message(self, client, userdata, msg):
        # print('\n' + msg.topic + " " + str(msg.payload))
        # 將收到的訊息發送出去
        self.dataReady.emit(str(msg.payload))

    # 斷線
    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            self.connection_status.emit(u'disconnection')

    # 送出金額
    def number(self, machineId, money):
        self.client.publish(
            self.topic_pub, '{0},${1}'.format(machineId, money))

    # 取消儲值
    def cancel(self, machineId, key):
        self.client.publish(
            self.topic_pub, '{0},{1}'.format(machineId, key))

    # 測試輸入序號
    def test(self):
        self.client.publish(self.topic_pub, "%123")


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('main')
    window = Window()
    window.showFullScreen()  # 全螢幕
    sys.exit(app.exec_())
