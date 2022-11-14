import sys
import json,requests,datetime;      
import pandas as pd

class SuperLevel(object):

    stock_pool_hold = {'sh000001':'指数','sh601012':'隆基股份','sz300274':'阳光电源','sh600438':'通威股份','sh603098':'森特股份','sz002459':'晶澳股份','sz000762':'西藏矿业'}
    # stock_pool_hold_name = ['隆基股份','阳光电源','通威股份','森特股份','晶澳股份','西藏矿业']


    def get_price(self, end_date='',count=10, frequency='1d', fields=[]):  
        if  frequency in ['1m','5m','15m','30m','60m']:  
            try:    
                return self.get_price_sina(end_date=end_date,count=count,frequency=frequency) 
            except: 
                return self.get_price_sina(end_date=end_date,count=count,frequency=frequency)

    def get_price_sina(self, end_date='', count=10, frequency='60m'):    
        
        frequency=frequency.replace('1d','240m').replace('1w','1200m').replace('1M','7200m');   mcount=count
        
        ts=int(frequency[:-1]) if frequency[:-1].isdigit() else 1       
        
        if (end_date!='') & (frequency in ['240m','1200m','7200m']): 
            end_date=pd.to_datetime(end_date) if not isinstance(end_date,datetime.date) else end_date    
            unit=4 if frequency=='1200m' else 29 if frequency=='7200m' else 1    
            count=count+(datetime.datetime.now()-end_date).days//unit               

        dataList = {}
        for code in self.stock_pool_hold:
            
            xcode = code.replace('.XSHG','').replace('.XSHE','')                      
            
            xcode = 'sh'+xcode if ('XSHG' in code)  else  'sz'+xcode  if ('XSHE' in code)  else code     
            
            URL = f'http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol={code}&scale={ts}&ma=5&datalen={count}'
            dstr = json.loads(requests.get(URL).content);

            for key in dstr:
                timeStemp = key['day']
                closePrice = key['close']
                priceArr = dataList[timeStemp] if (timeStemp in dataList) else {}
                priceArr[code] = closePrice
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

    def stockDetail(self, v1, v2):
        df = self.get_price(frequency=v1,count=v2)
        print('super-level:\n', df)



if __name__ == "__main__":
    frequency = sys.argv[1] if(len(sys.argv) > 1 ) else '5'
    count = sys.argv[2] if(len(sys.argv) > 2) else 10
    superLevel = SuperLevel()
    superLevel.stockDetail(frequency+'m', count) 
