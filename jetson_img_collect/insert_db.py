import pymysql
import mysql.connector
import cv2
import os

# def convertToBinaryData(filename):
#     with open(filename, 'wb') as file:
#         file.write(filename)
#     with open(filename,'rb') as f:
#         binaryData = f.read()
#     return binaryData

def insertBLOB(number, photo, go):
    if go ==1:
        create_table = 'create table IF NOT EXISTS free(id int auto_increment primary key, photo blob not null);'
        insert = """ INSERT INTO free (photo) VALUES (%s)"""
    if go ==2 :
        create_table = 'create table IF NOT EXISTS t_left(id int auto_increment primary key, photo blob not null);'
        insert = """ INSERT INTO t_left (photo) VALUES (%s)"""
    if go ==3 :
        create_table = 'create table IF NOT EXISTS t_right(id int auto_increment primary key, photo blob not null);'
        insert = """ INSERT INTO t_right (photo) VALUES (%s)"""
    try:
        connection = mysql.connector.connect(host='localhost',database='jetbot',user='parkhs',password='qksckdrh09')

        cursor = connection.cursor()
        cursor.execute(create_table)

        Picture = cv2.imencode('.jpeg', photo)[1].tobytes()
        # Picture = convertToBinaryData(Picture)

        insert_blob = (Picture,) 
        result = cursor.execute(insert, insert_blob) 

        connection.commit()
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()


if __name__=='__main__':
    free_dir = 'dataset/free'
    left_dir = 'dataset/left'
    right_dir = 'dataset/right'

    try:
        os.makedirs(free_dir)
        os.makedirs(left_dir)
        os.makedirs(right_dir)
    except FileExistsError:
        print('Directories not created becasue they already exist')
    free_dir = 'dataset/free'
    left_dir = 'dataset/left'
    right_dir = 'dataset/right'
    # free_dir = '/home/ddrawa/te/camera_data_collect/dataset/free'
    # left_dir = '/home/ddrawa/te/camera_data_collect/dataset/blocked'
    # right_dir = '/home/ddrawa/te/camera_data_collect/dataset/blocked'
    
    free_list = os.listdir(free_dir)
    left_list = os.listdir(left_dir)
    right_list = os.listdir(right_dir)

    for free_im in free_list:
        img_name = free_dir + '/' + free_im
        insertBLOB(None, img_name,1)
    for left_im in left_list:
        img_name = left_dir + '/' + left_im
        insertBLOB(None, img_name,2)
    for right_im in right_list:
        img_name = right_dir + '/' + right_im
        insertBLOB(None, img_name,3)