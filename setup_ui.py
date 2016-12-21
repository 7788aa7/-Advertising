# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *


class StockDialog(object):

    def setupUi(self, StockDialog):

        self.stack = QStackedWidget()
        self.stack.setFrameStyle(QFrame.Panel | QFrame.Raised)

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)

        self.listWidget = QListWidget()
        self.listWidget.insertItem(0, u"主帳號資料")
        self.listWidget.insertItem(1, u"帳號管理")
        self.listWidget.insertItem(2, u"註冊子帳號")
        self.listWidget.insertItem(3, u"機台設定")
        self.listWidget.insertItem(4, u"內文編輯")

        self.listWidget.setFont(font)

        self.savePushButton = QPushButton(u"儲存")
        self.closePushButton = QPushButton(u"關閉")

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(self.savePushButton)
        self.buttonLayout.addWidget(self.closePushButton)

        self.stackLayout = QVBoxLayout()
        self.stackLayout.setSpacing(6)
        self.stackLayout.addWidget(self.stack)
        self.stackLayout.addLayout(self.buttonLayout)

        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.addWidget(self.listWidget)
        self.mainLayout.addLayout(self.stackLayout)
        self.mainLayout.setStretchFactor(self.listWidget, 1)
        self.mainLayout.setStretchFactor(self.stackLayout, 3)


class Ui_LoginDialog(object):

    def setupUi(self, Ui_LoginDialog):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setWeight(50)

        label1 = QLabel(u"帳號:")
        label2 = QLabel(u"密碼:")
        label3 = QLabel(self)

        label1.setFont(font)
        label2.setFont(font)

        label3.setStyleSheet("background-image:url('./UI/LoginLogo.png');")
        label3.setGeometry(QRect(0, 0, 256, 256))

        self.textName = QLineEdit()
        self.textPass = QLineEdit()
        self.textName.setFont(font)
        self.textPass.setFont(font)
        self.buttonLogin = QPushButton('Login')
        self.buttonClose = QPushButton('Close')
        self.buttonLogin.setFont(font)
        self.buttonClose.setFont(font)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.buttonLogin)
        self.buttonLayout.addWidget(self.buttonClose)
        widget = QWidget(self)
        widget.resize(300, 300)
        self.center(widget)
        layout = QGridLayout(widget)
        layout.addWidget(label1, 0, 0, 1, 1)
        layout.addWidget(self.textName, 0, 1, 1, 1)
        layout.addWidget(label2, 1, 0, 1, 1)
        layout.addWidget(self.textPass, 1, 1, 1, 1)
        layout.addLayout(self.buttonLayout, 2, 0, 1, 2)
        x = widget.x() + 150
        y = widget.y() / 2 - 128
        if y < 0:
            y = 0
        label3.move(x - 128, y)

    def center(self, widget):
        qr = widget.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        widget.move(qr.topLeft())


class Ui_MemberManage(object):

    def setupUi(self, Ui_MemberManage):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setWeight(50)

        label1 = QLabel(u"主用戶編號:")
        label2 = QLabel(u"用戶名稱:")
        label3 = QLabel(u"登入帳號:")
        label4 = QLabel(u"手機號碼:")

        label1.setFont(font)
        label2.setFont(font)
        label3.setFont(font)
        label4.setFont(font)

        self.txtMasterId = QLineEdit()
        self.txtMasterName = QLineEdit()
        self.txtMasterAccount = QLineEdit()
        self.txtMasterPhone = QLineEdit()

        self.txtMasterId.setFont(font)
        self.txtMasterName.setFont(font)
        self.txtMasterAccount.setFont(font)
        self.txtMasterPhone.setFont(font)

        self.txtMasterId.setMaxLength(10)
        self.txtMasterName.setMaxLength(10)
        self.txtMasterAccount.setMaxLength(10)
        self.txtMasterPhone.setMaxLength(10)

        self.txtMasterId.setReadOnly(True)
        self.txtMasterAccount.setReadOnly(True)

        self.widget = QWidget(self)

        layout = QGridLayout(self.widget)
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.txtMasterId, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.txtMasterName, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.txtMasterAccount, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.txtMasterPhone, 3, 1)


class Ui_MasterMember(object):

    def setupUi(self, Ui_MasterMember):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setWeight(50)

        label1 = QLabel(u"主用戶編號:")
        label2 = QLabel(u"用戶名稱:")
        label3 = QLabel(u"登入帳號:")
        label4 = QLabel(u"電話號碼:")

        label1.setFont(font)
        label2.setFont(font)
        label3.setFont(font)
        label4.setFont(font)

        self.txtMasterId = QLineEdit()
        self.txtMasterName = QLineEdit()
        self.txtMasterAccount = QLineEdit()
        self.txtMasterPhone = QLineEdit()

        self.txtMasterId.setFont(font)
        self.txtMasterName.setFont(font)
        self.txtMasterAccount.setFont(font)
        self.txtMasterPhone.setFont(font)

        self.txtMasterId.setMaxLength(10)
        self.txtMasterName.setMaxLength(20)
        self.txtMasterAccount.setMaxLength(10)
        self.txtMasterPhone.setMaxLength(10)

        self.txtMasterId.setReadOnly(True)
        self.txtMasterAccount.setReadOnly(True)

        self.widget = QWidget(self)

        layout = QGridLayout(self.widget)
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.txtMasterId, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.txtMasterName, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.txtMasterAccount, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.txtMasterPhone, 3, 1)


