import socket  
import time
import random
from random import choice
from utils import *
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
    



#chatbot = ChatBot('Ron Obvious')
# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.chinese")

meme = ['爷吐了','nmsl','就这？','我服了','nmd,wsm','?','smjb']

s = socket.socket()         
host = "0.0.0.0" # ·Ö,0;:

Manager_id = [1812754005 , 752865034]



if __name__ == '__main__':

    b = BOT('2361844282')  
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
        b.process(jresp)

        c.close()               
