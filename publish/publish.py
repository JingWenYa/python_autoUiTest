import PySimpleGUI as sg
import requests
import redis

layout = [
    [sg.Text('输入用户uid'), sg.InputText(key='-uid-', size=(25, 20))],
    [sg.Text('选择发帖类型'), sg.Radio('图文贴', 'Type', default=True, key='-T-', enable_events=True),
     sg.Radio('问答贴', 'Type', key='-Q-'), sg.Radio('视频贴', 'Type', key='-V-')],
    [sg.Text('输入发帖标题'), sg.InputText(key='-Title-', size=(50, 20))],
    [sg.Text('输入发帖内容'), sg.Multiline(key='-Content-', size=(50, 10), default_text='内容最少输入八个字')],
    [sg.Button('发布', key='发布')]
]

windows = sg.Window('发帖小工具', layout)
event, values = windows.read()

#数据准备
url = 'https://test-circle.seeyouyima.com'
headers = {
    'myclient': '0120851000000000',
    'authorization': 'XDS 7.dw6g3Pxvx2dYpg3gU695hiw7lUJtELgA6bCSAXdgMGU',
    'content-type': 'application/json'
}

# 清除redis缓存
def delete_redis(uid):
    r = redis.Redis(host='test-community-redis.meiyoucloud.com', port=8635,
                    password='0RJ@QLrPfzrwPiNN9x9BpEOH63B+3rSc')
    r.delete('circle:forum_topic_time_interval_' + str(uid))

#发起请求
def post(kwargs=None):
    resp = requests.post(url, data=None, json=None, **kwargs)
    return resp.content

# 发图文贴
if values['-T-']:
    path1 = '/community/forums/0/topics?sign=457CC6&app_id=01&channelID=AppStore&lang=zh&mode=0&platform=ios&scale=3.0&themeid=0&v=8.5.1&v1=8.51.0.0'
    json = {
        "verify": "noneed",
        "title": values['-Title-'],
        "content": values['-Content-'],
        "use_anonymous": 'false',
        "is_share_mood": 1,
        "is_watermark": 1,
        'images': ["https://test-sc.seeyouyima.com/forum-iOS-220557675-3A78BF41075A0CE0_720_1560.jpg"]
    }
    #清除redis缓存
    delete_redis(values['-uid-'])
    #请求发帖接口
    resp = requests.post(url+path1, data=None, json=json, headers=headers)
    print(resp.url)
    print(resp.content.decode())


#发布问答贴
if values['-Q-']:
    path2 = '/community/forums/0/topics?app_id=01&channelID=AppStore&lang=zh&mode=0&platform=ios&scale=3.0&themeid=0&v=8.5.1&v1=8.51.0.0'
    json = {
        "title": values['-Title-'],
        "content": values['-Content-'],
        "use_anonymous": 'false',
        "is_ask": 1,
        'images': ["https://test-sc.seeyouyima.com/forum-iOS-220557675-3A78BF41075A0CE0_720_1560.jpg"]
    }
    # 清除redis缓存
    delete_redis(values['-uid-'])
    # 请求发帖接口
    resp = requests.post(url + path2, data=None, json=json, headers=headers)
    print(resp.url)
    print(resp.content.decode())


#发布视频贴
if values['-V-']:
    path2 = '/community/forums/0/topics?app_id=01&channelID=AppStore&lang=zh&mode=0&platform=ios&scale=3.0&themeid=0&v=8.5.1&v1=8.51.0.0'
    json = {
        "title": values['-Title-'],
        "content": values['-Content-'],
        "use_anonymous": 'false',
        "is_ask": 1,
        'images': ["https://test-sc.seeyouyima.com/forum-iOS-220557675-3A78BF41075A0CE0_720_1560.jpg"]
    }


windows.close()