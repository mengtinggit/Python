import re
from_file='C:/Users/Guuidea001/Desktop/The Lily of the Valley - Honore de Balzac.txt'
#打开文件
with open(from_file,'r') as in_file:
	#读取文件内容
	lines=in_file.read()
	#取出单词
	lists=re.split('\W+',lines)

#取出lists的值作为dict的key
dict1={}.fromkeys(lists)
#使用dict字典的方法排序，去重
sorted_dict=sorted(dict1);

#新建输出文件
with open("C:/Users/Guuidea001/Desktop/data.txt","w") as out_file:
	#统计出lists内所有单词出现的次数
	for item in sorted_dict:
			dict1[item]=lists.count(item)
	#将dict按value值从大到小排序
	dict2=dict(sorted(dict1.items(),key=lambda item:item[1],reverse=True))
	#将dict输出为字符串格式
	for key,value in dict2.items():
		word=('{Character} : {Count}\n'.format(Character=key,Count=value))
		#写入文件
		out_file.write(word)
#关闭文件
out_file.close()
print('finish！')
