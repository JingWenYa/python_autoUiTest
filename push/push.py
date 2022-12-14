import PySimpleGUI as sg
layout = [
    [sg.Text('选择发帖类型'), sg.Radio('图文贴','Type', default=True,key='-T-'),sg.Radio('问答贴','Type',key='-Q-'),sg.Radio('视频贴','Type',key='-V-')],
    [sg.Text('输入发帖标题'), sg.InputText(key='-Title1-',size=(50,20))],
    [sg.Text('输入发帖内容'), sg.Multiline(key='-Content-',size=(50,10),default_text='内容最少输入八个字')],
    [sg.Text('选择图片张数'), sg.Combo(['1张', '2张', '3张', '4张', '5张', '6张', '7张', '8张'], size=(10, 5),readonly=False,key='-PictureNum-')],
    [sg.Button('发布',key='-Publish-')]
]

windows = sg.Window('发帖小工具',layout)
# while True:
#     event, values = windows.read()
#     if event == sg.WIN_CLOSED:
#         windows.close()
#         break
#     if event == "发布":
#         print(windows['标题'].get())
#     if event == "图文":
#         windows["视频"].SetTooltip("哈哈哈")
#         print("111")
event,values = windows.read()
windows.close()
print(values[0])




