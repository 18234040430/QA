#!/Users/master/anaconda2/bin/python
#-*- coding:UTF-8 -*-
'''
Created on 2018年11月7日

@author: wyf
'''
import jieba
from jieba import analyse
import jieba.posseg as pseg
jieba.load_userdict("../fenci/MOVIEDIC.txt")
jieba.load_userdict("../fenci/GENREDIC.txt")
jieba.load_userdict("../fenci/PERSONDIC.txt")

def fenci(question):
    seg_list = pseg.cut(question)
    return seg_list



   
def getDic(input,output):
    with open(input,'rb') as f:
        for line in f.readlines():
            try:
                lineArrays = line.split(",")
                with open(output,'a+') as w:
                    if "" != lineArrays[3]:
                        moviename = lineArrays[4].replace(" ","+").replace("\n","")
                        w.write(moviename+" "+"9999"+" "+"person"+"\n")
                    
            except Exception,e:
                print e


if __name__ == '__main__':
    #getDic("/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/movie.csv", "/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/MOVIEDIC.txt")
    #getDic("/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/genre.csv", "/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/GENREDIC.txt")
    getDic("/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/person.csv", "/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/PERSONDIC.txt")
    
    
    
    
    a = fenci('李连杰演过花样年华么'.replace(" ","+"))
    for i in a:
        print i.word+","+i.flag
    
        