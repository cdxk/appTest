import logging.config
from config import get_path
import os

path= get_path.getPath()
print(path)
con_log=os.path.join(path+'config\log.conf')
print(con_log)
#读取配置文件
logging.config.fileConfig(con_log)
#创建一个日志器，logging=logging.getLogger('simpleExample'或者不填默认root)
logging=logging.getLogger()
logging.info('test')