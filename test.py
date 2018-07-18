from urllib.request import urlopen
import json

API_KEY = "814fcbef78be15dcc4bd405afec6914f"
url = "http://api.openweathermap.org/data/2.5/forecast?q=Canberra,au&APPID=#{API_KEY}"
#response = urlopen(url + "?q=Canberra,au&APPID=#{API_KEY}")
response = urlopen(url).read().decode('utf-8')

obj = json.loads(response)
name = obj['city']['name']
details = []
for state in obj['list']:
    detail = """
    Time : {}
        MAIN
            Temperature : {}
        WIND
            Degree : {}
            Speed  : {}
        WEATHER
            Description : {}
            Main        : {}
""".format(state['dt_txt'][11:16],
           state['main']['temp_kf'],
           state['wind']['deg'],
           state['wind']['speed'],
           state['weather'][0]['description'],
           state['weather'][0]['main'] + "\n" + "-" * 50)
    print(detail)
    details.append(detail)

# save the data to a file
with open('result', 'w') as fp:
    fp.write(str(name).upper() + " WEATHER\n" + "-" * 50 + "\n")
    for detail in details:
        fp.write(detail)
