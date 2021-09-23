#Deciphering
cip = input("Enter your cipher: \n")
cip = cip.lower()

key = input("Enter the keyword: \n")
keylist = []
key1 = len(key)


dicti = dict()

#Matching viginere values to letters of alphabet
count = 0
a = 97
c = 0
while count < 26:
    newlist = []
    b = count

    newlist.append(b)
    newlist.append(c)
    dicti[chr(a)] = newlist

    if c == 0:
        c = c- 25
    else:
        c = -25 + b
    
    count += 1
    a+= 1


#pulling values for key
for j in key:
    for k, v in dicti.items():
        if j == k:
            keylist.append(v[0])



#pulling values for cipher
ciplist = []
for p in cip:
    for k, v in dicti.items():
        if p == k:
            ciplist.append(v[0])

print(ciplist)

#making an additional list, to sync up with the message
plen = len(cip)
c = 0
keyed = []
nums = 0

while c < plen:
    keyed.append(keylist[nums])
    c+= 1
    nums += 1

    if nums == len(key):
        nums = 0

print(keyed)

decrypt = []
for c in range(len(ciplist)):
    decrypt.append(ciplist[c] - keyed[c])


#getting the mod26 of C-K
newmodlist =[]
for d in decrypt:
    newmod = d % 26
    newmodlist.append(newmod)

#outputting the decrypted message
decrypted = ""
for i in newmodlist:
    for k, v in dicti.items():
        if (i == v[0]) or (i == v[1]):
            decrypted += k
print("Decrypted Message: " + decrypted)