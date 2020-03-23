import re

result=re.findall(r'@(\w+.\w+.\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz, rodrigo@rodrigocordeiro.com.br')  
print result
