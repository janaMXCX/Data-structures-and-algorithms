s='hello,python'
print('1.',s.isidentifier())#判断字符串是否为合法字符串#False
print('hello'.isidentifier())
print('张三'.isidentifier())
print('张三_123'.isidentifier())

print('\t'.isspace())#判断指定字符串，是否全部由空白字符串组成(回车，空格，水平制表符)


print('abc'.isalpha())#判断指定字符串是否全部由字母组成

print('123'.isdecimal())#判断字符串是否全部由十进制数字组成
print('123四'.isdecimal())

print('123'.isnumeric())#判断字符串是否全部由数字组成
print('123四'.isnumeric())

print('abc1'.isalnum())#Ture#判断字符串是否全部由字母和数字组成。
print('张三123'.isalnum())#Ture




