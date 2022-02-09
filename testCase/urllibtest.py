from urllib3 import request
res=request.RequestMethods().urlopen(method='GET',url='http://www.baidu.com')
print(res.read().decode())