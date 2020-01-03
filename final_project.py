#coding:gbk
"""
对《黎明破晓的街道》文本中人物关系的提取，并利用Gelphi软件对人物关系可视化
作者:谈天
"""
import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}      # names保存人物出现次数
relationships = {}      #保存人物关系的
lineNames = []      #缓存变量，保存对每一段分词得到当前段中出现的人物名称
jieba.load_userdict("character.txt")     #自己输入的角色表
with codecs.open("黎明破晓的街道.txt", "r", "utf-8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)
        lineNames.append([])            # 为本段增加一个人物列表
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue        #判断是否为人物
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:       #当人物不在字典中时
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1
for line in lineNames:      # 判断人物关系的紧密程度
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2]= 1
            else:
                relationships[name1][name2] = relationships[name1][name2]+ 1        #通过判断名字之间是否出现在一行来计数关系程度
with codecs.open("1.csv", "w", "gbk") as f:
    f.write("Id Label Weight\r\n")      #生成一个csv格式的节点文件
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")
with codecs.open("2.csv", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")     #生成一个csv格式的边文件
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")
