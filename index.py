from bs4 import BeautifulSoup
import requests
import time, yaml
import os, logging, sys

def bet(str, tag1, tag2):
    index1 = 0
    if str.find(tag1, 0, len(str)) != -1:
        index1 = str.find(tag1, 0, len(str)) + len(tag1)
    index2 = index1
    if str.find(tag2, index1, len(str)) != -1:
        index2 = str.find(tag2, index1, len(str))
    return str[index1:index2]


def work():
    """check if it's online or not and automatically sign in.

    """
    global username, password, logger
    session = requests.Session()
    page = session.get("http://detectportal.firefox.com/success.txt")

    if (page.content.decode().strip() == 'success'):
        logger.info("connected, skip")
        return
    logger.info("unconnected, try to reconnect")
    url = 'http://enet.10000.gd.cn:10001/sz/sz112/' + bet(page.content, b"window.location = \'", b"\';").decode()

    html = session.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    form = soup.find('form', id='fm1')

    hidden = form.find_all('input', type='hidden')
    execution = hidden[0].get('value')
    params = {
        "username": username,
        "password": password,
        "_eventId": "submit",
        "geolocation": "",
        "execution": execution
    }
    res = session.post('https://cas.sustech.edu.cn/cas/login?service=' + url, data=params)
    text = res.content.decode()
    # print(text)
    if text.find("帐号状态为暂停") != -1:
        logger.info("Kr Au")
    elif text.find('成功') != -1:
        logger.info("reconnect ok")
    else:
        logger.info("failed to reconnect")

try:
    f = open('config.yaml','r',encoding='utf-8')
except IOError:
    print("Error: [config.yaml] doesn't exist!")
    exit(0)

cont = f.read()
x = yaml.load(cont)

username, password = "", ""
try:
    username, password = x["username"], x["password"]
except KeyError:
    print("Error: wrong config format. Please follow [config.yaml.example]")
    exit(0)
    
logger = logging.getLogger()    # initialize logging class
logger.setLevel(logging.INFO)  # default log level
sh = logging.StreamHandler(stream=sys.stdout)    # output to standard output
format = logging.Formatter("%(asctime)s - %(message)s")    # output format 
sh.setFormatter(format)
logger.addHandler(sh)

while (True):
    work()
    time.sleep(10)