# 注册地址：http://appapi.jinzhuqianguan.com/home/index?uucode=9VT87B2700&channel=10000
#  本人邀请码：9VT87B2700
'''
cron: 5 0,7 * * */2  python3 pk.py
new Env('金猪日记PK');
'''

import os
import requests
import random
import time

def collects(Authorization,User_Agent):
    s = requests.session()
    friendid = random.choice(getOwnerlist(Authorization,User_Agent))
    url= "http://appapi.jinzhuqianguan.com/api/Game/pk"
    data= {
        "channel":"10000",
        "friendid":friendid,
        "platform":"android"
        }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    r = s.post(url=url,data=data,headers=headers).json()
    if r["status"]=="200":
        if r["data"]["lastresult"]==1:
            print("你赢了")
        elif r["data"]["lastresult"]==2:
            print("你输了")
        else:
            print("平局")
    elif r["status"]=="201":
        print(r["msg"])


def getOwnerlist(Authorization,User_Agent):
    s = requests.session()
    url = "http://appapi.jinzhuqianguan.com/api/Game/menpiaolist"
    data= {
        "channel":"10000",
        "issue":time.strftime('%Y%m%d', time.localtime()),
        "platform":"android"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    r = s.post(url=url,data=data,headers=headers).json()["data"]
    friendid=[]
    for res in r:
        friendid.append(res["member_id"])
    return friendid
    
# cookice
JZ_Authorizations=os.environ['JZ_Authorizations'].split(",")
User_Agent = ["Mozilla/5.0 (Linux; U; Android 10; zh-cn; YAL-AL00 Build/HUAWEIYAL-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1","Dalvik/2.1.0 (Linux; U; Android 8.0.0; BLN-AL10 Build/HONORBLN-AL10)"]
for Authorization,User_Agent in zip(JZ_Authorizations,User_Agent):
    collects(Authorization,User_Agent)


