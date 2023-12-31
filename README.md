# Weather

## Формальное описание
Формат вывода информации следующий:
```
текущее время: 2023-12-14 01:35:09+05:00
название города: Ufa
погодные условия: overcast clouds
текущая температура: -23.37 degrees Celsius
ощущается как: -29.18 degrees Celsius
скорость ветра: 1.79 m/c

```
## Установка ПО для работы приложения
1. Установить интерпретатор python версии 3.11 или выше.
2. В папке с файлами приложения создать виртуальное окружение с помощью консольной команды `python -m venv {venv name}`, после чего активировать его командой `venv\Scripts\activate.bat` для Windows или `source venv/bin/activate` для Linux и MacOS.
3. Установить требуемые библиотеки в активированное виртуальное окружение командой `pip install -r requirements.txt`
4. Для запуска приложения введите команду `python main.py`

## Запуск программы

Запустите программу с помощью командной строки: python main.py 
и выберите одну из доступных команд:
  - '1': получить информацию о погоде по названию города;
  - '2': получить информацию о погоде по текущему местоположению;
  - '3': получить историю запросов о погоде;
  - '4': завершить выполнение программы.
