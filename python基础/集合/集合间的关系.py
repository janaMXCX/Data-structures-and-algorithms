s={1,2,3,4,5}
s2={1,2,3,4,5}
print(s==s2)
print(s!=s2)
'''一个集合是否是另一个集合的子集'''
s1={10,20,30,40,50,60}
s3={10,20,30,40}
s4={10,20,90}
print(s3.insubset(s1))
print(s4.insubest(s1))
'''一个集合是否是另一个集合的超集'''
print(s1.issuperst(s2))
print(s1.issuperst(s3))

'''两个集合是否含有交集'''
print(s2.isdisjoint(s3))
s5={100,200,300}
print(s2.isdisjoint(s5))