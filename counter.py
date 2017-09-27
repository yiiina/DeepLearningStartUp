#coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")    # 防止Unicode编码报错
import re
from collections import Counter
from zhon.hanzi import punctuation

initial_input=open("happiness_seg.txt", "r").read().decode("utf-8")    # 读取文件
string = re.sub(ur"[%s]+" %punctuation, "", initial_input.decode("utf-8"))    # 正则匹配中文标点符并剔除
initial_list=string.split(" ")    # 将文章生成初始列表，空格划分各个元素
#print initial_list

standard_list=[]    # 初始化最终的列表

for i in range(0, len(initial_list)-1):
	if(len(initial_list[i])>=1 and len(initial_list[i+1])>=1):    # 判断相邻两元素长度均不小于1
		doublewords=initial_list[i]+initial_list[i+1]
		standard_list.append(doublewords)
		
counter=Counter(standard_list).most_common(10)    # Counter的内置函数挑选出频次最高的10个
for element in counter:    # 打印
	for word_count in element:
		print word_count
