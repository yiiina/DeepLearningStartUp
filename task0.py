#coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")    
import re
from collections import Counter
from zhon.hanzi import punctuation

content=open("happiness_seg.txt","r").read().decode("utf-8") 

words=re.sub(ur"[%s]+"%punctuation,"",content.decode("utf-8"))

list_one=words.split(" ")

list_two=[]

for i in range(0,len(list_one)-1):
	if len(list_one[i])>=1 and len(list_one[i+1])>=1:
		two_words=list_one[i]+list_one[i+1]
		list_two.append(two_words)

top_ten=Counter(list_two).most_common(10)
for top in top_ten:
	for word_count in top:
		print word_count