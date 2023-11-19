#字符串的替换操作replace()
s='hello,python'
print(s.replace('python','java'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))
lst=['hello','java','python']

print('|'.join(lst))
print(''.join(lst))

t=('hello','java','python')
print(''.join(t))

print('*'.join('python'))