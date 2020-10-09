import re
import json

a='''POST / HTTP/1.1
Host: 0.0.0.0:7469
User-Agent: CQHttp/4.15.0
Content-Length: 368
Content-Type: application/json
X-Self-Id: 2361844282
X-Signature: sha1=888ad8a1fbe19e156516107b8246026fd6fcdb80
Accept-Encoding: gzip

{"anonymous":null,"font":0,"group_id":587215489,"message":"111","message_id":-681335642,"message_type":"group","post_type":"message","raw_message":"111","self_id":2361844282,"sender":{"age":0,"area":"","card":"","level":"","nickname":"Noitanivid","role":"owner","sex":"unknown","title":"","user_id":752865034},"sub_type":"normal","time":1601885075,"user_id":752865034}
'''
b=re.findall(r'{.+}',a)
for bb in b:
    #print(bb)
    r=json.loads(bb)
    print(r)
    if '1' in r['message']:
        print(1)

#print('a=')
#print(a)
#print('b=')
#print(b)
