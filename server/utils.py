import urllib
import re
import urllib.request
import urllib.parse
import json
from eval_compute import *
import setu
import jiki
import socket  
import time
import random
from random import choice


class BOT:
    def __init__(self,bot_qq):
        self.CQ_at = '[CQ:at,qq='+bot_qq+']'
        self.answer = ['爷吐了','nmsl','就这？','我服了','nmd,wsm','?','smjb']
        self.tar_url = "http://0.0.0.0:5700"

    def process(self , jresp):
        if  '图来' in jresp['message']:
            search_str = jresp['message'].replace('图来','')
            se_u = setu.get_setu(False , search_str , 1, False)
            if se_u == []:
                self.send_group_msg('找不到',jresp['group_id'])
            else:    
                se_url = se_u[0].url
                self.send_group_msg('[CQ:image,file='+se_url+']',jresp['group_id'])
    

        elif '是什么' in jresp['message'] and self.CQ_at in jresp['message']:
            stri = jresp['message'].replace(self.CQ_at,'').replace('是什么','')
            #response=chatbot.get_response(stri)
            #response='?'
            response = jiki.get_jikiresult(stri)
            print(response)
            self.send_group_msg('[CQ:reply,id='+str(jresp['message_id'])+']'+str(response),jresp['group_id'])

        elif '是不是' in jresp['message'] or '感觉' in jresp['message'] or '觉得' in jresp['message']:
            self.send_group_msg("确实",jresp['group_id'])

        elif '不会' in jresp['message'] and '吧' in jresp['message']:
            self.send_group_msg("不会吧不会吧",jresp['group_id'])
    
        elif self.CQ_at+'计算' in jresp['message'] or self.CQ_at+' 计算' in jresp['message']:
            stri = jresp['message'].replace(self.CQ_at,'').replace('计算','')
            #print(stri)
            #send_group_msg(stri,jresp['group_id'])
            try:
                result = eval_com(stri)
            except:
                self.send_group_msg("不会",jresp['group_id'])
            else:
                self.send_group_msg(result,jresp['group_id'])
                print(result) 
        
        #elif ('[CQ:at,qq=2361844282]重启' in jresp['message'] or '[CQ:at,qq=2361844282] 重启' in jresp['message']) and jresp['user_id'] in Manager_id:
            #restart(2000)
            #print(restart)

        elif self.CQ_at in jresp['message']:
            stri = jresp['message'].replace(self.CQ_at,'')
            #response=chatbot.get_response(stri)
            #response='?'
            response = choice(self.answer)
            print(response)
            self.send_group_msg('[CQ:reply,id='+str(jresp['message_id'])+']'+str(response),jresp['group_id'])

    def send_group_msg(self,str,gid):
        req = urllib.request.Request(self.tar_url + "/send_group_msg",urllib.parse.urlencode({"group_id": gid, "message": str}).encode('utf8'))
        rep = urllib.request.urlopen(req).read()
        print(rep)

    def send_private_msg(self,str,uid):
        req = urllib.request.Request(self.tar_url + "/send_private_msg",urllib.parse.urlencode({"user_id": uid, "message": str}).encode('utf8'))
        rep = urllib.request.urlopen(req).read()
        print(rep)


    def restart(self,d):
        req = urllib.request.Request(self.tar_url + "/set_restart_plugin",urllib.parse.urlencode({"delay": d}).encode('utf8'))
        rep = urllib.request.urlopen(req).read()
        print(rep)