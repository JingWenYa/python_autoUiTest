import PySimpleGUI as sg
layout = [
    [sg.Text('选择发帖类型'), sg.Radio('图文贴','Type', default=True),sg.Radio('问答贴','Type'),sg.Radio('视频贴','Type')],
    [sg.Text('输入发帖标题'), sg.InputText(size=(50,10)),sg.Text(size=(40,3),key='output')],
    [sg.Text('输入发帖内容'), sg.Multiline(size=(50,10),default_text='内容最少输入八个字'),sg.Text(size=(50,10),key='output')],
    [sg.Text('选择图片张数'), sg.Combo(['1张', '2张', '3张', '4张', '5张', '6张', '7张', '8张'], size=(10, 5),readonly=False)],
    # [sg.Combo(['1张', '2张', '3张', '4张', '5张', '6张', '7张', '8张'], default_value='1张')],
    [sg.Button('发布')]
]

window = sg.Window('发帖小工具',layout)
window.read()
window.close