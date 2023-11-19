class Student:
    native_place="吉林"
    def _int_(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("我的名字叫",self.name,"年龄是",self.age)


a=Student("张鑫帅",18)
print(a.name)