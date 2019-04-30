import requests
import itchat
import random

KEY = 'b34540fa0c6349bc988f2ea2e1d50fb1'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots = ['【WK】']
    reply = get_response(msg['Text']) + random.choice(robots)
    return reply or defaultReply


itchat.auto_login(hotReload=True)
itchat.run()