# def say_hello(name):
#     print(name+ " gamarjoba")

# say_hello("lika")                       # return ინახავს საცავში ინფორმაციას და ამავდროულად გამოაქვს,
# say_hello("sofi")                         ხოლო print -ს  ერთჯერადად გამოაქვს ტერმინალში შედეგი

# def say_hello(name):
#     return(name+ " gamarjoba")
# print(say_hello("shota"))
# print(say_hello("akaki"))

# def dashla(any_str):
#     return any_str.split()                  # დაშლა
# print(dashla(say_hello("shota")))           # [any_str, "gamarjoba"]


# print(abs(-7))             abc მოდული, პოულობს მანძილს რიცხვიდან ნულამდე


# my_arr= ["shota", "nika", "ilia", "akaki"]

# my_dict = {0: "a",
#            1: "b",
#            2: "c",
#            3: "d"
#            }
# print(my_dict[3])

# Dictionary
# my_students= {
#     "luka": 18,       
#     "nika": 24,
#     "saba": 30,                   # alt ისრები
#     "mzia": 42,
#     "tamo": [21, 12]

    #key:value

# print(my_students["nika"])

# my_students["rustaveli"] = 27
# print(my_students)



                                                                         ### import time # tuple _ მრგვალი ფრჩხილები
# print(my_students.get("mzia"))                                          

# print(list(my_students.items()))         # თითოეული წყვილისგან შემდგარი სია
# print(list(my_students.items())[0][1])


# print(list(my_students.keys()))
# print(list(my_students.values()))

# print(my_students.pop("tamo"))    #pop _ გაგდება
# print(my_students)


# list = [[1, 1], [2, 3], [5, 8, 2]]
# print(list[list[2][list[1][0]]])     # შიგნიდან უნდა მივყვეთ




# def rps(p1, p2):
#     winner_combo = {"rock" : "scissors",
#                     "scissors" : "paper",
#                     "paper" : "rock"}
#     if winner_combo[p1]==p2:
#         return "Player 1 won!"
#     if winner_combo[p2]==p1:
#         return "Player 2 won!"
#     return "Draw!"

# p1="rock"
# p2= "scissors"

# print(rps(p1,p2))



