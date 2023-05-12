collection = [10,20,30,40,50,60]
print(collection[:],
collection[3:5],
collection[-2:-5],
)
#added hiii
res = 40 in collection
print(res)
print(res = len(collection))
print(res = max(collection))
print(res = min(collection))
print(res = type(collection))
collection.append(500)
print(collection)
collection.extend([300,400])##
print(collection)
collection.insert(4,600)
print(collection)#
del collection[5]
print(collection)
res = collection.pop(1)
print(res)
collection.insert(1,res)
print(collection)
collection.remove(50)
print(collection)
res = collection.index(40)
print(res)
collection[res] = 100
print(collection)
collection.sort()
print(collection)
collection.reverse()
print(collection)
