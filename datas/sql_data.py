# -*- coding:utf-8 -*-

from sshtunnel import SSHTunnelForwarder
import pymysql


class SSH(object):
    def __init__(self):
        self.server = SSHTunnelForwarder(
            ssh_address_or_host=('120.78.203.246', 22),
            ssh_username='root',
            ssh_password='',        # SSH_Password
            remote_bind_address=('', 3306)      # aliyun_address
        )
        self.server.start()


class MySql(SSH):
    def __init__(self):
        super(MySql, self).__init__()
        mysql_config = {
            'user': 'root',
            'password': '666',        # MySQL_Password
            'host': '127.0.0.1',
            'port': self.server.local_bind_port,
            'db': 'eos'
        }
        # 连接数据库
        self.connect = pymysql.connect(**mysql_config)
        self.cursor = self.connect.cursor()

    def get_parameter(self):
        # 查询并打印数据
        self.cursor.execute("SELECT sms.content FROM sms WHERE active_flag=0 AND type=0 LIMIT 1")
        msg = self.cursor.fetchone()[0]
        print(msg)
        self.connect.close()
        self.server.stop()


if __name__ == '__main__':
    x = MySql()
    x.get_parameter()