class Ui_SubMember(object):

    def setupUi(self, Ui_SubMember):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setWeight(50)

        label1 = QLabel(u"主用戶編號:")
        label2 = QLabel(u"用戶編號:")
        label3 = QLabel(u"用戶名稱:")
        label4 = QLabel(u"登入帳號:")
        label5 = QLabel(u"登入密碼:")
        label6 = QLabel(u"手機號碼:")
        label7 = QLabel(u"驗證碼:")

        label1.setFont(font)
        label2.setFont(font)
        label3.setFont(font)
        label4.setFont(font)
        label5.setFont(font)
        label6.setFont(font)
        label7.setFont(font)

        self.txtMasterId = QLineEdit()
        self.txtSubId = QLineEdit()
        self.txtSubName = QLineEdit()
        self.txtSubAccount = QLineEdit()
        self.txtSubPassword = QLineEdit()
        self.txtSubPhone = QLineEdit()
        self.txtCode = QLineEdit()

        self.txtMasterId.setFont(font)
        self.txtSubId.setFont(font)
        self.txtSubName.setFont(font)
        self.txtSubAccount.setFont(font)
        self.txtSubPassword.setFont(font)
        self.txtSubPhone.setFont(font)
        self.txtCode.setFont(font)

        self.txtMasterId.setMaxLength(10)
        self.txtSubId.setMaxLength(10)
        self.txtSubName.setMaxLength(10)
        self.txtSubAccount.setMaxLength(10)
        self.txtSubPassword.setMaxLength(10)
        self.txtSubPhone.setMaxLength(10)
        self.txtCode.setMaxLength(10)

        self.txtMasterId.setReadOnly(True)
        self.txtSubId.setReadOnly(True)

        self.widget = QWidget(self)

        layout = QGridLayout(self.widget)
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.txtMasterId, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.txtSubId, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.txtSubName, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.txtSubAccount, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.txtSubPassword, 4, 1)
        layout.addWidget(label6, 5, 0)
        layout.addWidget(self.txtSubPhone, 5, 1)
        layout.addWidget(label7, 6, 0)
        layout.addWidget(self.txtCode, 6, 1)


