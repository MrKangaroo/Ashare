#!/usr/bin/evn python

import sys
import MySQLdb
import time
import warnings

warnings.filterwarnings("ignore")

class Insertion(object):
    
    default_charset = 'utf8'
    
    db_server_host = "10.2.4.31"
    db_user = "rd_dis_all"
    db_passwd = "edAOgKmF6yFMpFmM"

    
    db_name = "disconf"
    table_op_price = "env"

    def __init__(self):
        # 分页条数
        self.page_size = 100
        self.default_app_name = '' if len(sys.argv) == 1 else sys.argv[1] 


    # 比较逻辑
    def diff(self):
        # connection
        default_conn = MySQLdb.connect(
            host = self.db_server_host,
            user = self.db_user,
            passwd = self.db_passwd,
            db = self.db_name,
            charset = self.default_charset
        )

        # 游标
        default_cursor = default_conn.cursor()

        default_cursor.execute("select code, price from " + self.disconf_table_env)
        result_set = default_cursor.fetchall()
        for item in result_set:
            try:
                print("diff logic")
            except Exception as e:
                print(e)
                time.sleep(5)


    # 插入记录表
    def insert(self, code, price):
         # connection
        default_conn = MySQLdb.connect(
            host = self.db_server_host,
            user = self.db_user,
            passwd = self.db_passwd,
            db = self.db_name,
            charset = self.default_charset
        )

        # 游标
        default_cursor = default_conn.cursor()
        try:
            print("------开始插入------")
            missconf_insert_config_sql = "INSERT INTO `config` (`code`, `price`) VALUES (" + str(code) + "," + str(price) + "')"
            print("missconf_insert_config_sql:", missconf_insert_config_sql)
            default_cursor.execute(missconf_insert_config_sql)
            default_conn.commit()
        except Exception as e:
            print (e)
            time.sleep(5)
            default_cursor = default_conn.cursor()
        
        default_cursor.close()
        default_conn.close()

if __name__ == '__main__':
     configMigration = Insertion()
     configMigration.migrationConfig()