import re
from_file='C:/Users/aaa/Desktop/The Lily of the Valley - Honore de Balzac.txt'
in_file =open(from_file,'r')
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
list2={}.fromkeys(lists).keys()
print(list2)