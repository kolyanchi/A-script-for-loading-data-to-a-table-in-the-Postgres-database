# A-script-for-loading-data-to-a-table-in-the-Postgres-database
A script for loading data to a table in the Postgres database, run by a macro from an excel file

Задача - Создать скрипт upload.py (python 3) и из него исполняемый файл upload.exe, запускаемый по кнопке "Загрузить"* в файле "названия точек.xlsm",
для загрузки/обновления данных из файла в таблицу в БД Postgres. 

*При нажатии кнопки, VBA макрос(уже есть в файле "названия точек.xlsm") запускает upload.exe с аргументом (путь до файла "названия точек.xlsm")

1. Создать таблицу endpoint_names в БД для загрузки данных
2. Написать скрипт загрузки данных upload.py
3. Создать из скрипта исполняемый файл upload.exe
4. Настроить макрос кнопки

Результат:
1. доработанный файл "названия точек.xlsm"
2. upload.py
3. upload.exe
