# #                    map
# # list - ით გარდაიქმნება map, ვიზუალურად გამოტანისთვის

# def add_five(x):
#     return x + 5

# nums= [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)

# nums= [11, 22, 33, 44, 55]
# result = list(map(lambda x: x+5, nums))
# print(result)



# #                   filter

# nums = [11, 22, 33, 44, 55]
# res= list(filter(lambda x: x % 2 == 0, nums))
# print(res)






# # for loop
# names = ['David', 'John', 'Annabelle', 'Johnathan', 'Veronica']
# long_names = []
# for name in names:
#     if len(name) > 5:
#         long_names.append(name)
# print(long_names)


# # filter
# names = ['David', 'John', 'Annabelle', 'Johnathan', 'Veronica']
# a= list(filter(lambda x: len(x)>5, names))
# print(a)


# # list comprehension
# names = ['David', 'John', 'Annabelle', 'Johnathan', 'Veronica']
# print ([name for name in names if len(name)>5])

 



#     Generators --> yield --> პროგრამას არ არჩერებს

# def infinite_sevens():
#     while True:
#         yield 1

# for i in infinite_sevens():
#     print(i)



# # ['s', 'sp', 'spa', 'spam']
# def make_word():
#     word=""
#     for ch in "spam":
#         word += ch
#         yield word

# def double_string(any_lists):
#     new_list = []
#     for element in any_lists:
#         new_list.append(element + '*')
#     return new_list
# print(double_string(list(make_word())))


# # Decorate --    @ - გამოყენებით ფუნქციები ერთმანეთთან კავშირდება
# def decor(func):
#     def wrap():
#         print("============")       
#         func()
#         print("============")
#     return wrap

# def print_text():
#     print('Hello World!')

# print_text = decor(print_text)

# print_text()


# def decor(func):
#     def wrap():
#         print("============")
#         func()
#         print("============")
#     return wrap

# @decor
# def print_text():
#     print("Hello World!")

# print_text()




# text = input()

# def uppercase_decorator(func):
#     def wrapper(text):
#         return func(text).upper()
#     return wrapper
# @uppercase_decorator
# def display_text(text):
#     return(text)
# print(display_text(text))



# Recursion ---> ფუნქციაში ფუნქციის გამოძახება

