# Weather

## Формальное описание
Формат вывода информации следующий:
```
Текущее время: 2023-10-03 09:48:47+03:00
Название города: Санкт-Петербург
Погодные условия: облачно
Текущая температура: 12 градусов по цельсию
Ощущается как: 11 градусов по цельсию
Скорость ветра: 5 м/c
```
## Установка ПО для работы приложения
1. Установить интерпретатор python версии 3.11 или выше.
2. В папке с файлами приложения создать виртуальное окружение с помощью консольной команды `python -m venv {venv name}`, после чего активировать его командой `venv\Scripts\activate.bat` для Windows или `source venv/bin/activate` для Linux и MacOS.
3. Установить требуемые библиотеки в активированное виртуальное окружение командой `pip install -r requirements.txt`
4. Для запуска приложения введите команду `python main.py`

## Запуск программы

Запустите программу с помощью командной строки: python main.py 
И выберите одну из доступных команд:
  - '1': получить информацию о погоде по названию города;
  - '2': получить информацию о погоде по текущему местоположению;
  - '3': получить историю запросов о погоде;
  - '4': завершить выполнение программы.
