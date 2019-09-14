#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:10:49 2019

@author: liujun
"""

import pandas as pd



class BasedLocation:
    def __init__(self,path=None,k=10,addr='朝阳区',type1='score',sort=False):
        self.filepath=path
        self.k=k
        self.addr=addr
        self.type=type1
        self.sort=sort
        self.data=self.load_data()
        
    def load_data(self): #加载数据
        data=pd.read_csv(self.filepath,header=0,sep=',',encoding='gbk')
        return data[data['addr']==self.addr] #取出要找的地域的数据
    
    def recommend(self):
        if self.type in ['score','comment_num','lowest_price','decoration_time','open_time']: #如果排序选项要求在这范围内
            data=self.data.sort_values(by=[self.type,'lowest_price'],ascending=self.sort)[:self.k] #按排序选项和最低价格倒序
            return dict(data.filter(items=['name',self.type]).values) #取前K推荐的名字和排序选项值打印
        elif self.type=='combine': #如果是综合
            data=self.data.filter(items=['name','score','comment_num','decoration_time','open_time','lowest_price'])
            data['decoration_time']=data['decoration_time'].apply(lambda x:int(x)-2018) #
            data['open_time']=data['open_time'].apply(lambda x:2018-int(x))
            for col in data.keys():
                if col !='name':
                    data[col]=(data[col]-data[col].min())/(data[col].max()-data[col].min()) #数据归一化
            data[self.type]=1*data['score']+2*data['comment_num']+0.5*data['decoration_time']+0.5*data['open_time']+1.5*data['lowest_price']
            #评分权重为1 ，评分数目权重为2，装修时间你和开业时间权重为0.5，最低价格为1.5
            data=data.sort_values(by=self.type,ascending=self.sort)[:self.k]
            return dict(data.filter(items=['name',self.type]).values)
                
                
if __name__=='__main__':
    path='hotel.csv'
    hotel_rec=BasedLocation(path,addr='丰台区',type1='combine',k=10,sort=False)
    result=hotel_rec.recommend()
    print(result)
    
                
            
            
        