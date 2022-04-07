from flask import Flask, render_template, request
import requests
import json
import uvicorn

app = Flask(__name__)
app.debug = True

class ApiKey():
    api_key = '5430a591ad2a236c6e9fa319755565f4'





@app.route('/', methods=['GET', 'POST'])
def index():

    apikey = ApiKey.api_key
    city = request.form.get('city')
    

    

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}')
    res1 = json.loads(res.content)
    
    name_city = res1['name']
    clouds = res1['clouds']['all']
    country = res1['sys']['country']
    main_temp = res1 ['main']['temp']


    
    return render_template('index.html', response = res1, name_city = name_city, clouds = clouds, country = country, main_temp = main_temp)

if __name__ == '__main__':
    app.run()