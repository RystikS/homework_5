immutable_var = 1,2.5,"Hello",True,[0,1]
print(immutable_var)
immutable_var[0]=100
print(immutable_var) #кортеж относится к неизменяемым объектам
mutable_list = [1,2.5,"Hello", True,[0,1]]
mutable_list[0:4]=1,3,4,False
print(mutable_list)