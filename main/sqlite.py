#sqlite.py
#coding:utf-8
import sqlite3, os, pickle      
class sqlite_(object):
    def __init__(self,key,passege):
        with open('dict_info.txt','rb') as f:
            d=pickle.load(f)
        conn=sqlite3.connect('mnandb.db')
        cur=conn.cursor()
        #pickle d ,it's a dict.there are os.path, table key list
        self.d=d
        self.key=key
        self.passege=passege
        self.cur=cur
    def newkey(self,name,*keys):
        d=self.d
        tablekeyl=d['tablekeylist']
        if name in tablekeyl:
            print('keys are already here')
            return 0
        _execute='id varchar(20) primary key, '+' varchar(255), '.join(keys)+' varchar(255)'
        self.cur.execute('create table %s (%s)'%(name,_execute))
        d['tablekeylist'].append(name)
        with open('dict_info.txt','wb') as f:
            f.truncate()
            d=pickle.dump(d,f)
        
if __name__=="__main__":
    a=sqlite_('a','aaa')
    a.newkey('cxasssaaa','bbb')
        
        
        
