#可以使用内置函数zip进行压缩
items=['hello','python','jana']
prices=[96,78,54]
d={items:prices for items,prices in zip(items,prices)}
print(d)
c={items.upper():prices for items,prices in zip(items,prices)}
print(c)
#再进行压缩的时候会以较短的的那个为基础进行压缩。