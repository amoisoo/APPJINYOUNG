import os
import pymysql
pymysql.install_as_MySQLdb()


import time

now = time.ctime()
slugtime = time.strftime("%Y-%m-%d-%H%M%S", time.strptime(now))
print(slugtime)