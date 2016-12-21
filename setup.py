#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from PySide import QtGui, QtCore
from setup_ui import StockDialog, Ui_Machine, Ui_Message, Ui_MemberManage, Ui_MasterMember
from setup_ui import Ui_SubMember, Ui_LoginDialog
from MachineFactory import MachineFactory, Reply, Login
from subprocess import Popen


class Window(QtGui.QDialog, StockDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle(u'機台設定')
        self.setupUi(self)
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.BlankCursor)  # 隱藏鼠標
        screen = QtGui.QDesktopWidget().screenGeometry()  # 讀取螢幕尺寸
        self.factory = MachineFactory()
        self.setup_list = list(self.factory.loadAll())

        self.reply = Reply()

        self.memberManage = MemberManage(screen.width() * 0.73)
        self.masterMember = MasterMember(screen.width() * 0.73)
        self.subMember = SubMember(screen.width() * 0.73)
        self.machine = Machine(screen.width() * 0.73)
        self.message = Message()

        self.machine.SetLineText(self.setup_list)
        self.message.SetLineText(self.reply.ReplyText())
        self.masterMember.SetLineText(Login().loadData())
        self.stack.addWidget(self.masterMember)
        self.stack.addWidget(self.memberManage)
        self.stack.addWidget(self.subMember)
        self.stack.addWidget(self.machine)
        self.stack.addWidget(self.message)

        self.connect(self.listWidget, QtCore.SIGNAL("currentRowChanged(int)"),
                     self.stack, QtCore.SLOT("setCurrentIndex(int)"))

        self.closePushButton.clicked.connect(self.closess)
        self.savePushButton.clicked.connect(self.onShowWarning)

    def onShowWarning(self):
        flags = QtGui.QMessageBox.StandardButton.Ok
        flags |= QtGui.QMessageBox.StandardButton.Cancel
        msg = u"確定要儲存設定?"
        response = QtGui.QMessageBox.warning(self, "Warning!",
                                             msg, flags)
        if response == QtGui.QMessageBox.Ok:
            setup_list = self.machine.save()
            reply_list = self.message.save()
            print setup_list
            self.save(setup_list, reply_list)

    def save(self, setup_list, reply_list):
        self.factory.updateAll(setup_list)
        self.reply.Writetext(reply_list)

    def closess(self):
        os.system('python main.py')
        self.close()


class MemberManage(QtGui.QWidget, Ui_MemberManage):

    def __init__(self, width, parent=None):
        super(MemberManage, self).__init__(parent)
        self.setupUi(self)
        self.widget.resize(width, 200)


class MasterMember(QtGui.QWidget, Ui_MasterMember):

    def __init__(self, width, parent=None):
        super(MasterMember, self).__init__(parent)
        self.setupUi(self)
        self.widget.resize(width, 200)

    def SetLineText(self, mamber_list):
        self.mamber_list = mamber_list
        self.txtMasterId.setText(str(mamber_list[0]))
        self.txtMasterName.setText(str(mamber_list[1]))
        self.txtMasterAccount.setText(str(mamber_list[2]))
        self.txtMasterPhone.setText(str(mamber_list[4]))


class SubMember(QtGui.QWidget, Ui_SubMember):

    def __init__(self, width, parent=None):
        super(SubMember, self).__init__(parent)
        self.setupUi(self)
        self.widget.resize(width, 350)


