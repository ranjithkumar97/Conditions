list=["rajnith","kumar","santhosh"]
print(list)

print(list[2]) #by using index value
list[2]="hehehe"
print(list)   #by change santhosh


list.append("santhosh")
print(list) #by adding last case

print(len(list)) #length of the list

del list[2]
print(list) #del the 2nd index

name=['rajnith', 'kumar', 'santhosh']
x=name.count('rajnith')
print(x)


tuple=("hello","world","2k19")
x=tuple.count("hello")
print(x) #tuple count

print("hello" in  tuple)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)#when remove fail use discard