import pdb
pdb.set_trace()
class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age 
    def __str__(self):
        return f"my name is {self.name} and age is {self.age}"
    def __repr__(self)->str:
        return f"my name is repr method and age is"
emp=employee('ARun',18)
s=str(emp)
print(s) 