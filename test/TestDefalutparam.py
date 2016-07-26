import time
import json
def send_msgTest(msg='Test Message', toUserName=None):

    payloads = {
        'BaseRequest': "eww",
        'Msg': {
            'Type': 1,
            'Content': msg.encode('utf8') if isinstance(msg, unicode) else msg,
            'FromUserName': "me",
            'ToUserName': (toUserName if toUserName else "Test"),
            'LocalID': int(time.time()),
            'ClientMsgId': int(time.time()),
        }
    }
    return payloads

def send_msgTest( msg='Test Message', fromUserName=None, toUserName=None):

    if fromUserName is None:
        fromUserName = 'utf8'
    payloads = {
        'BaseRequest': 'BaseRequest',
        'Msg': {
            'Type': 1,
            'Content': msg.encode('utf8') if isinstance(msg, unicode) else msg,
            'FromUserName': fromUserName,
            'ToUserName': (toUserName if toUserName else "276").encode('utf8'),
            'LocalID': int(time.time()),
            'ClientMsgId': int(time.time()),
        },
    }
    return payloads



jsopn2 =send_msgTest(msg="232", fromUserName="QQQQQQQQQQQQQQQQQQQQQQ", toUserName="123")

print jsopn2
