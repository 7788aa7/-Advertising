# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt

broker = "192.168.0.129"  # IP 106.104.5.195
client_id = "python_server"  # 機台號碼
clean_session = True
userdata = None
protocol = "MQTTv311"
transport = "tcp"
topic_pub = 'ABC'     # 要送出的版 ABC
topic_sub = 'ABC'     # 要訂閱的版 ABC


def on_connect(client, userdata, rc):
    print('\n' + "Connected with result code " + str(rc))
    client.subscribe(topic_sub)


def on_message(client, userdata, msg):
    string = str(msg.payload)
    try:
        text = string.split(',')
        if text[1][0] == '$':
            client.publish(topic_pub, '#{0}'.format(str(123)))
        else:
            pass
    except Exception as e:
        pass
    finally:
        if string == '%123':
            client.publish(topic_pub, 'success')
        else:
            pass


client = mqtt.Client(
    client_id, clean_session, userdata, protocol, transport)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)  # 連接

client.loop_forever()
