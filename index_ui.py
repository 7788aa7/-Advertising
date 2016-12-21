# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.lin = QtGui.QLabel(self.centralwidget)
        self.lin.setGeometry(QtCore.QRect(0, 0, 600, 1024))
        self.lin.setStyleSheet("background-image:url(./UI/bg.png);")
        # 文字設定
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setFamily("KaiTi")

        # 兌幣按鈕
        self.exchange_button = QtGui.QPushButton(self.centralwidget)
        self.exchange_button.setGeometry(QtCore.QRect(400, 400, 150, 100))
        # self.exchange_button.setText(u"兌幣")
        self.exchange_button.setFlat(True)
        self.exchange_button.setFont(font)
        self.exchange_button.setStyleSheet(
            "background-image:url(./UI/exchange.png);")

        # 儲值按鈕
        self.gift_button = QtGui.QPushButton(self.centralwidget)
        self.gift_button.setGeometry(QtCore.QRect(400, 510, 150, 100))
        # self.gift_button.setText(u"儲值")
        self.gift_button.setFont(font)
        self.gift_button.setStyleSheet("background-image:url(./UI/gift.png);")

        # 取消按鈕
        self.cancel_button = QtGui.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(400, 620, 150, 100))
        # self.cancel_button.setText(u"取消")
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet(
            "background-image:url(./UI/cancel.png);")

        # 投入金額文字
        self.label_1 = QtGui.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(50, 400, 200, 80))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_1.setText(u"投入金額")
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(
            "background-image:url(./UI/input_money.png);")

        # 顯示投入金額
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 480, 200, 80))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setText(u"0")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image:url(./UI/number.png);")

        # 兌出枚數文字
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 560, 200, 80))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_3.setText(u"兌出枚數")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(
            "background-image:url(./UI/output_coin.png);")

        # 顯示兌出枚數
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 640, 200, 80))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setText(u"0")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-image:url(./UI/number.png);")

        # 訊息列
        self.message = QtGui.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(0, 724, 600, 60))
        self.message.setText(u"加入會員,請至Play商店下載'雲寶數位服務'")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setStyleSheet("font-size: 30px;\n"
                                   "font-family: KaiTi;\n"
                                   "background-image:url(./UI/info.png);")

        self.message1 = QtGui.QLabel(self.centralwidget)
        self.message1.setGeometry(QtCore.QRect(0, 338, 600, 60))
        self.message1.setAlignment(QtCore.Qt.AlignCenter)
        self.message1.setStyleSheet("font-size: 38px;\n"
                                    "font-family: KaiTi;\n"
                                    "background: transparent;")

        # 對話框
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setFamily("KaiTi")

        self.portrait_1 = QtGui.QLabel(self.centralwidget)
        self.portrait_1.setGeometry(QtCore.QRect(0, 784, 60, 60))
        self.portrait_1.setWordWrap(True)
        # self.portrait_1.setStyleSheet("background: #FFCCCC;")

        self.portrait_2 = QtGui.QLabel(self.centralwidget)
        self.portrait_2.setGeometry(QtCore.QRect(0, 844, 60, 60))
        self.portrait_2.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        # self.portrait_2.setStyleSheet("background: #FFCCCC;")

        self.portrait_3 = QtGui.QLabel(self.centralwidget)
        self.portrait_3.setGeometry(QtCore.QRect(0, 904, 60, 60))
        self.portrait_3.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        # self.portrait_3.setStyleSheet("background: #FFCCCC;")

        self.portrait_4 = QtGui.QLabel(self.centralwidget)
        self.portrait_4.setGeometry(QtCore.QRect(0, 964, 60, 60))
        self.portrait_4.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)
        # self.portrait_4.setStyleSheet("background: #FFCCCC;")

        self.linebg_1 = QtGui.QLabel(self.centralwidget)
        self.linebg_1.setGeometry(QtCore.QRect(60, 784, 540, 60))

        self.linebg_2 = QtGui.QLabel(self.centralwidget)
        self.linebg_2.setGeometry(QtCore.QRect(60, 844, 540, 60))

        self.linebg_3 = QtGui.QLabel(self.centralwidget)
        self.linebg_3.setGeometry(QtCore.QRect(60, 904, 540, 60))

        self.linebg_4 = QtGui.QLabel(self.centralwidget)
        self.linebg_4.setGeometry(QtCore.QRect(60, 964, 540, 60))

        self.line_1 = QtGui.QLabel(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(80, 784, 520, 60))
        self.line_1.setWordWrap(True)
        self.line_1.setAlignment(QtCore.Qt.AlignTop)
        self.line_1.setFont(font)

        self.line_2 = QtGui.QLabel(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(80, 844, 520, 60))
        self.line_2.setWordWrap(True)
        self.line_2.setAlignment(QtCore.Qt.AlignTop)
        self.line_2.setFont(font)

        self.line_3 = QtGui.QLabel(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(80, 904, 520, 60))
        self.line_3.setWordWrap(True)
        self.line_3.setAlignment(QtCore.Qt.AlignTop)
        self.line_3.setFont(font)

        self.line_4 = QtGui.QLabel(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(80, 964, 520, 60))
        self.line_4.setWordWrap(True)
        self.line_4.setAlignment(QtCore.Qt.AlignTop)
        self.line_4.setFont(font)
