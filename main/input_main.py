#coding:utf-8
#input_main.py
from sqor import Checker,Sqlcom
def I(_out):
    next(_out)
    while True:
        i=input('input an passage\n')
        _out.send(i)
def O():
    while True:
        i=yield None
        try:
            r=Sqlcom(Checker(i)).doing_sql()
            print(r)
        except Exception as e :
            print(repr(e))
out=O()
I(out)
