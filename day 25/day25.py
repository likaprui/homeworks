
# def index(array, n):
#     if n>len(array)-1:
#         return -1
#     else:
#         return array[n]**n
# print(index([1, 2, 3, 4],2))


# # dictionary.get(keyname, value)
# # get აბრუნებს მოცემული გასაღების მნიშნელობას
# def greet(language):
#     return {
#         'czech': 'Vitejte',
#         'danish': 'Velkomst',
#         'dutch': 'Welkom',
#         'english': 'Welcome',
#         'estonian': 'Tere tulemast',
#         'finnish': 'Tervetuloa',
#         'flemish': 'Welgekomen',
#         'french': 'Bienvenue',
#         'german': 'Willkommen',
#         'irish': 'Failte',
#         'italian': 'Benvenuto',
#         'latvian': 'Gaidits',
#         'lithuanian': 'Laukiamas',
#         'polish': 'Witamy',
#         'spanish': 'Bienvenido',
#         'swedish': 'Valkommen',
#         'welsh': 'Croeso'
#     }.get(language, 'Welcome')
# print(greet('swedish'))
# print(greet('kartuli'))



# # h a n d l i n g
# try:
#     num1=7
#     num2= 0
#     print(num1/num2)
#     print("Done calculation")
# except ZeroDivisionError:
#     print("An error occurred")
#     print("due to zero division")

# try:
#     print(1)
#     print(10/0)
# except TypeError:
#     print(unknown_var)
# finally:
#     print("This is excuted last")




# # r a i s e -raising   ხელოვნური ერორი
# print(1)
# raise ValueError
# print(2)


# #  a s s e r t 
# print(1)
# assert len('lika')!=3  # True
# print(2)
# assert 1+1==3        # assert false = Error
# print(3)

# temp = -10
# assert (temp>= 0), "civa"




