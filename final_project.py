#coding:gbk
"""
�ԡ����������Ľֵ����ı��������ϵ����ȡ��������Gelphi����������ϵ���ӻ�
����:̸��
"""
import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}      # names����������ִ���
relationships = {}      #���������ϵ��
lineNames = []      #��������������ÿһ�ηִʵõ���ǰ���г��ֵ���������
jieba.load_userdict("character.txt")     #�Լ�����Ľ�ɫ��
with codecs.open("���������Ľֵ�.txt", "r", "utf-8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)
        lineNames.append([])            # Ϊ��������һ�������б�
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue        #�ж��Ƿ�Ϊ����
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:       #�����ﲻ���ֵ���ʱ
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1
for line in lineNames:      # �ж������ϵ�Ľ��̶ܳ�
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2]= 1
            else:
                relationships[name1][name2] = relationships[name1][name2]+ 1        #ͨ���ж�����֮���Ƿ������һ����������ϵ�̶�
with codecs.open("1.csv", "w", "gbk") as f:
    f.write("Id Label Weight\r\n")      #����һ��csv��ʽ�Ľڵ��ļ�
    for name, times in names.items():
        f.write(name + " " + name + " " + str(times) + "\r\n")
with codecs.open("2.csv", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")     #����һ��csv��ʽ�ı��ļ�
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")
