from  Ashare import *
    
df=get_price('sh000001',frequency='1d',count=10)     
print('上证\n',df)

df=get_price('sh601012',frequency='1d',count=10)
print('LONGJI\n',df)

df=get_price('sh600438',frequency='1d',count=10)
print('TONGWEI\n',df)

df=get_price('sz300274',frequency='1d',count=10)
print('sunshine\n',df)