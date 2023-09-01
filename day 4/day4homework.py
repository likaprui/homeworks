#მომხმარებელს უნდა შემოვატანინოთ ორი სახელი, 
#უნდა დავაპრინტინოთ ის სახელი რომელშიც მეტი თანხმოვანია

name1 = input("enter name1: ")
name2 = input("enter name2: ")
ammount_of_consonant_in_name1 = 0
ammount_of_consonant_in_name2 = 0

for char in name1:
    if char in "bcdfghjklmnpqrstvwxyz":
        ammount_of_consonant_in_name1 +=1
for char in name2:
    if char in "bcdfghjklmnpqrstvwxyz":
        ammount_of_consonant_in_name2 +=1
if ammount_of_consonant_in_name1 > ammount_of_consonant_in_name2:
   print("most ammount of consonant is in {}".format(name1))
elif ammount_of_consonant_in_name2 > ammount_of_consonant_in_name1:
   print("most ammount of consonant is in {}".format(name2))










