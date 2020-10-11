import socket  
import time
from utils import *
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot = ChatBot('Ron Obvious')
# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.chinese")





if __name__ == '__main__':

    s = socket.socket()   
    with open('config.json','r') as f:
        jdata = json.load(f)      
    host = jdata['host'] 
    b = BOT(jdata)  
    port = jdata['my_port']
    s.bind((host, port))        
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
        try:
            jresp = json.loads(data_get[0])
        except:
            c.close()
            continue
        #print(jresp)
        #c.send(postdata)
        print(jresp)
        b.process(jresp)

        c.close()               
