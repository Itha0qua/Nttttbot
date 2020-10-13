import socket
import threading
import socketserver
import time
from utils import *
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot = ChatBot('Ron Obvious')
# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.chinese")



class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('get message')
        data_rec = self.request.recv(1024)
        if data_rec == b'':
            return
        data_get = re.findall(r'{.+}',data_rec.decode('utf-8'))    
        try:
            jresp = json.loads(data_get[0])
            print(jresp)
        except:
            return
        b.process(jresp)
        cur_thread = threading.current_thread()
        response = "{}: {}".encode()
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    with open('config.json','r') as f:
        jdata = json.load(f)      
    b = BOT(jdata)  
    HOST = jdata['host'] 
    PORT = jdata['my_port']

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print ("Server loop running in thread:" + server_thread.name)

    server.serve_forever()
    #server.shutdown()


'''
if __name__ == '__main__':

    s = socket.socket()   
    with open('config.json','r') as f:
        jdata = json.load(f)      
    b = BOT(jdata)  
    host = jdata['host'] 
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
'''