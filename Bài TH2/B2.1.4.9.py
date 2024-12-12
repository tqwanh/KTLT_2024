str=input("Enter a sting:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] +=1
    else:
        dict[n] = 1
print (dict)        
print("Tran Quang Anh, 235752021610095")
