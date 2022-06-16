import zipfile as zf
import os
import sys
import shutil
import re

desktop = 'C:/Users/Programmer/Desktop/'
path_dir = desktop + '소설 폴더/'
path_zip = desktop + '새 폴더/'

def zipFolderMove():
    for i in os.listdir(path_dir):
        path = path_dir + i
        for f in os.listdir(path):
            print(f)
def FolderRename():
    templist = list()
    for i in range(1, 27):
        path = path_dir + str(i)
        name = os.listdir(path)[0].split('.')[0]
        name = re.sub('~|\,|\.|0|1|2|3|4|5|6|7|8|9|!|@|#|$|%|^|&|\(|\)|_|-|=|\[|\]|\{|\}|\+|\*', "", name)
        name.strip()
        if len(name) == 0:
            name = str(i)
        elif name == "img":
            name = "img" + str(i)
        elif name in templist:
            name = name + str(i)
        templist.append(name)
        os.rename(path, path_dir+name)
def num_there(s):
    return any(i.isdigit() for i in s)
def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")
def FolderMakeMove():
    for i in os.listdir(path_zip):
        t = re.sub('[0123456789]', "", i).strip().split('.')[0].split(' ')[0]
        shutil.move(path_zip+i,"C:/Users/Programmer/Desktop/1/"+t)
        print(i)
def ZipFileCreate():
    for F in os.listdir(path_dir):
        p = path_dir+F+'/'
        for f in os.listdir(p):
            p2 = p + f
            try:
                shutil.make_archive(p2, "zip", p2)
                shutil.rmtree(p2)
            except:
                print(p2, "오류")
        print(p,"완료")
ZipFileCreate()
def t():
    t = set()
    for F in os.listdir(path_dir):
        p = path_dir+F+'/'
        for f in os.listdir(p):
            if len(f.split('.')) >= 2:
                t.add(F)
    for i in t:
        print(i)
        shutil.move(path_dir+i, path_zip)