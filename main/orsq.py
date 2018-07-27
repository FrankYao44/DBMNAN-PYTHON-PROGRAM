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
import re
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
            repw=re.compile(r'^(\/w)\n((.*\n.*\n)+)$')                
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
        result=dict(zip(k,v))
        self.input_str=input_str
        self.key=key
        self.result=result
        
            
if __name__=='__main__':
    r=Cheaker('/w\nkey\nvalue\nkey2\nvalue2\n')
    print(r.key,r.result)
