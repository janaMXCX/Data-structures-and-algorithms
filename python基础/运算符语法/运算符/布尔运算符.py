#对于布尔值之间的运算
a,b=1,2
print("------and 表示并且的意思-------")
print(a==1 and b==2)#True   True and True-->True
print(a==1 and b<2) #False  True and False-->False
print(a!=1 and b==2)#False  False and True-->False
print(a!=1 and b!=2)#False  False and False-->False
print("-----or 表示或者的意思-----")
print("------and 表示并且的意思-------")
print(a==1 or b==2)#True   True or True-->True
print(a==1 or b<2) #True  True or False-->True
print(a!=1 or b==2)#True  False or True-->True
print(a!=1 or b!=2)#False  False or False-->False
print("-----not 对bool类型操作数取反-----")
f=True
f1=False
print(not f)
print(not f1)
print('-----in与not in-----')
s="hellow word"
print('w'in s)
print('k'in s)
print('k'not in s)
print('w'not in s)