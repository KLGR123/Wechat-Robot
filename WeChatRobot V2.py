from PyWeChatSpy import WeChatSpy
import json
import requests

try_times = 0
ar_times = 0
temp_times = 0

def parser(data):
    def tryTuLin(current_content, number_wxid):
        urls = 'http://openapi.tuling123.com/openapi/api/v2'  #�����ַ
        data_dic = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": current_content
                },
                "inputImage": {
                    "url": "imageUrl"
                },
            },
            "userInfo": {
                "apiKey": "�������api������",
                "userId": number_wxid
            }
        }
        data_json = json.dumps(data_dic).encode('utf8')
        a = requests.post(urls, data_json)  # ʹ��post����
        content = (a._content).decode('utf-8')  # ��ȡ���ؽ��_content���ԣ�����
        res = json.loads(content)['results'] # �����л�
        for i in res:
            back_content = i['values']['text']
        print(back_content)
        spy.send_text(current_wxid, back_content)
        return back_content

    #����useridҪ���������int���ͣ���wxid������һ���ַ������ͣ�����ͨ�����ַ����е�ÿ���ַ�
    # ת����asc�����ۼӣ�ʵ����������int���͵�ͬʱ��ת�����idҲ����һһ��Ӧ
    def wxidtonumber(current_wxid):
        number_wxid = 0
        for i in current_wxid:
            number_wxid += ord(i) #�����ַ���Ӧ��ASCII
        return number_wxid

    print(data)

    if 'data' in data:  # ��Ϊ���û�յ������򲻻ᴫ��data�����Ե��յ�����ʱ��ִ���������
        for item in data['data']:
            current_self = item['self']  # selfΪ0��Ϊ�յ����ݣ�Ϊ1��Ϊ��������
            current_wxid = item['wxid1']  # �Է���wxid
            current_content = item['content']  # �յ�������

        global temp_content, temp_times, ar_times
        if temp_times == 0:  # temp_timesĬ��ֵΪ0
            temp_content = current_content  # ��ֵ
            temp_times += 1  # ��ֹ�ٴ�ִ��
        if temp_content != current_content:  # data�е�contentˢ�£���ζ���յ����µ�����
            ar_times = 0  # ��ֵΪ0
            temp_content = current_content  # ��ֵ
        if current_self == 0:
            if ar_times == 0:  # ֵΪ0ʱ�ż���ִ��
                content1 = '���յ�!'
                number_wxid = wxidtonumber(current_wxid)  # wxid���ַ���ͨ������ת��Ϊ������
                tryTuLin(current_content, number_wxid)  # ����ͼ�������api�Զ��ظ�
                print('auto send success')  # ����̨��ӡ�Զ��ظ��ɹ�
                ar_times += 1  # ��ֹ�ٴ�ִ��
        # ����temp_times�Լ�ar_times����Ϊ�˷�ֹ�ٴ�ִ��
        # temp_times���ڵ�������ʵ�ֳ���ʼ���һ��ִ��
        # ar_times���ڵ������ǵ�data�е�content�����ı�ʱ���ٵ���api
    else:
        raise Exception

if __name__ == '__main__':
    try:
        spy = WeChatSpy(parser=parser)
        spy.run()
    except Exception as e:
        print(e)