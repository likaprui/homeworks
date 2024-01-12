#      zip ფუნქცია
# def neutralisation(s1,s2):
#     result = ''
    
#     for char1, char2 in zip(s1, s2):
#         if char1 == '+' and char2 == '+':
#             result += '+'
#         elif char1 == '-' and char2 == '-':
#             result += '-'
#         else:
#             result += '0'
    
#     return result
# print(neutralisation("+--+","-+-+"))


# def neutralisation(s1, s2):
#     return ''.join('0' if i != j else i for i, j in zip(s1, s2))
# print(neutralisation("+--+","-+-+"))



# abs _ მოდული
# def twice_as_old(dad_years_old, son_years_old):
#     if dad_years_old-son_years_old*2 >0:
#         return dad_years_old-son_years_old*2
#     else:
#         return (dad_years_old-son_years_old*2)*-1

# def twice_as_old(d, s):
#     return abs(d-2*s)
# print(twice_as_old(66,22))



#
# def first_non_consecutive(arr):
#     i=0
#     for i in range(len(arr)-1):
#         if arr[i+1]==arr[i]+1:
#             i+=1
#         else:
#             return arr[i+1]
# print(first_non_consecutive[1,2,3,4,5,7,8,9])

# def first_non_consecutive(arr):
#     new_arr=[]
#     i=0
#     while i< len(arr)-1:
#         if arr[i+1] - arr[i] !=1:
#             return arr[i+1]
#         i += 1
# print(first_non_consecutive[1,2,3,4,5,7,8,9])



# names_list = ['nika', 'luka', ['mari', 'lizi', ['elene', 'ana']], ['el', ['guja', 'nodo']]]
# print(names_list[2][2][0]) + names_list[3][0] + names_list[3][1][0]



#tuple