"""
#Print each name and its index from a list of names.


names = ["Alice", "Bob", "Charlie"]
for i in names:
    print(f"{i}, {names.index(i)}")

for i, name in enumerate(names):
    print (f"{i},{name}")


#Filter numbers greater than 10 from a list using a lambda function.
nums = [4, 15, 8, 23, 7]
numsGt10 = list(filter(lambda i:i>10, nums))
print(numsGt10)
b = [i for i in nums if i> 10]
print(b)


#Count the number of vowels in a string.
text = "Hello World"
lstTxt = list(text)
vowLst = list('aeiouAEIOU')
cnt = sum(1 for i in lstTxt if i in vowLst)
print(cnt)


# Filter out people aged above 18 from a list of tuples.
people = [("Alice", 25), ("Bob", 17), ("Charlie", 19)]
adults =[]
for i, j in people:
    if j > 18:
        adults.append((i,j))
print(adults)


#Create a dictionary where keys are numbers from 1 to 10 and values are their squares.
dic = {}
for i in range(1, 11):
    dic[i]=i*i

dic1={x: x**3 for x in range(1, 11)}
print(dic)
print(dic1)


#Find common elements between two sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {x for x in set1 if x in set2}
#set3 = set1 & set2
print(set3)


from pyspark.sql.functions import count

#Count the number of lines, words in a text file.
with open("C:\\Users\\Prabhath\\Desktop\\Lak_op.txt", "r") as file:
    lines = file.readlines();
    lns = len(lines)
    chs = sum(len(line) for line in lines)
    wrds = sum(len(line.split(' ')) for line in lines)
    print(lns,chs,wrds)


#Write the multiplication table of a number into a file.
with open("C:\\Users\\Prabhath\\Desktop\\Lak_op_mul.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"5 * {i} = {5*i}\n")



# Generate the multiplication table for numbers 1 to 5. (nested loop)
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}\n")
    print("-----------")


#Count the frequency of each character in a string and save it to a file.
text = "Hello World"
chDict = {}
for ch in text:
    if ch.isalpha():
        chDict[ch] = text.count(ch)
# print(chDict)
with open("C:\\Users\\Prabhath\\Desktop\\Lak_op_mul.txt", "a") as file:
    for item in chDict.items():
        file.write(f"{item[0]} --> {item[1]}\n")
print("File updated successfully")

#Create a dictionary with student names as keys and another dictionary for subject marks. Calculate the average marks of each student.
students = {
    "Alice": {"Math": 85, "Science": 90, "English": 88},
    "Bob": {"Math": 78, "Science": 82, "English": 84},
    "Charlie": {"Math": 92, "Science": 88, "English": 91},
}

for student, marks in students.items():
    avg = sum(marks.values())/len(marks)
    print(f"{student} - {avg:.2f}")

from logging import exception

#Open a file, append a string, and handle exceptions.
try:
    with open("C:\\Users\\Prabhath\\Desktop\\Lak_op_mul.txt", "a") as file:
        file.write("This is appending with exceptions")
except FileNotFoundError:
    print("File does not exist")
except IOError:
    print("Could not write into the file")
except Exception as e:
    print(e)

"""
#Filter words longer than 5 characters using filter and lambda (anonymous func)
words = ["apple", "banana", "fig", "watermelon"]
lst = list(filter(lambda word: len(str(word)) > 5,  words))
print(lst)
lst1 = list(map(lambda word: len(str(word)),  words))
print(lst1)