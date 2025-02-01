"""
#To reverse the string
str = input('Enter a string: ')
print(str[::-1])
print(id(str), str[::-1], id(str[::]))

#Print max and sum of the elements in the list
l1 = list(range(1, 11))
print(f"{l1} - {max(l1)} - {min(l1)} - {sum(l1)} - {len(l1)}")

#Print number of vowels
str1 = 'tEst strIng'
vow_lst = list('aeiou')
print(vow_lst)
vow_cnt = 0
con_cnt = 0
for i in str1:
    if i in vow_lst:
        vow_cnt+=1
    elif i == ' ':
        continue
    else:
        con_cnt+=1
print(f"Vowel count: {vow_cnt} and Consonant count: {con_cnt}")

#Remove duplicate elements from the list
lst = [10, 20, 30, 40, 10, 50]
print(list(set(lst)))

#To print list of squares
lst1 = [i*i for i in lst if i < 40]
print(lst1)


#Filter numbers divisible by 3
numbers = [10, 20, 30, 40, 10, 50, 33, 99]
numBy3 = []
numBy3.extend(i for i in numbers if i%3==0)
print(numBy3)

#count the number of occurances of each character
str = input("Enter a string: ")
setChar = list(set(str))
print(setChar)
dict1 = {}
for ch in setChar:
    if ch.isalpha():
        dict1[ch] = str.count(ch)
print(dict1)


#Count the number of words in a given sentence
string = "Wish you a happy birthday"
wrds = len(str.split(' '))
print(wrds)



#To print all even numbers from 1 to 50
lst = list(range(1, 51))
evn = []
for i in lst:
    if i % 2 == 0:
        evn.append(i)
print(evn)


#Check if a number is positive, negative or zero
num = input("Enter a number: ")
if int(num) > 0:
    print(f"{num} is positive")
elif int(num) < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

import os

# To read the contents of a file named example.txt and print it
with open("C:\\Users\\Prabhath\\Desktop\\test.txt", "r") as file:
    cont = file.read()
    print(cont)


#To write the contents to a file from the list
lst = ['Today','tomorrow','yesterday']
with open("C:\\Users\\Prabhath\\Desktop\\Lak_op.txt", "w") as file:
    for i in lst:
        file.write(str(i) + '\n')
print('Written successfully')



#to extract characters from index 7 to the end.
st = 'Sahasra Sarayu'
print(st[7:])

#to extract characters from start to 5
st = 'Sahasra Sarayu'
print(st[:5])

# to extract every second character from a given string starting from the second character.
st = 'Sahasra Sarayu'
print(st[1::2])


with open("C:\\Users\\Prabhath\\Desktop\\test.txt", "r") as file:
    while True:
        cont = file.readline()
        if not cont:
            break
        print(cont.strip())
"""
with open("C:\\Users\\Prabhath\\Desktop\\Lak_op.txt", "r") as file:
    # file.seek(10)
    # cont = file.read(10)
    while cont := file.read(10):
        print("-------------")
        print(cont)
        # cont = file.read(10)
