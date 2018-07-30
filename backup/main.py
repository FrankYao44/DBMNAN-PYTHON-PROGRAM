#coding:utf-8
#main.py
import rom_sqlite
import display
import sqlite3
import re, time
import logging
R_M=re.compile(r'^(\/\w)(.{0,1023})(\@\@)|.(.{0,1023})(\@\@)|.(.{0,1023})(\@\@)|.(.{0,1023})$')
#R_A=re.compile(r'^(\/\w)(.{1,32}(.{0,1023}))$')
def cheaker(words):
    def catchkeys(words):
        c=R_M.match(words)
        if c==None:
            print('there are wrong words for %s'%('words'))
            return 0
        key=c.group(1)
        passage=c.group(2)
        return key,passage
    def checkkeys(key):
        keyslist=['/w','/r','/t','/g','/s','/i']
        if not key in keyslist:
            print('there are wrong keys:%s for %s'%(key,'keys'))
            return 0
    a=catchkeys(words)
    if a==0:return 0
    b=checkkeys(a[0])
    if b==0:return 0
    return a        
def inputer(w):
    w.send(None)
    while True:
        a=input("please input words:")
        result=cheaker(a)
        if result!=0:
            r=w.send(result)        
def writein():
    while True:
        result=yield 0
        key=result[0]
        passage=result[1]
        if key=='/r':
            pass
        elif key=='/t':
            pass
        else:
            pass

if __name__=='__main__':
    w=writein()
    inputer(w)
        
    
    
    
    
    
