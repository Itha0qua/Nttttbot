import socket               
import urllib
import re
import urllib.request
import urllib.parse
import json
import math
import time
import random
import setu
import jiki
from random import choice

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import signal
    

bot_qq = '2361844282'


chatbot = ChatBot('Ron Obvious')
CQ_at = '[CQ:at,qq='+bot_qq+']'
# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.chinese")

meme = ['爷吐了','nmsl','就这？','我服了','nmd,wsm','?','smjb']

s = socket.socket()         
host = "0.0.0.0" # ·Ö,0;:

Manager_id = [1812754005 , 752865034]


def signal_handler(signum , frame):
    print('Time Out')
    raise RuntimeError

def send_group_msg(str,gid):
    req = urllib.request.Request("http://0.0.0.0:5700/send_group_msg",urllib.parse.urlencode({"group_id": gid, "message": str}).encode('utf8'))
    rep = urllib.request.urlopen(req).read()
    print(rep)

def send_private_msg(str,uid):
    req = urllib.request.Request("http://0.0.0.0:5700/send_private_msg",urllib.parse.urlencode({"user_id": uid, "message": str}).encode('utf8'))
    rep = urllib.request.urlopen(req).read()
    print(rep)

def compute(mes,gid):
    stri = mes.replace(CQ_at,'').replace('计算','')
    #print(stri)
    #send_group_msg(stri,jresp['group_id'])
    try:
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(10)   # Ten seconds
        result = eval(stri)
        signal.alarm(0)
    except:
        send_group_msg("不会",gid)
    else:
        send_group_msg(result,gid)
        print(result) 

def restart(d):
    req = urllib.request.Request("http://0.0.0.0:5700/set_restart_plugin",urllib.parse.urlencode({"delay": d}).encode('utf8'))
    rep = urllib.request.urlopen(req).read()
    print(rep)

port = 7469
s.bind((host, port))        
#data={'user_id':752765034,'message':'test'}
#postdata=urllib.parse.urlencode(data).encode('utf8') 
s.listen(5)     
print("start successfully")            
while True:
    c,addr = s.accept()     
    #print(c,addr)
    data_rec = c.recv(1024)
    if data_rec == b'':
        c.close()
        continue
    data_get = re.findall(r'{.+}',data_rec.decode('utf-8'))
    
    jresp = json.loads(data_get[0])
    
    #print(jresp)
    #c.send(postdata)
    print(jresp)


    if  '图来' in jresp['message']:
        search_str = jresp['message'].replace('图来','')
        se_u = setu.get_setu(False , search_str , 1, False)
        if se_u == []:
            send_group_msg('找不到',jresp['group_id'])
        else:    
            se_url = se_u[0].url
            send_group_msg('[CQ:image,file='+se_url+']',jresp['group_id'])
    

    elif '是什么' in jresp['message'] and CQ_at in jresp['message']:
        stri = jresp['message'].replace(CQ_at,'').replace('是什么','')
        #response=chatbot.get_response(stri)
        #response='?'
        response = jiki.get_jikiresult(stri)
        print(response)
        send_group_msg('[CQ:reply,id='+str(jresp['message_id'])+']'+str(response),jresp['group_id'])

    elif '是不是' in jresp['message'] or '感觉' in jresp['message'] or '觉得' in jresp['message']:
        send_group_msg("确实",jresp['group_id'])

    elif '不会' in jresp['message'] and '吧' in jresp['message']:
        send_group_msg("不会吧不会吧",jresp['group_id'])
    
    elif CQ_at+'计算' in jresp['message'] or CQ_at+' 计算' in jresp['message']:
        compute(jresp['message'] , jresp['group_id'])
    
    #elif ('[CQ:at,qq=2361844282]重启' in jresp['message'] or '[CQ:at,qq=2361844282] 重启' in jresp['message']) and jresp['user_id'] in Manager_id:
        #restart(2000)
        #print(restart)

    elif CQ_at in jresp['message']:
        stri = jresp['message'].replace(CQ_at,'')
        #response=chatbot.get_response(stri)
        #response='?'
        response = choice(meme)
        print(response)
        send_group_msg('[CQ:reply,id='+str(jresp['message_id'])+']'+str(response),jresp['group_id'])

    c.close()               
