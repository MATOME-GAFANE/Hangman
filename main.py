# with open('/Users/matome/Desktop/words.txt', "r") as word_list:
#     words = word_list.read().split(' ')
#print(words)

import random
liste = []
with open('/Users/matome/Desktop/words.txt') as fa:
    lines = fa.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            liste.append(word)
print(liste)


number=random.randint(0,1001)
print(number)

print(liste[number])


word1=liste[number]
selected=word1

word1=word1.replace(word1[0],"_")
word1=word1.replace(word1[1],"_")


print(word1)
print(selected)


print (f"Try complete word {word1} : ")


print("   _____ \n"
      "  |      \n"
      "  |      \n"
      "  |      \n"
      "  |      \n"
      "  |      \n"
      "  |      \n"
      "__|__\n")

user=input("Enter a letter to complete word")

if(user==selected[0]):
    word1=word1.replace(word1[0],user)
    print("Correct")
    print(word1)
elif(user==selected[1]):
    word1=word1.replace(word1[1], user)
    print("Correct")
    print(word1)

elif(user!=selected[0] and user!=selected[1]):

    print("   _____ \n"
          "  |     | \n"
          "  |      \n"
          "  |      \n"
          "  |      \n"
          "  |      \n"
          "  |      \n"
          "__|__\n")



