s='天涯共此时'
print(s.encode(encoding='GBK'))#在gbk这种编码格中 一个中文占两个字节
print(s.encode(encoding='UTF-8'))#在UTF-8这种编码格式中，一个中文占三个字节

#解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))