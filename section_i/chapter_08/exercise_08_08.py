# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_08.py
@time: 2019-01-17 20:06

8-8 用户的专辑：
在为完成练习8-7编写的程序中，编写一个while循环，让用户输入一个专辑的歌手和名称。
获取这些信息后，使用它们来调用函数make_album()，并将创建的字典打印出来。
在这个while循环中，务必要提供退出途径

"""
album = {}


def make_album(singer_name, album_name, song_num=''):
    album['歌手'] = singer_name
    album['专辑'] = album_name
    if song_num:
        album['曲目'] = song_num
    return album


while True:
    singer_name = input("歌手：")
    if singer_name == 'quit':
        break
    album_name = input("专辑：")
    if album_name == 'quit':
        break
    print(make_album(singer_name, album_name))

