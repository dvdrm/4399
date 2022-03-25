# 注册地址：http://appapi.jinzhuqianguan.com/home/index?uucode=9VT87B2700&channel=10000
#  本人邀请码：9VT87B2700
'''
cron: */10 * * * *  python3 extract.py
new Env('金猪日记转盘');
'''

import requests
from time import sleep
import os

# 查看次数
def lotteryNum(Authorization,User_Agent):
    url = "http://appapi.jinzhuqianguan.com/api/Props/lotteryNum"
    data = {
        "brand":"HUAWEI",
        "platform":"android",
        "channel":"10000"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    r = requests.post(url, data=data, headers=headers).json()["data"]
    if str(r) =="0":
        print("暂无次数")
    else:
        for a in str(r):
          receiveLotteryReward(Authorization,User_Agent)

# 抽奖
def lotteryNew(Authorization,User_Agent):
    url = "http://appapi.jinzhuqianguan.com/api//Props/lotteryNew"
    data = {
        "brand":"HUAWEI",
        "platform":"android",
        "channel":"10000"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    r = requests.post(url, data=data, headers=headers).json()
    recordId = r["data"]["recordId"]
    msg = r["msg"]
    print(msg)
    return recordId

# 领取
def receiveLotteryReward(Authorization,User_Agent):
    recordId = lotteryNew(Authorization,User_Agent)
    sleep(30)
    url = "http://appapi.jinzhuqianguan.com/api/Props/receiveLotteryReward"
    data = {
        "rid":recordId,
        "platform":"android",
        "channel":"10000"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    r = requests.post(url, data=data, headers=headers).json()["msg"]
    print(r)
    
# cookice
JZ_Authorizations=os.environ['JZ_Authorizations'].split(",")
User_Agent = ["Mozilla/5.0 (Linux; U; Android 10; zh-cn; YAL-AL00 Build/HUAWEIYAL-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1","Dalvik/2.1.0 (Linux; U; Android 8.0.0; BLN-AL10 Build/HONORBLN-AL10)"]
for Authorization,User_Agent in zip(JZ_Authorizations,User_Agent):
    lotteryNum(Authorization,User_Agent)
