# 注册地址：http://appapi.jinzhuqianguan.com/home/index?uucode=9VT87B2700&channel=10000
#  本人邀请码：9VT87B2700
'''
cron: 01 0,6,18 * * *  python3 daily.py
new Env('金猪日记日常');
'''

import requests
import time
import os

# 查看列表
def task(Authorization,User_Agent):
    url = "http://appapi.jinzhuqianguan.com/api/Member/task"
    data = {
        "group":"1",
        "platform":"android",
        "channel":"10000"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    r = requests.post(url, data=data, headers=headers).json()["data"]
    list_01 = []
    list_02 = []
    id_01 = r[list(r.keys())[0]]["data"]
    id_02 = r[list(r.keys())[-1]]["data"]
    for a in list(id_01.keys()):
        list_01.append(a)
    for b in list(id_02.keys()):
        list_02.append(b)
    return list_01,list_02
 
# 签到01
def dealtask(Authorization,User_Agent):
    tasketids = task(Authorization,User_Agent)[0]
    for tasketid in tasketids:
        url = "http://appapi.jinzhuqianguan.com/api/Member/dealtask"
        data = {
            "tasketid":tasketid,
            "platform":"android",
            "channel":"10000",
            "is_hot":"0"
        }
        headers = {
            "Authorization":Authorization,
            "user-agent":User_Agent
        }
        msg = requests.post(url, data=data, headers=headers).json()["msg"]
        print(msg)

#签到02
def dealtask_01(Authorization,User_Agent):
    tasketids = task(Authorization,User_Agent)[-1]
    for tasketid in tasketids:
        url = "http://appapi.jinzhuqianguan.com/api//WakeupTask/dealTask"
        data = {
            "taskid":tasketid,
            "platform":"android",
            "channel":"10000",
            "is_hot":"0"
        }
        headers = {
            "Authorization":Authorization,
            "user-agent":User_Agent
        }
        msg = requests.post(url, data=data, headers=headers).json()["msg"]
        print(msg)

# 打开app
def dealTask(Authorization,User_Agent):
    for tasketid in range(2,4):
        print(tasketid)
        url = "http://appapi.jinzhuqianguan.com/api//WakeupTask/dealTask"
        data = {
            "taskid":tasketid,
            "platform":"android",
            "channel":"10000",
            "is_hot":"1"
        }
        headers = {
            "Authorization":Authorization,
            "user-agent":User_Agent
        }
        msg = requests.post(url, data=data, headers=headers).json()["msg"]
        print(msg)


def join(Authorization,User_Agent):
    url = "http://appapi.jinzhuqianguan.com/api/Game/join"
    data = {
        "platform":"android",
        "channel":"10000",
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    msg = requests.post(url, data=data, headers=headers).json()["msg"]
    print(msg)

def receivePrize(Authorization,User_Agent):
    url = "http://appapi.jinzhuqianguan.com/api/Game/receivePrize"
    data = {
        "platform":"android",
        "channel":"10000"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    msg = requests.post(url, data=data, headers=headers).json()["msg"]
    print(msg)

# 神秘任务
def mysterious(Authorization,User_Agent):
    url = "http://appapi.jinzhuqianguan.com/api//Member/dealtask"
    data = {
        "tasketid":"5",
        "platform":"android",
        "channel":"10000"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    msg = requests.post(url, data=data, headers=headers).json()["msg"]
    print(msg)
# 报名+总任务
def setGameChoose(Authorization,User_Agent):
    dealtask(Authorization,User_Agent)
    dealtask_01(Authorization,User_Agent)
    dealTask(Authorization,User_Agent)
    join(Authorization,User_Agent)
    mysterious(Authorization,User_Agent)
    url = "http://appapi.jinzhuqianguan.com/api/Game/setGameChoose"
    data = {
        "platform":"android",
        "channel":"10000",
        "issue":time.strftime('%Y%m%d', time.localtime()),
        "one":"1",
        "two":"1",
        "three":"2",
        "isauto":"1"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    msg = requests.post(url, data=data, headers=headers).json()["msg"]
    print(msg)
    receivePrize(Authorization,User_Agent)

# cookice
JZ_Authorizations=os.environ['JZ_Authorizations'].split(",")
User_Agent = ["Mozilla/5.0 (Linux; U; Android 10; zh-cn; YAL-AL00 Build/HUAWEIYAL-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1","Dalvik/2.1.0 (Linux; U; Android 8.0.0; BLN-AL10 Build/HONORBLN-AL10)"]
for Authorization,User_Agent in zip(JZ_Authorizations,User_Agent):
    setGameChoose(Authorization,User_Agent)
