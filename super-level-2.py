import requests

hk_sina_stock_list_url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData"
hk_sina_stock_dict_payload = {
    "page": "1",
    "num": "3000",
    "sort": "symbol",
    "asc": "1",
    "node": "qbgg_hk",
    "_s_r_a": "page"
}

def sina_hk_real():
    """
    新浪财经-港股的所有港股的实时行情数据
    http://vip.stock.finance.sina.com.cn/mkt/#qbgg_hk
    :return: 实时行情数据
    :rtype: []
    """
    res = requests.get(hk_sina_stock_list_url, params=hk_sina_stock_dict_payload)
    if res.status_code != 200:
        logging.error(f"sina_hk_real/status_code:{res.status_code}/text:{res.text}")
        return []
    else:
        try:
            data_json = res.json()
            """
            {'symbol': '00021',  # 港股代码
            'name': '大中华地产控股',  # 中文名称
            'engname': 'GREAT CHI PPT',  # 英文名称
            'tradetype': 'EQTY',  # 交易类型
            'lasttrade': '0.000',  # 最新价
            'prevclose': '0.118',  # 前一个交易日收盘价
            'open': '0.000',  # 开盘价
            'high': '0.000',  # 最高价
            'low': '0.000',  # 最低价
            'volume': '0',  # 成交量(万)
            'currentvolume': '0',  # 每手股数
            'amount': '0',  # 成交额(万)
            'ticktime': '2022-04-08 10:54:17',  # 当前数据时间戳
            'buy': '0.115',  # 买一
            'sell': '0.120',  # 卖一
            'high_52week': '0.247',  # 52周最高价
            'low_52week': '0.110',  # 52周最低价
            'eps': '-0.003',   # 每股收益
            'dividend': None,   # 股息
            'stocks_sum': '3975233406', 
            'pricechange': '0.000',  # 涨跌额
            'changepercent': '0.0000000',  # 涨跌幅
            'market_value': '0.000',  # 港股市值
            'pe_ratio': '0.0000000'
            }
            """
        except Exception as e:
            logging.error(f"sina_hk_real/error: res.json()/detail:{e.__str__()}")
            return []
        res = [
            {"stock_code": d["symbol"],
             "name": d["name"],
             "eng_name": d["engname"],
             "date": d["ticktime"][:10],
             "time": d["ticktime"][11:],
             "now": float(d["lasttrade"]),
             "open": float(d["open"]),
             "close": float(d["prevclose"]),
             "high": float(d["high"]),
             "low": float(d["low"]),
             "volume": float(d["amount"]) * 10000,
             "turnover": float(d["volume"]) * 10000,
             "buy": float(d["buy"]),
             "sell": float(d["sell"]),
             "change": float(d["pricechange"]),
             "change_rate": float(d["changepercent"]),
             "stock_type": "hk"}
            for d in data_json
        ]
    return res