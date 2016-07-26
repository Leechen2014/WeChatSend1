#-*-coding:UTF-8-*-
import itchat
import time
import sys
import thread
import json

def LogCat(msg,tag=None):
    if tag is None:
        tag='[INFO]:'
    print('\(tag) %s',msg)
#web interface 1.0
def getUUID():
    uuid = itchat.get_QRuuid()
    for count in xrange(10):
        if uuid is None:
            LogCat("UUID is none,try again....", tag="INFO:")
            uuid = itchat.get_QRuuid()
        else:
            break
    return uuid

#web interface 1.1
def getQR(uuid):
    LogCat("get UUID")
    f = itchat.get_QRTest2(uuid)
    LogCat("scan QR...")
    return f

# web interface 1.3
def Login(uuid):
    waitForConfirm = False
    while True:
        status = itchat.check_login(uuid)
        if status=='200':
            break
        elif status=='201':
            if waitForConfirm:
                LogCat("Plase press confrim ....")
                waitForConfirm=True
        elif status == '408':
            LogCat("Reloading QR code....")
            uuid = getUUID()
            print uuid
            getQR(uuid)
            waitForConfirm = False
    itchat.web_init()
    itchat.show_mobile_login()
    #i
    con = itchat.get_contractTest()

    itchat.start_receiving()#key
    return con
###1.4
def runItChat():
    thread.start_new_thread(itchat.run, ())
##2.0
def sendMsg(message,fromUserName,userName):
    isSucc = itchat.send_msgTest(msg=message,fromUserName=fromUserName,toUserName=userName)
    return isSucc
#
# #
# #
# uuid = getUUID()
# #
# uuid2=getQR(uuid)
# con = Login(uuid=uuid2)
# print con
# contract=itchat.get_contract()
#
# # print "print---------info---------"
# # print contract
# # # 使用另一线程，但注意不要让程序运行终止
# #
# # # itchat.run()
# for i in xrange(len(contract)):
# # isSucc=itchat.send(msg='Text Message',contract[1]['UserName'])
#     isSucc=itchat.send_msg(msg="This is a test message,to see if I could send message in Chinese.这是一条测试信息,试一下我是否可以发送中文短信.", toUserName = contract[i]['UserName'])
#
#     print isSucc
# #
# # # chatRooms = itchat.get_chatrooms(True)
# # # for i in xrange(len(chatRooms)):
# # #     isSucc=itchat.send(msg='This is a test message,to see if I could send message in Chinese.这是一条测试信息,试一下我是否可以发送中文短信.',
# # #                        toUserName=chatRooms[i]['UserName'])
# # #     print isSucc
# #
# #
# #
