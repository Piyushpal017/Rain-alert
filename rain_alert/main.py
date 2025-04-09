api_key = "YOUR_api_key"
import requests
my_lat = 28.6667
my_long = 77.2167

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4
}

def telegram_bot_sendtext(bot_message):
    
    bot_token = 'Your_bot_token'
    bot_chatID = 'Your_bot_chatID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

weather_response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
weather_response.raise_for_status()
data = weather_response.json()

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    test = telegram_bot_sendtext("It's going to rain 🌧️ today. Remember to bring an ☔")
    


    



