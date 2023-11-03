# tasks with list

# 1. 
ls = ["kamal", 'chanda', 'durga', "somil", "prince"]
# get the following name form the list
# kamal
# chanda
# prince

print(ls)
print(ls[0])
print(ls[1])
print(ls[-1])
print(ls[4])
print(len(ls))

for i in ls:
    if len(ls) == 4:
        print("len of the list is {}".format(len(ls)))
        break
else:
    print("sorry not equal")
        
# check the len of the list if len of the list is 5 then print the index 1 from the list else print list

if len(ls) == 4:
    print(ls[1])

else:
    print(ls)