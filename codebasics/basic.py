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

# https://www.youtube.com/watch?v=hNddJ3_hahk&list=PLeo1K3hjS3us_ELKYSj_Fth2tIEkdKXvV&index=10