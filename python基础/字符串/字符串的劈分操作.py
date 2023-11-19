s='hello word python'
print(s.split())#从左边开始劈分，默认劈分字符是空格字符串，返回的值是一个列表
lst=s.split()
print(lst)
s1='hello|word|python'
print(s1.split(sep='|'))#使用sep指定分隔符号
#通过参数 maxsplit 指定劈分字符串时的最大劈分次数，在经过最大劈分次数之后，剩余字串会单独作为一部分。
print(s1.split(sep='|',maxsplit=1))

#rsplit()操作与上边相同只是从右边进行分割。