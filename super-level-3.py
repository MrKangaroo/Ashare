import sys
import json,requests,datetime;      
import pandas as pd

class SuperLevel(object):

    stock_pool_hold = {'01880':'中国中免','06610':'飞天云动', '01810':'小米'}

    def get_price(self):    
        
        for code in self.stock_pool_hold:
            
            URL = f'http://qt.gtimg.cn/q=s_hk{code}'

            dstr = requests.get(URL).content.decode('gb2312')
            
            info = dstr.split('=')[1].replace('"','')          
            print(info.split('~')[1], info.split('~')[3])

    def stockDetail(self):
        df = self.get_price()

if __name__ == "__main__":
    superLevel = SuperLevel()
    superLevel.stockDetail() 
