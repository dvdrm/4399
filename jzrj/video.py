# 注册地址：http://appapi.jinzhuqianguan.com/home/index?uucode=9VT87B2700&channel=10000
#  本人邀请码：9VT87B2700
'''
cron: 25 8-11 * * * *  python3 video.py
new Env('金猪日记看视频');
'''

import os
import requests
def video(Authorization,User_Agent):
    s = requests.session()
    url = "http://appapi.jinzhuqianguan.com/api//Member/getAdVideoReward"
    data= {
        "channel":"10000",
        "type":3,
        "platform":"android"
    }
    headers = {
        "Authorization":Authorization,
        "user-agent":User_Agent
    }
    r = s.post(url=url,data=data,headers=headers).json()["msg"]
    print(r)

# cookice
JZ_Authorizations=os.environ['JZ_Authorizations'].split(",")
User_Agent = ["Mozilla/5.0 (Linux; U; Android 10; zh-cn; YAL-AL00 Build/HUAWEIYAL-AL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/5.0 Mobile Safari/533.1","Dalvik/2.1.0 (Linux; U; Android 8.0.0; BLN-AL10 Build/HONORBLN-AL10)"]
for Authorization,User_Agent in zip(JZ_Authorizations,User_Agent):
    video(Authorization,User_Agent)