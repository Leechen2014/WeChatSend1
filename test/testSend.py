# -*-coding:UTF-8-*-
import time

import itchat
import thread


# web interface 1.0
def LogCat(msg, tag=None):
    if tag is None:
        tag = '[INFO]:'
    print('\(tag) %s', msg)


# web interface 1.1
def getQR(uuid, client):
    LogCat("get UUID")
    client.get_QRTest(uuid)
    LogCat("scan QR...")


def getUUID(client):
    uuid = client.get_QRuuid()
    for count in xrange(10):
        if uuid is None:
            LogCat("UUID is none,try again....", tag="INFO:")
            uuid = itchat.get_QRuuid()
        else:
            break
    return uuid


# web interface 1.3
def Login(uuid, client):
    waitForConfirm = False
    while True:
        status = client.check_login(uuid)
        if status == '200':
            break
        elif status == '201':
            if waitForConfirm:
                LogCat("Plase press confrim ....")
                waitForConfirm = True
        elif status == '408':
            LogCat("Reloading QR code....")
            uuid = getUUID(client)
            print uuid
            getQR(uuid, client)
            waitForConfirm = False
    client.web_init()
    client.show_mobile_login()
    # i
    con = client.get_contractTest()

    client.start_receiving()  # key
    return con


###1.4
def runItChat(client):
    thread.start_new_thread(client.run, ())


##2.0
def sendMsg(client, message, fromUserName, userName):
    isSucc = client.send_msgTest(msg=message, fromUserName=fromUserName, toUserName=userName)
    return isSucc


#
# #
# it = itchat.client()
#
# uuid = getUUID(it)
# #
# uuid2 = getQR(uuid, it)
# con = Login(uuid2,it)
# print con
# contract = it.get_contract()
#
# # print "print---------info---------"
# # print contract
# # # 使用另一线程，但注意不要让程序运行终止
# #
# # # itchat.run()
# for i in xrange(len(contract)):
#     # isSucc=itchat.send(msg='Text Message',contract[1]['UserName'])
#     isSucc = it.send_msg(
#         msg="This is a test message,to see if I could send message in Chinese.这是一条测试信息,试一下我是否可以发送中文短信.",
#         toUserName=contract[i]['UserName'])
#     print isSucc
#
# # chatRooms = itchat.get_chatrooms(True)
# # for i in xrange(len(chatRooms)):
# #     isSucc=itchat.send(msg='This is a test message,to see if I could send message in Chinese.这是一条测试信息,试一下我是否可以发送中文短信.',
# #                        toUserName=chatRooms[i]['UserName'])
# #     print isSucc
#
#
#
