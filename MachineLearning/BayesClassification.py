#-*- coding:UTF-8 -*-
'''
Created on 2018年11月12日

@author: master
'''
import PreProcessData as pre
import numpy as np
import fenci
from sklearn.naive_bayes import MultinomialNB

def stopWord(path):
    temp= set()
    with open(path) as f:
        for line in f.readlines():
            line = line.replace('\n','')
            temp.add(line)
    return temp



def wordDic():
        stopword = stopWord('../MachineLearning/StopWord.txt')
        initlist = pre.getFileName('/Users/master/Desktop/证监会信息中心/基于知识图谱的智能问答/数据/data/question/', [])
        wordSet = set()
        files = [file  for file in initlist if '【' in file ]
        for file in files :
            label = pre.findNum(file)
            with open(file) as f:
                for line in f.readlines() :
                        line = line .replace("\n","")
                        seglist = fenci.fenci(line)
                        for seg in seglist:
                            word = seg.word.replace("\n","").encode('utf-8')
                            if word not in stopword:
                                wordSet.add(word)
        
        return wordSet            
                    
        
def preData():
    worddic = list(wordDic())
    
    cols = len(worddic)
    rows = 0
    with open('../MachineLearning/train.txt') as f :
        for line in f.readlines():
            rows = rows+1
    samples = np.zeros((rows,cols))
    labels = np.zeros((rows,1))
    with open('../MachineLearning/train.txt') as f :
        i = 0
        for line in f.readlines():
            line = line .replace("\n","")
            lineArray = line.split(" ")
            labels[i] = int(pre.findNum(lineArray[0]))
            i = i+1
    
    with open('../MachineLearning/train.txt') as f :
        i = 0
        for line in f.readlines():
            line = line.replace("\n","")
            lineArray = line.split(" ")
            j=0
            for word in lineArray:
                if word in worddic:
                    
                    samples[i,worddic.index(word)] = 1
            
            
            i = i+1
        np.set_printoptions(threshold='nan')
        return samples,labels   
        
def Bayes():
    samples,labels  = preData()
    clf = MultinomialNB(alpha=2.0)
    model = clf.fit(samples,labels)
    return  model
         
            

if __name__ == '__main__':
    
   Bayes()
        
            

        
    
    
      
        
    
    
