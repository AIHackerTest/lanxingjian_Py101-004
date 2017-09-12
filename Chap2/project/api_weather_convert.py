import requests
import json

def print_help():
        print("""
        - 输入城市名，返回该城市最新的天气数据
        - 输入指令，获取帮助信息（一般使用h或help）
        - 输入指令，获取历史查询信息（一般使用history）
        - 输入指令，退出程序的交互（一般使用quit或者exit）
        - 输入指令，转换温度（一般使用f转换成华氏度，使用c转换成摄氏度。
        温度一开始默认为摄氏度）
        """)
# 定义函数，获取api上的数据
def fetchweather(location,unit):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key':'nx0kuprfirtdt9ej',
        'location': location,
        'language': 'zh-Hans',
        'unit': unit
    }, timeout=1)
    return result
#定义函数，输出天气、更新时间、温度的一个字符串
def weather_info(result):
    txt = json.loads(result.text.replace("T","T "))
    weather = txt['results'][0]['now']['text']
    date = txt['results'][0]['last_update']
    temp = txt['results'][0]['now']['temperature']
    weather_data =  f'{date}\n{order}  天气:{weather}\t温度：{temp}\n'
    return weather_data

unit = 'c'  # 默认温度输出为摄氏度，给unit一个默认值
histories = [] # 创建一个空的历史查询列表

while True:
    order = input('输入您想要查询天气的城市：')
    # 获取天气值，并且制作查询列表
    try :
        result = fetchweather(order,unit)
        weather_data = weather_info(result)
        print(weather_data)
        histories.append(weather_data)
    except KeyError:
        # 获取帮助文档
        if order == 'help' or order == 'h':
            print_help()
        # 退出程序
        elif order in ['quit','q','exit']:
            print("感谢您的使用，再见！")
            break
        # 获取历史查询信息
        elif order == 'history':
            for history_info in histories:
                print(history_info)
        # 实现温度转换功能
        elif order in ['c','f']:
            unit = order
            print("温度已转换\n")
        else:
            print("抱歉，您输入的城市暂时没有数据！请输入其他城市查询。")
