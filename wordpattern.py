#ascii a
a = 97

#creating list for characters
llist = []
while a < 123:
    llist.append(chr(a))
    a +=1

#getting string from user
keyword = input("Enter the string you would like to search: ")
keyword = keyword.lower()


#entering the file name and reading it, then adding it to a file
wordlist = input("Enter the filename: ")
txt = open(wordlist, 'r')
alpha = txt.readlines()



if keyword == "":
    print("Empty search string")



#uniq the empty list, to be filled with pattern matches
uniq = []



#stripping the \n character"
for o in range(len(alpha)):
    alpha[o] = alpha[o].strip('\n')


#loop through the word list, by each word
for i in alpha:
    dicti = {}


    #initialize an empty list, and lowercase the word.
    llist1 = []
    worded = i.lower()
    

    #loop each character through the string
    for k in worded:
        if k == "\n":
            break

    #if the specific character is not in the list, add it
        if k not in llist1:
            llist1.append(k)



    

    #make count 0, on each word
    count = 0

    #looping through the list, llist1
    for l in llist1:

        #for the dictionary, make the lists count
        dicti[llist1[count]] = llist[count]
        count += 1
    

    retstr = "" 

    #looping through worded
    for j in worded:
        for x in dicti.keys():
            if j == x:
                retstr += dicti[x]


    uniq.append(retstr)      



numlist = []
catch = ""

#looping through the words list and searching for the keyword match
for z in range(len(alpha)):
    if keyword == alpha[z]:
        numlist.append(z)

        #turning this variable into the corresponding letter pattern
        catch = uniq[z]


#if there is a match, add it to anslist
anslist = []
for zx in range(len(uniq)):
    if uniq[zx] == catch:
        anslist.append(alpha[zx])


#output
if catch != "":
    print("\nThere are " + str(len(anslist)) + " pattern matches for the keyword: "  + keyword)
    print("\nBelow are the pattern matches:")

    for i in anslist:
        print(i)

    print("\nThe word pattern for " + keyword + " is: " + catch +"\n")

else:
    print("word is not in file")


#for part 4, convert the numbers into letter patterns
#searching for specific ciphers and outputting the keywords
pattern_search = input("\nEnter a specific pattern or enter nothing to exit: \n")
for z in range(len(uniq)):
    if uniq[z] == pattern_search:
        print(alpha[z])

