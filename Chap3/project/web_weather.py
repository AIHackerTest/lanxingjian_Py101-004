# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from sources import fetchWeather, weather_info

app = Flask(__name__)
history = []
# 模板渲染,进入查询系统
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/user_request', methods = ['GET'])
def user_request():
    try:
        city = request.args.get('city')
        weather_data = weather_info(city, fetchWeather(city))
        history.append(weather_data)
        return render_template('query.html', weather_data=weather_data)
    except KeyError:
        if request.args.get('help') == '帮助':
            return render_template('help.html')
        elif request.args.get('history') == '历史':
            return render_template('history.html',history=history)
        else:
            return render_template('Error.html')

if __name__ == "__main__":
    app.run(debug = True)
