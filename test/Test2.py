#-*- coding:UTF-8 -*-
'''
Created on 2018年11月15日

@author: master
'''
import json
import sys
import os 
from spyder.widgets.findinfiles import FILE_PATH
reload(sys)
sys.setdefaultencoding( "utf-8" )
def cmp(src_data,dst_data,key):
    if isinstance(src_data, dict):
        """若为dict格式"""
        for key in dst_data:
            if key not in src_data:
                print("src不存在这个key"+key)
        for key in src_data:
            if key in dst_data:
                """递归"""
                cmp(src_data[key], dst_data[key],key)
            else:
                print("dst不存在这个key"+key)
    elif isinstance(src_data, list):
        """若为list格式"""
        if len(src_data) != len(dst_data):
            print(key+"list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
        for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
            """递归"""
            cmp(src_list, dst_list,key)
    else:
        if str(src_data) != str(dst_data):
            print(key+src_data)
            
def cmp2(src,other ,key):
    if isinstance(src, dict) :
        for key in other:
            if key not in src:
                print("src中不存在："+key)
        for key in src:
            if key in dict:
                cmp2(src[key], other[key], key)    
            else:
                print("other中不存在"+key)
    elif isinstance(src, list) :
        if len(src) != len(other) :
            print(key+"数组长度不一致")  
        for src_list,other_list in zip(sorted(src),sorted(other)):
            cmp(src_list,other_list, key)
    else:
        if str(src) != str(other):
            print(key+src)
    

def countJsonKey(src,path,countdit):
    if isinstance(src, dict) :
        for key in src:
            countJsonKey(src[key], path+[key], countdit)    
            
    elif isinstance(src, list) : 
        for (i, src_list) in enumerate(src):
            countJsonKey(src_list, path+[str(i)], countdit)
    else:
        countdit['.'.join(path)] =  str(src)
     

def listdir(path):
    listname = []
    for file in os.listdir(path):
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            listdir(filepath,listname)
        else:
            listname.append(filepath)
    
    return listname
    
            
    
    
    
    

   
    
    
'''
    dict1 = {"id": "503", "name": "班级优化", "info": {"uid":"2017","stuName":["李四"]}}
    dict2 = {"id": "503", "name": "班级优化2", "info": {"uid":"2017","stuName":["张三","赵五"]}}
    cmp(dict1, dict2,"")
'''    
    
            
if __name__ == '__main__':
    
    urlList = listdir('/Users/master/Desktop/证监会信息中心/数据大屏/NLP结果/达观抽取结果/output_company/')
    count = 0
    allTotal = 0
    allMissValuetotal=0
    for url in urlList:
        if '兰州银行股份有限公司' in url:
            continue 
        try:
            count= count+1  
            with open(url) as f:
                data = json.load(f)
            path = []
            countdit = {}
            countJsonKey(data,path,countdit)
            total = 0
            missValuetotal = 0
            for key in countdit :
                if countdit[key] == '' or countdit[key] == 'None' :
                    missValuetotal = missValuetotal+1
                total = total+1
            with open("/Users/master/Desktop/证监会信息中心/数据大屏/NLP结果/达观2.csv",'a+') as w:
                w.write(url+","+str(total)+","+str(missValuetotal)+"\n")
            allTotal = allTotal + total
            allMissValuetotal = allMissValuetotal + missValuetotal
        except Exception :
            print "error:"+url
    
    print count
    print allTotal
    print allMissValuetotal
    print round(allMissValuetotal/float(allTotal),3)
        
            
  
      

