#DSA
want="yes"
sentence = input("enter a sentence")
words= sentence.split()
list=[]

total=0
dict={}
for i in range (len(words)):
    dict[words[i]]=dict.get(words[i],0) + 1

count=max(dict,key=dict.get)

for i in dict:
    b=dict[i]
    list.append(b)
for i in list:
    total=i+total
    #print(total)
    
while want=="yes":
    print("what u want to check")
    print ("press a for checking frequency of words")
    print ("press b for checking unique words")
    print ("press c for checking most appeared word")
    print("press d for checking total number of words")
    which=input("enter your option ")
    if which=='d':
        print("total number of words are",total)                 #total number of words
        want=input("do u want to check more (yes/no)")
    if which=='c':
        print ("The word that appeard most times is 🧐 : ", count)  #most time appeared
        want=input("do u want to check more (yes/no)")
    if which=='b':
        print ("THE total number of distinct words are 😎:",len(dict))  
        want=input("do u want to check more (yes/no)")    #  distinct number of words
    if which=='a':
        print(dict)
        want=input("do u want to check more (yes/no)")        #frequency


#print(words)
