import re
from_file='C:/Users/Guuidea001/Desktop/The Lily of the Valley - Honore de Balzac.txt'
with open(from_file,'r') as in_file:
	lines=in_file.read(1000)
	lists=re.split('\W+',lines)
#lists.sort();
#print(lists)
#a=lists.sort()
#print(x)
'''
#使用set集合的方法去重
List_set = list(set(lists))
#Lists_l=list(List_set)
#使用list的方法排序
List_set.sort();
for item in List_set:
		word=("%s %d" %(item,lists.count(item)))
		print(word)
		'''
'''
with open("C:/Users/aaa/Desktop/data.txt","w") as out_file:
	
		#print(word)

	out_file.writelines(word)
	out_file.close()
print("finish!")
'''

#print(lists)
#使用dict字典的方法去重
dict1={}.fromkeys(lists)
#print(dict1)
#使用dict字典的方法排序
sorted_dict=sorted(dict1);
#print(sorted_dict)

with open("C:/Users/Guuidea001/Desktop/data.txt","w") as out_file:
	#out_file.write('Character  Count  ')
	for item in sorted_dict:
			dict1[item]=lists.count(item)
#			word=("%s %d \n" %(item,lists.count(item)))
			#word=word+"\n"
			
			#out_file.write(dict1)
dict2=dict(sorted(dict1.items(),key=lambda item:item[1],reverse=True))
#print(str(dict2))

#out_file.write(str(dict2))
	for key,value in dict2.items():
		word=('{Character}:{Count}'.format(Character=key,Count=value))
		out_file.write(word)
	#print(word)
#print(dict2)	
out_file.close()
print('finish！')
#print(sorted_dict)
