#DSA
sentence = input("enter a sentence")
words= sentence.split()
dict={}
for i in range (len(words)):
    dict[words[i]]=dict.get(words[i],0) + 1

count=max(dict,key=dict.get)

print ("The word that appeard most times is 🧐 : ", count)  #most time appeared
print ("THE total number of distinct words are 😎:",len(dict))      #  distinct number of words
print(words)
print(dict)