class Machine(QtGui.QWidget, Ui_Machine):

    def __init__(self, width, parent=None):
        super(Machine, self).__init__(parent)
        self.setupUi(self)
        self.widget.resize(width, 700)

    def SetLineText(self, setup_list):
        self.setup_list = setup_list
        self.txtId.setText(setup_list[0])
        self.txtVersion.setText(setup_list[1])
        self.txtEquipment.setText(setup_list[2])
        self.txtPlace.setText(setup_list[3])
        self.txtQuantity.setText(str(setup_list[4]))
        self.txtBanknote.setText(str(setup_list[5]))
        self.txtCoin.setText(str(setup_list[6]))
        self.Community.setText(setup_list[12])
        self.Third_Party.setText(setup_list[13])
        if setup_list[7] == 1:
            self.motor1_on.setChecked(True)
        else:
            self.motor1_off.setChecked(True)
        if setup_list[8] == 1:
            self.motor2_on.setChecked(True)
        else:
            self.motor2_off.setChecked(True)
        if setup_list[9] == 1:
            self.online_on.setChecked(True)
        else:
            self.online_off.setChecked(True)
        if setup_list[10] == u'觸控':
            self.import_on.setChecked(True)
        else:
            self.import_off.setChecked(True)
        if setup_list[11] == u'RS232':
            self.output_on.setChecked(True)
        else:
            self.output_off.setChecked(True)

    def save(self):
        self.setup_list[2] = self.txtEquipment.text()
        self.setup_list[3] = self.txtPlace.text()
        self.setup_list[4] = int(self.txtQuantity.text())
        self.setup_list[5] = int(self.txtBanknote.text())
        self.setup_list[6] = int(self.txtCoin.text())
        if self.motor1_on.isChecked():
            self.setup_list[7] = 1
        else:
            self.setup_list[7] = 0
        if self.motor2_on.isChecked():
            self.setup_list[8] = 1
        else:
            self.setup_list[8] = 0
        if self.online_on.isChecked():
            self.setup_list[9] = 1
        else:
            self.setup_list[9] = 0
        if self.import_on.isChecked():
            self.setup_list[10] = u'觸控'
        else:
            self.setup_list[10] = u'按鈕'
        if self.import_on.isChecked():
            self.setup_list[11] = u'RS232'
        else:
            self.setup_list[11] = u'Signal'
        return self.setup_list


class Message(QtGui.QWidget, Ui_Message):

    def __init__(self, parent=None):
        super(Message, self).__init__(parent)
        self.setupUi(self)

        self.Text3.textChanged.connect(
            lambda: self.textChanged(self.Text3, 55))
        self.Text4.textChanged.connect(
            lambda: self.textChanged(self.Text4, 55))
        # self.Text5.textChanged.connect(lambda: self.textChanged(self.Text5))
        self.Text6.textChanged.connect(
            lambda: self.textChanged(self.Text6, 21))

    def SetLineText(self, reply_list):
        self.reply_list = reply_list
        self.LineText1.setText(reply_list[0].strip())
        self.LineText2.setText(reply_list[1].strip())
        self.LineText7.setText(reply_list[2].strip())
        self.Text3.setText(reply_list[3].strip())
        self.Text4.setText(reply_list[4].strip())
        self.Text5.setText(reply_list[5].strip() +
                           '\n' + reply_list[6].strip())
        self.Text6.setText(reply_list[7].strip())

    def textChanged(self, object1, maxLength):
        textContent = object1.toPlainText()
        textLength = len(textContent)
        if(textLength > maxLength):
            textCursor = object1.textCursor()
            object1.setText(textContent[:maxLength])
            textCursor.setPosition(maxLength)
            object1.setTextCursor(textCursor)

    def save(self):
        text5 = self.Text5.toPlainText()
        text5 = text5.split('\n')
        self.reply_list[0] = self.LineText1.text()
        self.reply_list[1] = self.LineText2.text()
        self.reply_list[2] = self.LineText7.text()
        self.reply_list[3] = self.Text3.toPlainText()
        self.reply_list[4] = self.Text4.toPlainText()
        self.reply_list[5] = text5[0]
        self.reply_list[6] = text5[1]
        self.reply_list[7] = self.Text6.toPlainText()
        return self.reply_list


class LoginDialog(QtGui.QDialog, Ui_LoginDialog):

    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        LoginDialog.showFullScreen(self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonClose.clicked.connect(self.close)
        self.member = Login().loadData()

    def handleLogin(self):
        if (self.textName.text() == 'a' and
                self .textPass.text() == 'a'):
            self.accept()  # 關鍵
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Bad user or password')


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName(u'機台設定')
    window = Window()
    window.showFullScreen()
    if LoginDialog().exec_() == QtGui.QDialog.Accepted:
        sys.exit(app.exec_())
    else:
        window.close()
