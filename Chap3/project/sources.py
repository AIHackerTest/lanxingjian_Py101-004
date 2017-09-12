import requests
import json
def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key':'nx0kuprfirtdt9ej',
        'location': location,
        'language': 'zh-Hans',
        'unit': ''
    }, timeout=10)
    return result

def weather_info(location,result):
    txt = json.loads(result.text)
    weather = txt['results'][0]['now']['text']
    date = txt['results'][0]['last_update']
    temp = txt['results'][0]['now']['temperature']
    weather_data =  f'\n{location}\n天气:{weather}\n温度:{temp}摄氏度\n更新时间:{date}\n'
    return weather_data
