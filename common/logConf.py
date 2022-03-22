import logging
import logging.config
from util import get_path
import os

path=get_path.getPath()
con_log=os.path.join(path+'log.conf')
#读取配置文件
logging.config.fileConfig(con_log)
#创建一个日志器，logging=logging.getLogger('simpleExample'或者不填默认root)
logging=logging.getLogger()