import urllib.request as req
import urllib
import re
from bs4 import BeautifulSoup

def get_jikiresult(word):
    url = 'https://jikipedia.com'
    s_url = url + '/search?phrase=' + urllib.parse.quote(word)
    try:
        a = req.urlopen(req.Request(s_url)).read().decode()
        e = re.findall('/definition/[0-9]*',a)[0]
        r_url = url + e
        a2 = req.urlopen(req.Request(r_url)).read().decode()
        soup = BeautifulSoup(a2, 'html.parser')
        res = soup.find_all(name='div',attrs={"class":"brax-render render"})[0]
       
        return soup.find_all(name='h1',attrs={"class":"title"})[0].get_text()+'\n'+res.get_text()
    except:
        return '希腊奶'