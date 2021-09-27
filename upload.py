
import psycopg2
import openpyxl
import sys


connection = psycopg2.connect(user="postgres",
                              # пароль, который указали при установке PostgreSQL
                              password="1254",
                              host="127.0.0.1",
                              port="5432",
                              database="TestEncost")
cursor = connection.cursor()
#python upload.py "C:/1.upload_names/названия точек.xlsm"
#sys.argv
file = openpyxl.open(sys.argv[1],read_only=True)
sheet = file.active

#print(sheet[1][1].value)
cursor.execute("""DELETE FROM endpoint_names""") # Удаляем старые данные
for row in range(2,sheet.max_row+1):
    id = sheet[row][0].value
    name = sheet[row][1].value
    # Загржаем новые
    cursor.execute("""INSERT INTO endpoint_names(endpoint_id,endpoint_name) VALUES (%s,%s)""", (id,name))
    connection.commit()

"""
     # Получить результат
    cursor.execute("SELECT * from endpoint_names")
    record = cursor.fetchall()
    print("Результат", record)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")"""