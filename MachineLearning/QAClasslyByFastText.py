#!/Users/master/anaconda2/bin/python
#-*- coding:UTF-8 -*-
'''
Created on 2018年11月8日

@author: master
'''
import fastText   

model = fastText.train_supervised("../MachineLearning/train.txt",wordNgrams=4,lr=0.00001,epoch=10000)
result = model.predict(u'电影  评分  多少', 2)
print result
