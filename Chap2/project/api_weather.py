import requests
import json

def print_help():
        print("""
        - 输入城市名，返回该城市最新的天气数据
        - 输入指令，获取帮助信息（一般使用h或help）
        - 输入指令，获取历史查询信息（一般使用history）
        - 输入指令，退出程序的交互（一般使用quit或者exit）
        """)

def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key':'nx0kuprfirtdt9ej',
        'location': location,
        'language': 'zh-Hans',
        'unit': ''
    }, timeout=1)
    return result

def weather_info(result):
    txt = json.loads(result.text.replace("T","T "))
    weather = txt['results'][0]['now']['text']
    date = txt['results'][0]['last_update']
    temp = txt['results'][0]['now']['temperature']
    weather_data =  f'{date}\n{order}  天气:{weather}\t温度：{temp}摄氏度\n'
    return weather_data

histories = []
while True:
    order = input('输入您想要查询天气的城市：')
    result = fetchWeather(order)
    if result:
    #if order in json.loads(result.text)['results'][0]['location']['name']:
        weather_data = weather_info(result)
        print(weather_data)
        histories.append(weather_data)
    elif order == 'help' or order == 'h':
        print_help()
    elif order in ['quit','q','exit']:
        print("感谢您的使用，再见！")
        break
    elif order == 'history':
        for history_info in histories:
            print(history_info)
    else:
        print("抱歉，您输入的城市暂时没有数据！请输入其他城市查询。")
