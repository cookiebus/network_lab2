# -*- coding: utf-8 -*-  
import os, os.path, sys

reload(sys) 
sys.setdefaultencoding('utf-8')

PICPATH = '/home/cmh/project/network_lab2/pictures'
"""
f = open("/home/cmh/project/network_lab2/pictures/农学家/\xe6\x9d\x8e\xe6\x96\x87\xe5\x8d\x8e.jpg", "r")
print f.read()
exit(0)
"""
#upath = ("home/cmh/project/network_lab2/pictures/游戏和动漫行业/游戏 动漫高层/陈天桥.jpg").decode('gbk').encode("utf-8")
#f = open(upath, "r")
def insert(name, major, url, path):
    print name, major, url, path

for parent,dirnames,filenames in os.walk(PICPATH):
    if 'name.txt' in filenames:
        major = parent[parent.find("pictures/") + 9:]
        major = major[:major.find('/')]
        #print parent, filenames
        file = open(parent + "/name.txt", "r")
        while 1:
            line = file.readline()
            if not line:
                break
            if not ' ' in line:
                continue
            params = line.split(" ")
            name = params[0]
            url = params[1]
            for p, d, f in os.walk(parent):
                for ff in f:
                    if ff != 'name.txt':
                        path = p + '/' +  ff
                        t = (name + '.jpg').find(ff) != -1
                        if t:
                            insert(name, major, url, path)
                        else:
                            t = (name + '-1.jpg').find(ff) != -1
                            if t:
                                insert(name, major, url, path)

        file.close()
