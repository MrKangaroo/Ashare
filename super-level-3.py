import sys
import json,requests,datetime;      
import pandas as pd

class SuperLevel(object):

    stock_pool_hold = {'sh000001':'指数','sh601012':'隆基股份','sz300274':'阳光电源','sh600438':'通威股份','sh603098':'森特股份','sz002459':'晶澳股份','sz000762':'西藏矿业','hk01880':'中国中免','hk06610':'飞天云动', 'hk01810':'小米'}

    def get_price(self):    

        now = datetime.datetime.now()
        
        dataList = {}
        timeStemp = now.strftime("%d/%m/%Y %H:%M:%S")

        for code in self.stock_pool_hold:
            URL = f'http://qt.gtimg.cn/q=s_{code}'
            dstr = requests.get(URL).content.decode('gb2312')
            key = dstr.split('=')[0].split("_")[2]
            price = dstr.split('=')[1].replace('"','').split('~')[3]  
            priceArr = dataList[timeStemp] if (timeStemp in dataList) else {}
            priceArr[key] = price
            dataList[timeStemp] = priceArr

        dataArr = []
        for key in dataList:
            data = {}
            data['day'] = key
            for item in dataList[key]:
                itemKey = self.stock_pool_hold[item]
                data[itemKey] = dataList[key][item]
            dataArr.append(data)    

        dynamicColumns = []
        dynamicColumns.append('day')
        for code in self.stock_pool_hold:
            dynamicColumns.append(self.stock_pool_hold[code])


        pd.set_option('display.unicode.east_asian_width', True)
        pd.set_option('display.unicode.east_asian_width', True)
        df= pd.DataFrame(dataArr, columns = dynamicColumns)
        
        df.day=pd.to_datetime(df.day);    
        
        df.set_index(['day'], inplace=True);     
        
        df.index.name=''           
        
        return df  

    def stockDetail(self):
        df = self.get_price()
        print('super-level-2:\n', df)

if __name__ == "__main__":
    now = datetime.datetime.now()
    print(now)
    superLevel = SuperLevel()
    superLevel.stockDetail() 
    now = datetime.datetime.now()
    print(now)
