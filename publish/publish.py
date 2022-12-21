import PySimpleGUI as sg
import requests
import redis
import json

layout = [
    [sg.Text('输入用户uid'), sg.InputText(key='-uid-', size=(25, 20))],
    [sg.Text('选择发帖类型'), sg.Radio('图文贴', 'Type', default=True, key='-T-'),
     sg.Radio('问答贴', 'Type', key='-Q-'), sg.Radio('视频贴', 'Type', key='-V-')],
    [sg.Text('输入发帖标题'), sg.InputText(key='-Title-', size=(50, 20), default_text='发帖标题')],
    [sg.Text('输入发帖内容'), sg.Multiline(key='-Content-', size=(50, 10), default_text='内容最少输入八个字')],
    [sg.Button('发布', key='发布')]
]

windows = sg.Window('发帖小工具', layout,size=(600, 350))

while True:
    event, values = windows.read()
    if event in (None, '取消'):
        break

    # 请求url
    url = 'https://test-circle.seeyouyima.com'

    # 获取永久授权头
    def get_auth(uid):
        url = f"http://test-users.seeyouyima.com/uc?do=user_id&user_id={uid}&pass=meiyou"
        resp = requests.get(url)
        resp_json = resp.json()
        auth = resp_json['data']['authorization']
        return auth

    #获取请求头
    def get_headers(uid):
        auth = get_auth(uid)
        headers = {
            'myclient': '0120851000000000',
            'authorization': auth,
            'content-type': 'application/json'
        }
        return headers


    # 清除redis缓存
    def delete_redis(uid, type):
        r = redis.Redis(host='test-community-redis.meiyoucloud.com', port=8635,
                        password='0RJ@QLrPfzrwPiNN9x9BpEOH63B+3rSc')
        if type == 'V':
            r.delete('circle:video_forum_topic_time_interval_' + str(uid))
        else:
            r.delete('circle:forum_topic_time_interval_' + str(uid))


    # 发图文贴
    if values['-T-']:
        path1 = '/community/forums/0/topics?sign=457CC6&app_id=01&channelID=AppStore&lang=zh&mode=0&platform=ios&scale=3.0&themeid=0'
        json = {
            "verify": "noneed",
            "title": values['-Title-'],
            "content": values['-Content-'],
            "use_anonymous": False,
            "is_share_mood": 1,
            "type": 1,
            "is_watermark": 1,
            'images': ["https://test-sc.seeyouyima.com/forum-iOS-220557675-3A78BF41075A0CE0_720_1560.jpg"]
        }
        # 清除redis缓存
        delete_redis(values['-uid-'], 'T')
        # 请求发帖接口
        headers = get_headers(values['-uid-'])
        resp = requests.post(url + path1, data=None, json=json, headers=headers)
        resp_json = resp.json()
        if resp.status_code == 200:
            sg.popup('请求成功,topic_id为', resp_json['topic_id'])
        else:
            sg.popup(resp_json['message'])
        print(resp.content.decode())


    # 发布问答贴
    if values['-Q-']:
        path2 = '/community/forums/0/topics?app_id=01&channelID=AppStore&lang=zh&mode=0&platform=ios&scale=3.0&themeid=0'
        json = {
            "title": values['-Title-'],
            "content": values['-Content-'],
            "use_anonymous": False,
            "is_ask": 1,
            'images': ["https://test-sc.seeyouyima.com/forum-iOS-220557675-3A78BF41075A0CE0_720_1560.jpg"]
        }
        # 清除redis缓存
        delete_redis(values['-uid-'], 'Q')
        # 请求发帖接口
        headers = get_headers(values['-uid-'])
        resp = requests.post(url + path2, data=None, json=json, headers=headers)
        resp_json = resp.json()
        resp_json = resp.json()
        if resp.status_code == 200:
            sg.popup('请求成功,topic_id为', resp_json['topic_id'])
        else:
            sg.popup(resp_json['message'])
        print(resp.content.decode())


    # 发布视频贴
    if values['-V-']:
        path3 = '/v2/video_post'
        json = {
            'special_effects': [],
            'type': 2,
            'video_body': {
                'video_thumb': "https://test-sc.seeyouyima.com/news/vod/2022/12/svrvideo-iOS-220557675-223B78B0D8A6BFA2_438_780.jpg",
                'video_time': "13.05",
                'video_thumb_height': 780,
                'video_url': 'https://test-sc.seeyouyima.com/news/vod/2022/12/svrvideo-iOS-220557675-223B78B0D8A6BFA2_592_1280.mp4',
                'video_thumb_width': 438,
                'tool_id': 0
            },
            "title": values['-Title-']
        }
        # 清除redis缓存
        delete_redis(values['-uid-'], 'V')
        # 请求发帖接口
        headers = get_headers(values['-uid-'])
        resp = requests.post(url + path3, data=None, json=json, headers=headers)
        resp_json = resp.json()
        if resp_json['code'] == 0:
            sg.popup('请求成功,topic_id为', resp_json['data']['video_id'])
        else:
            sg.popup(resp_json['message'])
        print(resp.content.decode())

windows.close()




