# -*-coding:UTF-8-*-
import StringIO
from flask import Flask
from flask import make_response
from flask import render_template
from flask import url_for
from flask import request
from flask.ext.cors import CORS


from functools import wraps

import json

from requests import Response

import Wechats

import sys

import itchat
from flask import send_file
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
CORS(app)


###
def allow_coress_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_heads = 'Referer,Accept,Origin,User-Agent'
        rst.headers['Access-Control-Allow-Headers'] = allow_heads
        return rst

    return wrapper_fun


@app.route('/')
def hello_world():
    if request.method == 'GET':
        uuid = request.args.get('uuid')  # ?uuid=XXX
        print uuid

    return render_template('index.html')


## getUuid
@app.route('/getuuid')
@allow_coress_domain
def getuuid():

    uuid = Wechats.getUUID()
    data = {'uuid': str(uuid)}
    uuidJson = json.dumps(data)
    return str(uuidJson)


## getQR
@app.route('/getQR', methods=['POST', 'GET'])
@allow_coress_domain
def getQR():
    if request.method == 'GET':
        uuid = request.args.get('uuid')  # ?uuid=XXX
    elif request.method == 'POST':
        uuid = request.form['uuid']
    print 'get uuid :' + uuid
    f = Wechats.getQR(uuid)


    return send_file(f, mimetype='image/jpeg')
    # return render_template('getQR.html', name=str(uuid + '.jpg'))

##get Json Contacet
@app.route('/getContract', methods=['POST', 'GET'])
@allow_coress_domain
def getContract():
    if request.method == 'GET':
        uuid = request.args.get('uuid')
        print 'get UUID: ' + uuid
        myContract = Wechats.Login(uuid)
        Wechats.runItChat()
        # for i in xrange(len(myContract)):
        #     itchat.send('This is a test message,to see if I could send message in Chinese.这是一条测试信息,试一下我是否可以发送中文短信.',
        #                        toUserName=myContract[i]['UserName'])
        # chatRooms = itchat.get_chatrooms(True)
        # for i in xrange(len(chatRooms)):
        #     isSucc=itchat.send(msg='This is a test message,to see if I could send message in Chinese.这是一条测试信息,试一下我是否可以发送中文短信.',
        #                        toUserName=chatRooms[i]['UserName'])
        print "Logcat::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
        print myContract
        return str(myContract)
    return 'error'


@app.route('/sendMessage', methods=['GET', 'POST'])
@allow_coress_domain
def sendMessage():
    if request.method == 'GET':
        userName = request.args.get('userName')
        content = request.args.get('content')
    elif request.method == 'POST':
        userName = request.form['userName']
        content = request.form['content']
    r = itchat.send(content,userName)
    return r

if __name__ == '__main__':
    app.run(host='192.168.127.32', port=8000)
