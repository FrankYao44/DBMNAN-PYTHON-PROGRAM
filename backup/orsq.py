#coding:utf-8
#orsq.py
'''
 this is a project which allow user run sql by input str
 programmer: Frank Yao 44
 main eof:
 /?\nkey\nvalue\n......
 for example: /w\ntable\nEnglish\nid\n1\nword\nmy
 /?:this is a v which show the action
 for:
 /n
'''
import re, sqlite3
class Cheaker(object):
    #this class can get a str,and turn it into Cheaker
    def __init__(self,input_str):
        
        def group(in_str):
            result=''
            for _ in in_str:
                if _=='\n':
                    yield result
                    result=''
                else:
                    result=result+_
        def cheakstr(input_str):
            repw=re.compile(r'^(\/\w)\n((.*\n.*\n)+)$')                
            restr=repw.match(input_str)
            if restr==None:
                raise ValueError
            key=restr.group(1)
            in_str=restr.group(2)
            return key , in_str
        che=cheakstr(input_str)
        key,in_str=che[0],che[1]
        ge=group(in_str)
        k,v,i=[],[],0
        while True:
            try:
                a=next(ge)
                i=i+1
                if i%2!=0:
                    k.append(a)
                else:v.append(a)
            except StopIteration:
                break
        dict_passage=dict(zip(k,v))
        self.tablename=dict_passage['table']
        dict_passage.pop('table')
        self.input_str=input_str
        self.key=key
        self.dict_passage=dict_passage
class Sqlcom(object):
    def __init__(self,cheaker):
        if not isinstance(cheaker,Cheaker):
            raise ValueError
        self.cheaker=cheaker
    def __sql_to_dict(self,sql_v):
        if isinstance(sql_v,tuple):
            sql_v=[].append(sql_v)
        k=self.cur.execute('PRAGMA table_info(%s)'%(self.cheaker.tablename))
        sql_k=[_[1] for _ in k]
        return list(map(lambda tv: dict(zip(sql_k,tv)),sql_v))
    def __writein(self):
        passage=self.cheaker.dict_passage
        tablename=self.cheaker.tablename

        #insert into tablename (key1,key2...) values(value1,value2...) 
        _exe,_cu,_te='insert into %s '%(tablename),'',''
        for k,v in passage.items():
            _cu=_cu+'%s,'%(k)
            _te=_te+'\'%s\','%(v)
        _execute='%s(%s) values(%s)'%(_exe,_cu[:-1],_te[:-1])
        self.cur.execute(_execute)
        return self.cur.rowcount
    def __createtable(self):
        passage=self.cheaker.dict_passage
        #create table tablename (key1 varchar(value1),key2 varchar(value2))
        _exe,_cute='create table %s'%(self.cheaker.tablename),''
        for k,v in passage.items():
            if 'p' in v:
                _cute=_cute+'%s varchar(%s) primary key,'%(k,v.strip('p'))
            else:
                _cute=_cute+'%s varchar(%s),'%(k,v)
        _execute='%s (%s)'%(_exe,_cute[:-1])
        self.cur.execute(_execute)
        return 1
    def __search(self):
        passage=self.cheaker.dict_passage
        # select * from tablename where key=? (value,)
        _exe,_cu,_te='select * from %s where'%(self.cheaker.tablename),'',[]
        for k,v in passage.items():
            _cu=_cu+' %s=? and'%(k)
            _te.append(v)
        _execu=_exe+_cu[:-3]
        self.cur.execute(_execu,_te)
        return self.__sql_to_dict(self.cur.fetchall())
    def __delete(self):
        passage=self.cheaker.dict_passage
        # select * from tablename where key=? (value,)
        _exe,_cu,_te='delete from %s where'%(self.cheaker.tablename),'',[]
        for k,v in passage.items():
            _cu=_cu+' %s=? and'%(k)
            _te.append(v)
        _execu=_exe+_cu[:-3]
        self.cur.execute(_execu,_te)
        return self.cur.rowcount
    def doing_sql(self):
        conn=sqlite3.connect('test.db')
        cur=conn.cursor()
        self.cur=cur
        try:
            key_dict={'/w':self.__writein,'/c':self.__createtable,'/s':self.__search,'/d':self.__delete}
            result=key_dict[self.cheaker.key]()
        finally:
            cur.close()
            conn.commit()
            conn.close()
        return result
        
if __name__=='__main__':
    #r=Cheaker('/c\ntable\nnnnuser\nid\n20\nname\n20\nsex\n1p\n')
    #Sqlcom(r).doing_sql()
    r=Cheaker('/w\ntable\nnnUser\nid\n\n\nsex\n9\n')
    #print(r.key,r.tablename,r.dict_passage)
    s=Sqlcom(r)
    s.doing_sql()
    r=Cheaker('/s\ntable\nnnUser\nname\n%s\n'%(None))
    print(Sqlcom(r).doing_sql())
