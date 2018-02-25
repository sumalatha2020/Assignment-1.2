l=[]  #An array

#loop through the given range to findout numbers divisible by 7 but not 5

for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

# print the output

print(','.join(l))