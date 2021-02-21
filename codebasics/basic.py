print("Hello World")

# variables
rent=5000
travel=2000

print("Monthly Rent = ",rent)
print("Travel = ",travel)

total=rent+travel

print("Total Expense = ",total)

# numbers
del_mum=654
mum_blr=423
total_distance=del_mum+mum_blr

speed=65

time_taken=total_distance/speed

print("Time Taken to Complete the Journey = ",round(time_taken,2),"hrs")

print(6-5.7) #output will be 0.2999999999999998 because when we use the float value precision is lost
print(round(6-5.7,2))

# stings

text="ice creme"

print(text[0])

# text[1]=g //throws error because strings are immutable in python

print(text[0:3])
print(text[4:])

address="""B-7, WAC, Subroto Park
Dhaula Kuan, New Delhi
Delhi - 110010"""

print(address)

print(text[0:3]+text[4:])

# list

grocery_list=["bread","pasta","vegetables"]
print(grocery_list)

print(grocery_list[1])

grocery_list[2]="chips"

print(grocery_list[-1]) # last element

#grocery_list.append("Butter")
grocery_list.insert(1,"Butter")

print(grocery_list)

bath_items=["soap","shampoo"]

combine_list=grocery_list+bath_items # concatenate two lists
print(len(combine_list))

print("soad" in combine_list) # lookup in list

# if statement
"""
num=input("Enter a Number : ")
if(int(num)%2 == 0):
    print("Even")
else:
    print("Odd")"""

print(4!=5)

print(5>3 and 7<9)

print(not(4==4))

"""indian=["samosa","kachori","golgappe"]
south_indian=["idli","dosa","uttapam"]
chinese=["momos","noodles","manchurian"]

food=input("Enter the Food Item : ")

if food in indian:
    print("Indian")
elif food in south_indian:
    print("South Indian")
elif food in chinese:
    print("Chinese")
else:
    print("FNF")"""


# for loop

exp=[13434,18470,19487,14786]
total_expense=0

for i in exp:
    total_expense+=i

print("Total Expense = ",total_expense)

for i in range(1,11):
    print(i**2)

for i in range(len(exp)):
    print("Month :",i+1," Expense :",exp[i])
    total_expense+=exp[i]

print("Total Expense :",total_expense)


key_location="chair"
locations=["table","bed","chair","microwave"]

for i in locations:
    if key_location == i:
        print("Key Found on",i)
        break
    else:
        print("Key Not Found on",i)

for i in range(6):
    if i%2 == 0:
        continue
    else:
        print(i**2)

# while statement

i=1
while i<=5:
    print(i)
    i+=1

# function [function is a block of code that performs a specific task]

