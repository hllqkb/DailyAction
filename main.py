from win11toast import toast
import requests
import json
from bs4 import BeautifulSoup
import os
from config import *
if open_random_sentence:
    # 发起http请求
    response = requests.get(sentence_url)
    #解析JSON数据
    soup = BeautifulSoup(response.text, 'html.parser')
    favicon_path=os.path.join(os.path.dirname(__file__),'img/favicon.ico')
    print(favicon_path)
    #  把text转成json格式
    data = json.loads(soup.text)
    # 打印json数据
    sentence=(data['hitokoto'])
    # 句子来源
    sentence_from=(data['from'])
    if open_random_img:
       #  随机选择一张图片
        img_response = requests.get(img_url)
        with open('img.jpg', 'wb') as f:
            
            f.write(img_response.content)
            f.close()
        img_path=os.path.join(os.path.dirname(__file__),'img.jpg')
        #  显示通知
        toast_respose=toast(title,sentence,selection=['MC', 'IDEA', 'Other'], button='Submit',image=img_path,
            icon=favicon_path)
        # toast_respose_json=json.loads(toast_respose)
        try:
            result=toast_respose['user_input']['selection']
        except:
            result='404.webp'
        if result == 'MC':
            # 打开浏览器页面
            os.startfile('https://www.bilibili.com/list/ml2481574454?spm_id_from=333.1387.0.0&oid=804910460&bvid=BV1ry4y1V7Go')
        elif result == 'IDEA':
            # 打开IDEA
            os.startfile(r'C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2021.1.1\bin\idea64.exe')
        elif result == '' or result == 'Other':
            os.startfile('https://www.bilibili.com/list/ml2481574454?spm_id_from=333.1387.0.0&oid=804910460&bvid=BV1ry4y1V7Go')

else:
    toast('Hello', 'Hello from Python',selection=['Apple', 'Banana', 'Grape'], button='Submit',
        icon=r'D:\code\DailyAction\img\favicon.ico')
