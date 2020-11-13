import random
import json

with open("picture.json","r",encoding="utf-8") as jFile_5:
    jdata_5 = json.load(jFile_5)

def Rolled():
    pic_list = []
    pic_num = 0

    sp_num = 0
    ssr_num = 0
    sr_num = 0
    r_num = 0

    chance = 10
    while chance != 0:
        luckNum = random.randint(1,10000)
        pic_num = pic_num + luckNum
        if luckNum <= 25:
            pic_list.append(SP())
            sp_num = sp_num + 1
        elif luckNum <= 125:
            pic_list.append(SSR())
            ssr_num = ssr_num + 1
        elif luckNum <= 2125:
            pic_list.append(SR())
            sr_num = sr_num + 1
        elif luckNum <= 10000:
            pic_list.append(R())
            r_num = r_num + 1
        chance = chance - 1
    return pic_list, pic_num, [sp_num, ssr_num, sr_num, r_num]

def SP():
    a = random.choice(jdata_5["sp"])
    return a[1]

def SSR():
    b = random.choice(jdata_5["ssr"])
    return b[1]

def SR():
    c = random.choice(jdata_5["sr"])
    return c[1]

def R():
    d = random.choice(jdata_5["r"])
    return d[1]