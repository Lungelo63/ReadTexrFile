#opening text file...
y = open('DOB.txt' ,'r')

#printting out "name". undername:
#initiating loop to generate the names from 
#the list
print("name")
for i in y:
    name, surname, day, month, year = i.split(" ")
    print(name + " " + surname)
y.close()

#opening a new variable name with the same file
x = open('DOB.txt' ,'r')

#printing out birthdays
#initiating for loop to print out the birthdays
#the birthdays and closing file
print("\nbirthday")
for a in x:
    name, surname, day, month, year = a.split(" ")
    birth = day + " " + month + " " + year.replace("\n", "")
    print(birth)
x.close()






