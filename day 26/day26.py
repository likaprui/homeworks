# ადვილი
# def divisible_by(numbers, divisor):
#     arr_new=[]
#     for char in numbers:
#         if char%divisor==0:
#             arr_new.append(char)
#     return arr_new

# # მოკლე
# return [i for i in numbers if i % divisor==0]



# სტრინგის პირველი ასოს გადიდება _  txt.capitalize()


# def arr(n):
#     return list(range(n))


#              ფუნქცია  x.count()
# def well(x):
#     if x.count("good") == 0:
#         return 'Fail!'
#     elif x.count("good") >=1 and x.count("good"):
#         return 'Publish!'
#     return 'I smell a series!'
# print(well(['bad','bad','bad', 'good','bad']))



# x=int(input("enter integer: "))
# y=int(input("enter your limit: "))

# def find_multiples(integer, limit):
#     return list(range(integer,limit+1,integer))
# print(find_multiples(x,y))

# # find_multiples(5, 25), [5, 10, 15, 20, 25])
# test.assert_equals(find_multiples(1, 2), [1, 2])




# def shortcut( s ):
#     new_s=""
#     for i in s:
#         if i in "aeiou":
#             continue
#         else:
#             new_s+=i
#     return new_s
# print(shortcut("hello"), "hll")
# print(shortcut("hellooooo"), "hll")
# print(shortcut("how are you today?"), "hw r y tdy?")
# print(shortcut("complain"), "cmpln")
# print(shortcut("never"), "nvr")

# # მეორე გზა
# return"".join(i for i in s if i not in "aeiou")

# მესამე 
# for vowel in "aeiou":
#     s = s.replace(vowel,"")
# return s



