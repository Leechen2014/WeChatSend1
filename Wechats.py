# -*-coding:UTF-8-*-
import itchat

import thread


def LogCat(msg, tag=None):
    if tag is None:
        tag = '[INFO]:'
    print('\(tag) %s', msg)

dictClient = {}

# web interface 1.0
def getUUID():
    it = itchat.client()
    uuid = it.get_QRuuid()
    dictClient[uuid] = it
    for count in xrange(10):
        if uuid is None:
            LogCat("UUID is none,try again....", tag="INFO:")
            uuid = it.get_QRuuid()
        else:
            break
    return uuid


# web interface 1.1
def getQR(uuid):
    LogCat("get UUID")
    it = dictClient[uuid]
    f = it.get_QRTest2(uuid)
    LogCat("scan QR...")

    return f


# web interface 1.3
def Login(uuid):
    print uuid
    it = dictClient[uuid]
    waitForConfirm = False
    while True:
        status = it.check_login(uuid)
        if status == '200':
            break
        elif status == '201':
            if waitForConfirm:
                LogCat("Plase press confrim ....")
                waitForConfirm = True
        elif status == '408':
            LogCat("Reloading QR code....")
            # uuid = getUUID()
            print uuid
            # getQR(uuid)
            waitForConfirm = False
    it.web_init()
    it.show_mobile_login()
    # i
    con = it.get_contractTest()

    it.start_receiving()  # key
    return con


###1.4
def runItChat():
    thread.start_new_thread(itchat.run, ())


##2.0
def sendMsg(id, message, userName):
    it = dictClient[id]
    isSucc = it.send_msgTest(msg=message, toUserName=userName)
    return isSucc

def sendImg(id,img,userName):
    it = dictClient[id]
    isSucc = it.send_image(img,userName)
    return  isSucc

def sendFile(id,file,userName):
    it = dictClient[id]
    isSucc = it.send_soundTest(file, userName)
    return isSucc

# #
uuid = getUUID()
path=getQR(uuid)
con = Login(uuid)
contract=dictClient[uuid].get_contract()

# for i in xrange(len(contract)):
#     isSucc = sendMsg(id=uuid,message="This is a test message,to see if I could send message in Chinese.这是一条测试信息,试一下我是否可以发送中文短信.", userName = contract[i]['UserName'])
#     print isSucc
#
# for i in xrange(len(contract)):
#     isSucc = sendImg(id=uuid,img="/home/master/PycharmProjects/WeChatSend/img/test.gif", userName = contract[i]['UserName'])
#     print isSucc

for i in xrange(len(contract)):
    isSucc = sendFile(id=uuid,file="/home/master/PycharmProjects/WeChatSend/vido/19001.wav", userName = contract[i]['UserName'])
    print isSucc
#
#
# print dictClient
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
