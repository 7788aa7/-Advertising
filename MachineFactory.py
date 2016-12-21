#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import time
import io


class MachineFactory(object):
    """docstring for MachineFactory"""

    def __init__(self):
        super(MachineFactory, self).__init__()

    def executeSql(self, sql):
        conn = sqlite3.connect("Gift_Machine.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def loadData(self):
        conn = sqlite3.connect("Gift_Machine.db")
        cursor = conn.cursor()
        cursor.execute("SELECT machine_quantity FROM machine_setting")
        preset_quantity = cursor.fetchone()
        preset_quantity = preset_quantity[0]
        return preset_quantity
        conn.close()

    def loadAll(self):
        conn = sqlite3.connect("Gift_Machine.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM machine_setting")
        data = cursor.fetchone()
        return data
        conn.close()

    def insert(self, machine_number, banknote, coin, coin_out):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = 'INSERT INTO exchange (machine_number,banknote,coin,coin_out,time) VALUES ('
        sql += "'" + machine_number + "',"
        sql += "'" + str(banknote) + "',"
        sql += "'" + str(coin) + "',"
        sql += "'" + str(coin_out) + "',"
        sql += "'" + time_now + "')"
        self.executeSql(sql)

    def update(self, preset_quantity):
        sql = "UPDATE machine_setting set machine_quantity = " + \
            str(preset_quantity) + " where machine_number='CM_0000001'"
        self.executeSql(sql)

    def updateAll(self, exchange_preset):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = "UPDATE machine_setting set "
        sql += "machine_name = '" + exchange_preset[2] + "',"
        sql += "machine_place = '" + exchange_preset[3] + "',"
        sql += "machine_quantity = " + str(exchange_preset[4]) + ","
        sql += "machine_banknote = " + str(exchange_preset[5]) + ","
        sql += "machine_coin = " + str(exchange_preset[6]) + ","
        sql += "machine_first_motor = " + str(exchange_preset[7]) + ","
        sql += "machine_second_motor = " + str(exchange_preset[8]) + ","
        sql += "machine_online = " + str(exchange_preset[9]) + ","
        sql += "machine_import = '" + exchange_preset[10] + "',"
        sql += "machine_update_time = '" + str(time_now) + "'"
        sql += " where machine_number = '" + str(exchange_preset[0]) + "'"
        self.executeSql(sql)

    def malfunction(self, not_out, coin_out):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = 'INSERT INTO machine_malfunction (not_out,coin_out,status,time) VALUES ('
        sql += "'" + str(not_out) + "',"
        sql += "'" + str(coin_out) + "',"
        sql += "'" + str(1) + "',"
        sql += "'" + time_now + "')"
        self.executeSql(sql)

    def malfunction_check(self):
        conn = sqlite3.connect("Gift_Machine.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id,not_out,coin_out FROM machine_malfunction where status == 1")
        data = cursor.fetchone()
        return data
        conn.close()

    def malfunction_update(self, id1):
        sql = "UPDATE machine_malfunction set status = 0 where id == " + str(id1)
        self.executeSql(sql)


class Reply(object):
    """docstring for Reply"""

    def __init__(self):
        super(Reply, self).__init__()
        self.message_list = []
        f = io.open('reply.txt', 'r', encoding='UTF-8')
        while True:
            i = f.readline()
            if i == '':
                break
            else:
                self.message_list.append(i)
        f.close()

    def ReplyText(self):
        return self.message_list

    def Writetext(self, reply_list):
        f = io.open('reply.txt', 'w', encoding='UTF-8')
        for x in reply_list:
            f.write(x + '\n')
        f.close()


class Login(object):
    """docstring for Login"""

    def __init__(self):
        super(Login, self).__init__()

    def loadData(self):
        conn = sqlite3.connect("Gift_Machine.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM member")
        data = cursor.fetchone()
        return data
        conn.close()
