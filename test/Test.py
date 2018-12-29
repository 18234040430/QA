#!/Users/master/anaconda2/bin/python
#-*- coding:UTF-8 -*-
'''
Created on 2018年11月9日

@author: master
'''
import re

if __name__ == '__main__':
    bbd = []
    with open('../test/bbd拟上市公司列表.txt') as f :
       for line in  f.readlines():
          bbd.append(line.replace("\n",""))
    our = [] 
    with open('../test/招股书列表.txt') as f :
        for line in f.readlines():
            print line
            our.append(line)
    i = 0
    for bbd_name in bbd :
        flag = True
        for our_name in our:

            if bbd_name in our_name:    
                flag = False
                i= i+1
                break
         
        if flag:
            print bbd_name
             
    
     