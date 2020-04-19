from PyWeChatSpy import WeChatSpy
import requests
from weather import *
import re

#wxrobot���

def get_reply(data):
    # key��ȡ��ַhttp://xiao.douqq.com/
    url = f"http://api.douqq.com/?key=dUk1cEtUdmZxc2RCPW5XaFdBdT1lWUJiSnhzQUFBPT0&msg={data}"
    resp = requests.get(url)
    return resp.text

#��ʱ�ӿڣ����޸ģ�

def parser(data):
    if data["type"] == 1:
        print(data)
    elif data["type"] == 200:
        # ����
        pass
    elif data["type"] == 203:
        print("΢���˳���¼")
    elif data["type"] == 5:
        # ��Ϣ
        for item in data["data"]:
            content = item["content"]
            print(content)
            #����յ����ݸ�ʽΪxx����������ƥ��
            if re.match('(\w){1,10}����', content):
                #����weather����
                reply = reply_weather(content)
                print(reply)
            else:
                reply = get_reply(content)
                print(reply)
            spy.send_text("wxid_3xollkhxgq5t22", reply)
    elif data["type"] == 2:
        print(data)

if __name__ == '__main__':
    spy = WeChatSpy(parser=parser)
    spy.run()



