import requests
from config import open_weather_token
from pprint import pprint

def get_wether(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
            # f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={open_weather_token}"
        )
        data = r.json()
        pprint(data)
        city = data["name"]
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        print(f"Погода в городе: {city}\n"
              f"Температура: {temp}\n"
              f"Ветер: {wind}\n")


    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город: ")
    get_wether(city, open_weather_token)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
