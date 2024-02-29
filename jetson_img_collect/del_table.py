import pymysql
import mysql.connector
connection = mysql.connector.connect(host='localhost',database='kj',user='parkhs',password='qksckdrh09')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS go_img')
cursor.execute('DROP TABLE IF EXISTS no_img')