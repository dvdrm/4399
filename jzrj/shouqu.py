# 注册地址：http://appapi.jinzhuqianguan.com/home/index?uucode=9VT87B2700&channel=10000
#  本人邀请码：9VT87B2700
'''
cron: */1 * * * *  python3 shouqu.py
new Env('金猪日记收金币');
'''

import requests
import os

def collects(Authorization,User_Agent):
    s = requests.session()
    collect_url = "http://appapi.jinzhuqianguan.com/api/Member/getCoin1"
    get_data = {
        "brand":"HUAWEI",
        "platform":"android",
        "channel":"400000",
    }
    headers = {
        "Authorization":Authorization,
        "user_agent":User_Agent
    }
    r = s.post(url=collect_url,data=get_data,headers=headers).json()
    print(r["msg"])
    print("领取奖励："+str(int(r["coin"]/10)))


User_Agent = ["Dalvik/2.1.0 (Linux; U; Android 11; Mi9 Pro 5G Build/RKQ1.200826.002)-ksad-android-3.3.23"]
# cookice
JZ_Authorizations=os.environ['JZ_Authorizations'].split(",")
for Authorization,User_Agent in zip(JZ_Authorizations,User_Agent):
    collects(Authorization,User_Agent) 
