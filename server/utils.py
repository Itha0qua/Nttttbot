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
from qa import *
from poker import *
import feedparser


class BOT:
    def __init__(self , data):
        self.bot_qq = data['bot_qq']
        self.te = {}
        self.CQ_at = '[CQ:at,qq='+str(self.bot_qq)+']'
        self.answer = QA(data['answer'])
        self.tar_url = data['tar_url']
        self.rss_list = data['rss_list']
        #self.texas_num = 0

    def process(self , jresp):
        if jresp['message'] in self.rss_list:
            try:

                rss = feedparser.parse(self.rss_list[jresp['message']])
                result = ''
                for i in range(0,5):
                    result += rss.entries[i].title+'\n'+rss.entries[i].id+'\n'+rss.entries[i].published+'\n\n'
                self.send_group_msg(result,jresp['group_id'])
            except:
                print('error')


        elif jresp['message'] == '开始德州':
            try:
                gid = str(jresp['group_id'])
                if gid not in self.te:
                    self.te[gid] = texas()
                result = self.te[gid].new_game()
                self.te[gid].texas_num = 0
                self.send_group_msg(result,jresp['group_id'])
            except:
                self.send_group_msg('出现意外,请重新开始',jresp['group_id'])

        elif jresp['message'] == '给我发牌':
            #print(self.te.playerlist)
            try:
                gid = str(jresp['group_id'])
                result = self.te[gid].add_player('[CQ:at,qq='+str(jresp['user_id'])+']')
                self.send_private_msg(result,jresp['user_id'])
                self.send_group_msg('发牌成功',jresp['group_id'])
            except:
                self.send_group_msg('发牌失败',jresp['group_id'])
        
        elif jresp['message'] == '弃牌':
            #print(self.te.playerlist)
            try:
                gid = str(jresp['group_id'])
                result = self.te[gid].remove_player('[CQ:at,qq='+str(jresp['user_id'])+']')
                self.send_group_msg(result,jresp['group_id'])
            except:
                self.send_group_msg('弃牌失败',jresp['group_id'])

        elif jresp['message'] == '翻牌':
            #print(self.te.playerlist)
            try:
                gid = str(jresp['group_id'])
                if self.te[gid].texas_num == 0:
                    result = self.te[gid].show_board(0,3)
                    self.te[gid].texas_num = 1
                elif self.te[gid].texas_num == 1:
                    result = self.te[gid].show_board(0,4)
                    self.te[gid].texas_num = 2
                elif self.te[gid].texas_num == 2:
                    result = self.te[gid].show_board(0,5)
                    self.te[gid].texas_num = 3
                elif self.te[gid].texas_num == 3:
                    result = self.te[gid].end()
                    self.te[gid].texas_num = 4
                else:
                    result = '已经结束了'
                self.send_group_msg(result,jresp['group_id'])
            except:
                self.send_group_msg('出现意外,请重新开始',jresp['group_id'])

        elif  '图来' in jresp['message']:
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
            stri = jresp['message'].replace(self.CQ_at,'').replace(' ','')
            #response=chatbot.get_response(stri)
            #response='?'
            response = self.answer.qna(stri)
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