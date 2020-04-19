import json
import requests
from urllib3 import *

disable_warnings()
http = PoolManager()

#�ش��������ݺ���
def reply_weather(content):
    #��ȡλ��
    location = content[0:-2]
    #�ͷ����� api-key����
    url = f'https://free-api.heweather.net/s6/weather/now?location={location}&key=8c321dd4895f4c32963c52e6aa3b0cfc'
    #request�õ�����json����
    data = http.request('GET', url).data.decode('utf-8')
    data = json.loads(data)
    #״̬��ok
    if data["HeWeather6"][0]['status'] == 'ok':
        data = data["HeWeather6"]
        res = '''
            ��ѯλ�ã�%s \n
            γ�ȣ�%s \n
            ���ȣ�%s \n
            �¶ȣ�%s \n
            ʪ�ȣ�%s \n
            ����%s \n
            ���������%s \n
            ����ʱ�䣺%s \n
            ''' % (data[0]['basic']['location'], data[0]['basic']['lat'],
                   data[0]['basic']['lon'], data[0]['now']['tmp'], data[0]['now']['hum'],
                   data[0]['now']['wind_dir'], data[0]['now']['cond_txt'],
                   data[0]['update']['loc'])
    else:
        res = '��ȡ����ʧ�ܣ��밴��ʽ������������+������'
    return res



