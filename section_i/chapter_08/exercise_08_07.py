# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_07.py
@time: 2019-01-17 19:55

8-7 专辑：
编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，
以核实字典正确地存储了专辑的信息。

给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。
如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。
调用这个函数，并至少在一次调用中指定专辑包含的歌曲数

"""
album = {}


def make_album(singer_name, album_name, song_num=''):
    album['歌手'] = singer_name
    album['专辑'] = album_name
    if song_num:
        album['曲目'] = song_num
    return album


print(make_album('Jay', '叶惠美'))
print(make_album('Jay', '七里香'))
print(make_album('Jay', '周杰伦的床边故事', '10'))
