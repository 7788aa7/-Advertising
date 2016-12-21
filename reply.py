# -*- coding: utf-8 -*-
import io
message_list = []


def load():
    f = io.open('reply.txt', 'r', encoding='UTF-8')
    while True:
        i = f.readline()
        # i = i.decode('utf8')
        if i == '':
            break
        else:
            message_list.append(i)
    f.close()


def ReplyText():
    return message_list


def r1():
    return message_list[0]


def r21():
    return message_list[1]


def r22():
    return message_list[2]


def r3():
    return message_list[3]


def r4():
    return message_list[4]


def r51():
    return message_list[5]


def r52():
    return message_list[6]
