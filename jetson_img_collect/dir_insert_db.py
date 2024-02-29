import pymysql
import mysql.connector
import os
def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(number, photo, go):
    if go ==True:
        create_table = 'create table IF NOT EXISTS free(id int auto_increment primary key, photo blob not null);'
        insert = """ INSERT INTO free (id, photo) VALUES (%s,%s)"""
    else :
        create_table = 'create table IF NOT EXISTS blocked(id int auto_increment primary key, photo blob not null);'
        insert = """ INSERT INTO blocked (id, photo) VALUES (%s,%s)"""
    try:
        connection = mysql.connector.connect(host='localhost',database='jetbot',user='parkhs',password='qksckdrh09')

        cursor = connection.cursor()
        cursor.execute(create_table)

        Picture = convertToBinaryData(photo)

        insert_blob = (number, Picture) 
        result = cursor.execute(insert, insert_blob) 

        connection.commit()
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

blocked_dir = 'dataset/blocked'
free_dir = 'dataset/free'

try:
    os.makedirs(free_dir)
    os.makedirs(blocked_dir)
except FileExistsError:
    print('Directories not created becasue they already exist')

go_dir = '/home/ddrawa/te/camera_data_collect/dataset/free'
no_dir = '/home/ddrawa/te/camera_data_collect/dataset/blocked'
 
go_list = os.listdir(go_dir)
no_list = os.listdir(no_dir)

for go_im in go_list:
    img_name = go_dir + '/' + go_im
    insertBLOB(None, img_name,True)
for no_im in no_list:
    img_name = no_dir + '/' + no_im
    insertBLOB(None, img_name,False)



    
