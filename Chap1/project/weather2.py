file = open('weather_info.txt')

weather_sys = {}
history_info = ''

for info in file.readlines():
    city = info.split(',')[0]
    weather = info.split(',')[1].strip()
    weather_sys[city] = weather

while True:
    order = input('input the city you want :')
    if order in weather_sys.keys():
        weather_data = weather_sys[order]
        print(weather_data)
        history_data = order + ',' + weather_data + '\n'
        history_info = history_info + history_data
    elif order in ['help','Help','-h','-H']:
        print("""
        -输入城市名，获取该城市的天气情况
        -输入指令help，获取帮助信息
        -输入指令history，获取历史查询信息
        -输入指令quit，退出程序""")
    elif order == "history":
        print(history_info)
    elif order == "quit":
        print("您所查询过的信息是:\n%s" % history_info)
        break
    else:
        print("抱歉，您搜索的城市天气暂时没有！请输入其他城市。")
