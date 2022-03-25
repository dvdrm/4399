# 注册地址：http://appapi.jinzhuqianguan.com/home/index?uucode=9VT87B2700&channel=10000
#  本人邀请码：9VT87B2700
'''
cron: */2 * * * */2  python3 prop.py
new Env('金猪日记报名pk并且使用道具');
'''

import os
import time
import requests


# 报名
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


# 设置PK规则
def setGameChoose(Authorization,User_Agent):
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

# 道具列表
def myProps(Authorization,User_Agent):
    url = "http://appapi.jinzhuqianguan.com/api/Props/myProps"
    data = {
        "limit":"100",
        "page":"1",
        "use_type":"1",
        "game_type":"1",
        "platform":"android",
        "channel":"10000"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    r = requests.post(url, data=data, headers=headers).json()["data"]
    id_obj=[]
    for ids in r:
        id_obj.append(ids["id"])
    return id_obj

# 执行使用道具
def useProps(Authorization,User_Agent):
    join(Authorization,User_Agent)  # 执行报名
    setGameChoose(Authorization,User_Agent) # 设置规则
    ids = myProps(Authorization,User_Agent)
    if ids == []:
        print("暂无道具")
    else:
        for idobj in ids:
            url = "http://appapi.jinzhuqianguan.com/api/Props/useProps"
            data = {
                "id":idobj,
                "platform":"android",
                "channel":"10000"
            }
            headers = {
                "Authorization":Authorization,
                "user-agent":User_Agent
            }
            r = requests.post(url, data=data, headers=headers).json()["msg"]
            print(r)
            time.sleep(3)

# cookice
JZ_Authorizations=os.environ['JZ_Authorizations'].split(",")
User_Agent = ["Mozilla/5.0 (Linux; U; Android 10; zh-cn; YAL-AL00 Build/HUAWEIYAL-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1","Dalvik/2.1.0 (Linux; U; Android 8.0.0; BLN-AL10 Build/HONORBLN-AL10)"]
for Authorization,User_Agent in zip(JZ_Authorizations,User_Agent):
    useProps(Authorization,User_Agent)
