empids={23,10,121,20,77,30,40,55}
# ids=empids.copy()
# print(empids)
# print(ids)
# print(ids.pop())
# print(ids.pop())
# print(ids.pop())
#ids.remove(121) #if the value is not present it will give an error

# ids.discard(222)
# print(ids)
# ids.clear()#to remove all the vallues
# #clear
# print(ids)
# empids1={130,540,525}
# print(empids1)
# empids1.add(84)
# print(empids1)
# empids.update(empids1)
# print(empids)

x={98,23,99,11,44,54,63}
y={29,78,64,31,12,63,92}

print(x.union(y))#x|y
print(x.intersection(y))#x&y
print(x.difference(y))#x-y