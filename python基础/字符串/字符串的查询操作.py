s='hello,hello'
print(s.index('lo'))#3
print(s.find('lo'))#3
print(s.ridex('lo'))#9
print(s.rfind('lo'))#9

print(s.index('k'))#会报错
print(s.find('k'))#不会报错#-1
print(s.ridex('k'))#会报错
print(s.rfind('k'))#-1