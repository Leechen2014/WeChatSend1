# -*-coding:UTF-*-
import time
import itchat


# {u'AppInfo': {u'Type': 0, u'AppID': u''}, u'ImgWidth': 0, u'FromUserName': u'@3242d8ae500aca33956f502c4a2026977b22455e09cd9cf90ec3ce2fb1946261', u'PlayLength': 0, u'ImgStatus': 1, u'RecommendInfo': {u'UserName': u'', u'Province': u'', u'City': u'', u'Scene': 0, u'QQNum': 0, u'Content': u'', u'Alias': u'', u'OpCode': 0, u'Signature': u'', u'Ticket': u'', u'Sex': 0, u'NickName': u'', u'AttrStatus': 0, u'VerifyFlag': 0}, u'Content': u"&lt;msg&gt;<br/>&lt;op id='4'&gt;<br/>&lt;username&gt;filehelper,wxid_0w9hdaeow06w21,2522583537@chatroom,newsapp,wxid_58jz348qthxu22,1767966412@chatroom,1827854093@chatroom,1359843466@chatroom,gh_30c4673243e2,gh_195c941a4de3,gh_ccb2e04cc75c,gh_a9506d05eeba,officialaccounts,weixin&lt;/username&gt;<br/>&lt;unreadchatlist&gt;<br/>&lt;/unreadchatlist&gt;<br/>&lt;unreadfunctionlist&gt;<br/>&lt;/unreadfunctionlist&gt;<br/>&lt;/op&gt;<br/>&lt;/msg&gt;", u'MsgType': 51, u'ImgHeight': 0, u'StatusNotifyUserName': u'filehelper,@f99ed0134611c5da260b178db72473ed0de2abef54f6bd7701b0cf3075a6afce,@@91725f3540c33f3dd9b2ce623b35843ede8d485ff12e19c561195328ef027bfa,newsapp,@3242d8ae500aca33956f502c4a2026977b22455e09cd9cf90ec3ce2fb1946261,@@b17579a310a1c755b4fd90a798835551bdb3a83322b77dcbe2ab5fdb64682d1a,@@bc72e0fea74dc5b1688420928b40d8e137f90bfde62862bdd7cad7f1805a97e0,@@ef9eeed300b3e589aef18d0955be084bba15e0c0981d48f3b664c487157f735c,@c7be0c1d5bcb5a4e42acb847d18fc1d8,@d34adb9709232fcd963a72339464891a,@cb351101522301ed72df579ad5306bf3,@4aa0cd5d652b389d2ac02eaaa92efb30,officialaccounts,weixin', u'StatusNotifyCode': 4, 'Type': 'Init', u'NewMsgId': 7519521467892350346, u'Status': 3, u'VoiceLength': 0, u'MediaId': u'', u'MsgId': u'7519521467892350346', u'ToUserName': u'@3242d8ae500aca33956f502c4a2026977b22455e09cd9cf90ec3ce2fb1946261', u'ForwardFlag': 0, u'FileName': u'', u'Url': u'', u'HasProductId': 0, u'FileSize': u'', u'AppMsgType': 0, 'Text': u'@3242d8ae500aca33956f502c4a2026977b22455e09cd9cf90ec3ce2fb1946261', u'Ticket': u'', u'CreateTime': 1469066119, u'SubMsgType': 0}
#
# step1 : msg uI received: 乡

def simple_reply():
    @itchat.msg_register
    def simple_reply(msg):
        if msg.get('Type', '') == 'Text':
            return 'I received: %s' % msg.get('Content', '')


def complex_reply():
    @itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
    def text_reply(msg):
        print "msg[\'FromUserName\']" + msg['FromUserName']
        itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

    @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
    def download_files(msg):
        fileDir = '%s%s' % (msg['Type'], int(time.time()))
        msg['Text'](fileDir)
        itchat.send('%s received' % msg['Type'], msg['FromUserName'])
        itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])

    @itchat.msg_register('Friends')
    def add_friend(msg):
        itchat.add_friend(**msg['Text'])
        itchat.get_contract()
        itchat.send('Nice to meet you!', msg['RecommendInfo']['UserName'])

    @itchat.msg_register('Text', isGroupChat=True)
    def text_reply(msg):
        print "msg[\'FromUserName\']" + msg['FromUserName']
        if msg['isAt']:
            itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

    itchat.run()


if __name__ == '__main__':

    # itchat.auto_login()
    # print itchat.get_contractTest()
    # itchat.get_contract()
    # chartRooms=itchat.get_chatrooms(update=True)
    # print chartRooms
    # simple_reply()

    dict1={}
    dict1[0] =itchat.client()
    dict1[0].auto_login()
    contract = dict1[0].get_contract()
    print "===============0=========="
    print contract


    for i in xrange(7):
        UserName = contract[i]['UserName']
        print UserName
        dict1[0].send_msg(msg="Test.....", toUserName=UserName)

    # dict1[1] = itchat.client()
    # dict1[1].auto_login()
    # contract = dict1[1].get_contract()
    # print "============1==========="
    # print contract
    #
    #
    # # for i in xrange(len(memList)):
    # #     UserName = memList[i]['UserName']
    # #     print UserName
    # #     dict1[1].send_msg(msg="Test.....", toUserName=UserName)
    #
    # # for i in xrange(len(memList)):
    # #     UserName = memList[i]['UserName']
    # #     print UserName
    # #     dict1[0].send_msg(msg="Test.....", toUserName=UserName)
    # memList0=dict1[0].get_contract(True)
    # print "=============0==============="
    # print memList0
