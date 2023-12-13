import requests
import geocoder
import sqlite3
from datetime import datetime, timezone, timedelta

api_key = "2541ab2df295ab1935fab364a53109d3"

def print_weather_info(location: str, data_from_file: dict):

    utc_timestamp = data_from_file["dt"]

    offset = data_from_file["timezone"]

    tz = timezone(timedelta(seconds=offset))
    result_time = datetime.fromtimestamp(utc_timestamp, tz)

    formatted_time = result_time

    print("текущее время:", formatted_time)
    print("название города:", location)
    print("погодные условия:", data_from_file["weather"][0]["description"])
    print("текущая температура:", data_from_file["main"]["temp"], "degrees Celsius")
    print("ощущается как:", data_from_file["main"]["feels_like"], "degrees Celsius")
    print("скорость ветра:", data_from_file["wind"]["speed"], "m/c")

def get_weather_by_city(city: str):
    """
    Получение информации о погоде по названию города.

    Аргумент:
    city - название города.
    """

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&"
        response = requests.get(url)
        response.raise_for_status()  
        data_from_file = response.json()

        print_weather_info(city, data_from_file)
        save_to_database((datetime.now(), city, data_from_file["weather"][0]["description"], data_from_file["main"]["temp"], data_from_file["main"]["feels_like"], data_from_file["wind"]["speed"]))
    except requests.exceptions.HTTPError as err:
        print("Такого города не существует, попробуйте снова!")
    except requests.exceptions.RequestException as err:
        print("Проблемы с соединением, попробуйте позже!")

def get_weather_by_location():

    try:
        location = geocoder.ip("me")

        if location:
            latitude, longitude = location.latlng
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric&"
            response = requests.get(url)
            response.raise_for_status()  
            data_from_file = response.json()
           
            print_weather_info(location.address, data_from_file)
            save_to_database((datetime.now(), location.address, data_from_file["weather"][0]["description"], data_from_file["main"]["temp"], data_from_file["main"]["feels_like"], data_from_file["wind"]["speed"]))
        else:
            print("Не удалось определить текущее местоположение")
    except requests.exceptions.HTTPError as err:
        print("Такого города не существует, попробуйте снова!")
    except requests.exceptions.RequestException as err:
        print("Проблемы с соединением, попробуйте позже!")

def save_to_database(data: tuple):
    try:
        connection = sqlite3.connect("weather.db")
        cursor = connection.cursor()

        cursor.execute('''create table if not exists weather_requests
                          (id integer primary key autoincrement, 
                          timestamp datetime, 
                          city text, 
                          weather_condition text, 
                          temperature float,
                          feeling float,
                          speed float)''')

        formatted_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute("INSERT INTO weather_requests (timestamp, city, weather_condition, temperature, feeling, speed) VALUES (?, ?, ?, ?, ?, ?)", (formatted_time,) + data[1:])
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("ошибка при работе с базой данных, попробуйте снова!")

def print_history(n: str):

    try:
        n = int(n)
        if n < 0:
            print("Введите значение n > 0")
        else:
            connection = sqlite3.connect("weather.db")
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM weather_requests ORDER BY timestamp DESC LIMIT {n}")
            results = cursor.fetchall()
            connection.close()

            print("Последние", n, "запросов:")
            print("=" * 20)
            for result in results:
                print("время запроса:", result[1])
                print("название города:", result[2])
                print("погодные условия:", result[3])
                print("температура:", result[4], "degrees Celsius")
                print("ощущение:", result[5], "degrees Celsius")
                print("скорость ветра:", result[6], "m/c")
                print("=" * 20)
            
    except ValueError:
        print("введите целое число для 'history'.")
    except sqlite3.OperationalError:
        print("история запросов пуста.")
    except sqlite3.Error as error:
        print("ошибка при работе с базой данных, попробуйте снова!")

menu_text = (
    "\nкоманды:\n1. погода по названию города\n2. погода по текущему местоположению\n"
    "3. просмотр истории запросов\n4. закрыть программу\n"
)

def main():
    while True:
        print(menu_text)
        user_input = input("\nВыберите одну из команд и введите её: ").strip()
        if user_input == '4':
            print("Завершение программы.")
            break
        elif user_input == '1':
            city = input("Введите название города: ").strip()
            print()
            get_weather_by_city(city)
        elif user_input == '2':
            print()
            get_weather_by_location()
        elif user_input == '3':
            n = input("Введите количество последних запросов: ").strip()
            print()
            print_history(n)
        else:
            print("Неизвестная команда. Пожалуйста, выберите из предложенного списка.")

if __name__ == "__main__":
    main()