class Ui_Machine(object):

    def setupUi(self, Ui_Machine):

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setWeight(50)

        label1 = QLabel(u"機台號碼:")
        label2 = QLabel(u"固件版本:")
        label3 = QLabel(u"設備名稱:")
        label4 = QLabel(u"場地名稱:")
        label5 = QLabel(u"　　幣量:")
        label6 = QLabel(u"紙鈔比率:")
        label7 = QLabel(u"硬幣比率:")
        label8 = QLabel(u"第一馬達:")
        label9 = QLabel(u"第二馬達:")
        label10 = QLabel(u"連線設定:")
        label11 = QLabel(u"輸入設定:")
        label12 = QLabel(u"紙鈔輸入:")
        label13 = QLabel(u"　　社群:")
        self.Community = QLabel()
        label14 = QLabel(u"第三方支付:")
        self.Third_Party = QLabel()

        label1.setFont(font)
        label2.setFont(font)
        label3.setFont(font)
        label4.setFont(font)
        label5.setFont(font)
        label6.setFont(font)
        label7.setFont(font)
        label8.setFont(font)
        label9.setFont(font)
        label10.setFont(font)
        label11.setFont(font)
        label12.setFont(font)
        label13.setFont(font)
        self.Community.setFont(font)
        label14.setFont(font)
        self.Third_Party.setFont(font)

        motor1widget = QWidget()
        motor2widget = QWidget()
        onlinewidget = QWidget()
        importwidget = QWidget()
        outputwidget = QWidget()

        self.txtId = QLineEdit()
        self.txtVersion = QLineEdit()
        self.txtEquipment = QLineEdit()
        self.txtPlace = QLineEdit()
        self.txtQuantity = QLineEdit()
        self.txtBanknote = QLineEdit()
        self.txtCoin = QLineEdit()
        self.motor1_on = QRadioButton(u"啟用", motor1widget)
        self.motor1_off = QRadioButton(u"禁用", motor1widget)
        self.motor2_on = QRadioButton(u"啟用", motor2widget)
        self.motor2_off = QRadioButton(u"禁用", motor2widget)
        self.online_on = QRadioButton(u"連線", onlinewidget)
        self.online_off = QRadioButton(u"單機", onlinewidget)
        self.import_on = QRadioButton(u"觸控", importwidget)
        self.import_off = QRadioButton(u"按鍵", importwidget)
        self.output_on = QRadioButton(u"RS232", outputwidget)
        self.output_off = QRadioButton(u"Signal", outputwidget)

        self.txtId.setFont(font)
        self.txtVersion.setFont(font)
        self.txtEquipment.setFont(font)
        self.txtPlace.setFont(font)
        self.txtQuantity.setFont(font)
        self.txtBanknote.setFont(font)
        self.txtCoin.setFont(font)
        self.motor1_on.setFont(font)
        self.motor1_off.setFont(font)
        self.motor2_on.setFont(font)
        self.motor2_off.setFont(font)
        self.online_on.setFont(font)
        self.online_off.setFont(font)
        self.import_on.setFont(font)
        self.import_off.setFont(font)
        self.output_on.setFont(font)
        self.output_off.setFont(font)

        self.txtId.setMaxLength(10)
        self.txtVersion.setMaxLength(10)
        self.txtEquipment.setMaxLength(10)
        self.txtPlace.setMaxLength(10)
        self.txtQuantity.setMaxLength(10)
        self.txtBanknote.setMaxLength(10)
        self.txtCoin.setMaxLength(10)

        self.txtId.setReadOnly(True)
        self.txtVersion.setReadOnly(True)

        motor1Layout = QHBoxLayout(motor1widget)
        motor1Layout.addWidget(self.motor1_on)
        motor1Layout.addWidget(self.motor1_off)
        motor2Layout = QHBoxLayout(motor2widget)
        motor2Layout.addWidget(self.motor2_on)
        motor2Layout.addWidget(self.motor2_off)
        onlineLayout = QHBoxLayout(onlinewidget)
        onlineLayout.addWidget(self.online_on)
        onlineLayout.addWidget(self.online_off)
        importLayout = QHBoxLayout(importwidget)
        importLayout.addWidget(self.import_on)
        importLayout.addWidget(self.import_off)
        outputLayout = QHBoxLayout(outputwidget)
        outputLayout.addWidget(self.output_on)
        outputLayout.addWidget(self.output_off)

        self.widget = QWidget(self)

        layout = QGridLayout(self.widget)
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.txtId, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.txtVersion, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.txtEquipment, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.txtPlace, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.txtQuantity, 4, 1)
        layout.addWidget(label6, 5, 0)
        layout.addWidget(self.txtBanknote, 5, 1)
        layout.addWidget(label7, 6, 0)
        layout.addWidget(self.txtCoin, 6, 1)
        layout.addWidget(label8, 7, 0)
        layout.addWidget(motor1widget, 7, 1)
        layout.addWidget(label9, 8, 0)
        layout.addWidget(motor2widget, 8, 1)
        layout.addWidget(label10, 9, 0)
        layout.addWidget(onlinewidget, 9, 1)
        layout.addWidget(label11, 10, 0)
        layout.addWidget(importwidget, 10, 1)
        layout.addWidget(label12, 11, 0)
        layout.addWidget(outputwidget, 11, 1)
        layout.addWidget(label13, 12, 0)
        layout.addWidget(self.Community, 12, 1)
        layout.addWidget(label14, 13, 0)
        layout.addWidget(self.Third_Party, 13, 1)


class Ui_Message(object):

    def setupUi(self, Ui_Message):

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setWeight(50)

        label1 = QLabel(u"未投幣:")
        label2 = QLabel(u"儲值:")
        label3 = QLabel(u"完成儲值:")
        label4 = QLabel(u"取消:")
        label5 = QLabel(u"故障:")
        label6 = QLabel(u"標題:")
        label7 = QLabel(u"+序號+")

        label1.setFont(font)
        label2.setFont(font)
        label3.setFont(font)
        label4.setFont(font)
        label5.setFont(font)
        label6.setFont(font)
        label7.setFont(font)

        self.LineText1 = QLineEdit()
        self.LineText2 = QLineEdit()
        self.Text3 = QTextEdit()
        self.Text4 = QTextEdit()
        self.Text5 = QTextEdit()
        self.Text6 = QTextEdit()
        self.LineText7 = QLineEdit()

        self.LineText1.setFont(font)
        self.LineText2.setFont(font)
        self.Text3.setFont(font)
        self.Text4.setFont(font)
        self.Text5.setFont(font)
        self.Text6.setFont(font)
        self.LineText7.setFont(font)

        self.LineText1.setMaxLength(15)
        self.LineText2.setMaxLength(15)
        self.LineText7.setMaxLength(15)

        lineLayout = QVBoxLayout()
        lineLayout.addWidget(self.LineText2)
        lineLayout.addWidget(label7)
        lineLayout.addWidget(self.LineText7)

        layout = QGridLayout(self)
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.LineText1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addLayout(lineLayout, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.Text3, 2, 1)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.Text4, 3, 1)
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.Text5, 4, 1)
        layout.addWidget(label6, 5, 0)
        layout.addWidget(self.Text6, 5, 1)
