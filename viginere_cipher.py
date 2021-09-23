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


#getting inputs from user
key = input("Enter the keyword: \n")
keylist = []
key1 = len(key)

plaintext = input("Enter your message: \n")
plaintext = plaintext.lower()

#removing additional characters
removeables = [".", ",", "?", "!", "/", " "]
for i in plaintext:
    if i in removeables:
        plaintext = plaintext.replace(i, "")


#pulling values for key
ptlist = []
for j in key:
    for k, v in dicti.items():
        if j == k:
            keylist.append(v[0])

#pulling values for plaintext
for p in plaintext:
    for k, v in dicti.items():
        if p == k:
            ptlist.append(v[0])


#making an additional list, to sync up with the message
plen = len(plaintext)
c = 0
keyed = []
nums = 0

while c < plen:
    keyed.append(keylist[nums])
    c+= 1
    nums += 1

    if nums == len(key):
        nums = 0

#Plaintext + Key values
pklist = []
for k in range(len(keyed)):
    pklist.append(keyed[k]+ ptlist[k])


#list of values for the cipher
modlist = []
for i in pklist:
    mod26 = i % 26
    modlist.append(mod26)

#creation of the cipher
cipher = ""
for i in modlist:
    for k, v in dicti.items():
        if (i == v[0]) or (i == v[1]):
            cipher += k
print("Ciphertext: " + cipher)



#Decryption

#Getting values for cipher minus key
decrypt = []
for c in range(len(modlist)):
    decrypt.append(modlist[c] - keyed[c])

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
    
