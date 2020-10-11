import re
import json
from random import choice
class QA:
    def __init__(self,default_answer=['?']):
        with open('qa.json','r') as f:
            try:
                self.qa = json.load(f)
            except:
                print('read error')
                qa = {}

        self.data = re.compile(r'问[:|：](.+)答[:|：](.+)')
        self.dele = re.compile(r'删除问答[:|：](.+)')
        self.default_answer = default_answer

    def qna(self,a):
        if self.dele.match(a):
            dele_select = self.dele.findall(a)
            #print(dele_select)
            if(dele_select[0] in self.qa):
                del self.qa[dele_select[0]]
                result = '好 爷已经忘了'
            else:
                result = '你教过这句？'
            
        elif self.data.match(a):
            data_select = self.data.findall(a)
            self.qa[data_select[0][0]] = data_select[0][1]
            result = '我会了'
        elif a in self.qa:
            result = self.qa[a]
        else:
            result = choice(self.default_answer)
        with open('qa.json','w') as f:
            json.dump(self.qa,f)
        return result

if __name__ == '__main__':
    test = QA()
    while(True):
        a = input()
        print(test.qna(a))
