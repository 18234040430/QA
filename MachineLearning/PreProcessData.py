#!/Users/master/anaconda2/bin/python
#-*- coding:UTF-8 -*-
'''
Created on 2018年11月9日

@author: wyf
'''
import os
import re
import fenci

def getFileName(path,list_name):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            getFileName(file_path, list_name)  
        else:  
            list_name.append(file_path)
    
    return list_name 
    

def propessTrainData(path):
    initlist = getFileName(path, [])
    files = [file  for file in initlist if '【' in file ]
    for file in files :
        label = '__label__'+findNum(file)
        with open(file) as f:
            for line in f.readlines():
                seglist = fenci.fenci(line)
                temp = []
                for seg in seglist:
                    temp.append(seg.word)
                
                tempSentence = ' '.join(temp).encode('utf-8')
                sample = label+","+tempSentence
                
                with open('/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/train.txt','a+') as w:
                   
                    w.write(sample)
                 
                
                
    
def findNum(str):
    comp = re.compile('[0-9]\d*')
    list_str=comp.findall(str)
    return list_str[0] 

if __name__ == '__main__':

    a = propessTrainData('/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/data/question/')
    
    
