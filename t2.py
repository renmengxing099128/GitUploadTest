#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月9日

@author: lei.wang
'''

def diff(listA,listB):
    #求交集的两种方式
    retA = [i for i in listA if i in listB]
    retB = list(set(listA).intersection(set(listB)))

    print ("retA is: ",retA)
    print ("retB is: ",retB)

    #求并集
    retC = list(set(listA).union(set(listB)))
    #print ("retC1 is: ",retC)

    #求差集，在B中但不在A中
    retD = list(set(listB).difference(set(listA)))
    print ("retD is: ",retD)

    retE = [i for i in listB if i not in listA]
    print ("retE is: ",retE)

def main():
    listA = [1,2,3,4,5]
    listB = [3,4,5,6,7]
    diff(listA,listB)

if __name__ == '__main__':
    main()
